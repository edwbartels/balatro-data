import zlib
from lua_to_json import convert_save_to_json


def read_save_file(filename, output_file):
    with open(filename, "rb") as f:
        compressed_data = f.read()

    decompressed = zlib.decompress(compressed_data, wbits=-zlib.MAX_WBITS)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(decompressed.decode("utf-8"))
        read_game_state(output_file)


def read_game_state(save_file_path: str) -> dict:
    return convert_save_to_json(save_file_path)


if __name__ == "__main__":
    # Example usage
    save_data = read_game_state("../save_state.lua")
    print(f"Current state: {save_data['STATE']}")
