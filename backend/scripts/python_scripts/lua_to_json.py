import json
import subprocess
import os
from pathlib import Path
from typing import Dict, Any


def convert_save_to_json(save_file_path: str, keep_json: bool = True) -> Dict[str, Any]:
    """
    Convert a Balatro save file to JSON using Lua and load it

    Args:
        save_file_path (str): Path to the save file
        keep_json (bool): Whether to keep the intermediate JSON file (default: False)

    Returns:
        dict: The parsed save data
    """
    # Convert paths to absolute paths
    save_file_path = os.path.abspath(save_file_path)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    lua_script = os.path.join(script_dir, "..", "lua-scripts", "save_to_json.lua")
    json_file = os.path.splitext(save_file_path)[0] + ".json"

    try:
        # Run Lua conversion script
        result = subprocess.run(
            ["lua", lua_script, save_file_path, json_file],
            capture_output=True,
            text=True,
            check=True,
        )

        if result.stdout:
            print(result.stdout)

        # Load the converted JSON
        with open(json_file) as f:
            data = json.load(f)

        # Clean up JSON file unless keep_json is True
        if not keep_json:
            os.remove(json_file)

        return data

    except subprocess.CalledProcessError as e:
        print(f"Error running Lua script: {e.stderr}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise
    finally:
        # Make sure we clean up the JSON file if something went wrong
        if not keep_json and os.path.exists(json_file):
            os.remove(json_file)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert Balatro save file to JSON")
    parser.add_argument("save_file", help="Path to the save file")
    parser.add_argument(
        "--keep-json", action="store_true", help="Keep the intermediate JSON file"
    )
    parser.add_argument("--output", help="Path to write output JSON file")

    args = parser.parse_args()

    # Convert and load the save data
    save_data = convert_save_to_json(args.save_file, args.keep_json)

    # Write to output file if specified
    if args.output:
        with open(args.output, "w") as f:
            json.dump(save_data, f, indent=2)
        print(f"\nFull save data written to {args.output}")
