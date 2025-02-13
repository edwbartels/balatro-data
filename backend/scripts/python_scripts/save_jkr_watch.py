import os
import time
from datetime import datetime
import argparse


def watch_file(filepath, interval=1):
    """
    Watch for file creation and modifications.
    If the file doesn't exist, wait for it to be created.

    Args:
        filepath (str): Path to the file to watch
        interval (int): Time in seconds between checks
    """
    print(f"Starting watch for {filepath}")

    last_modified = None
    last_size = None
    file_exists = False

    try:
        while True:
            current_exists = os.path.exists(filepath)

            # Handle file creation
            if current_exists and not file_exists:
                print(
                    f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
                    f"File was created"
                )
                file_exists = True
                last_modified = os.path.getmtime(filepath)
                last_size = os.path.getsize(filepath)
                print(f"Initial size: {last_size} bytes")

            # Handle file deletion
            elif not current_exists and file_exists:
                print(
                    f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
                    f"File was deleted"
                )
                print("Watching for recreation...")
                file_exists = False
                last_modified = None
                last_size = None

            # Check for modifications if file exists
            elif current_exists:
                current_modified = os.path.getmtime(filepath)
                current_size = os.path.getsize(filepath)

                if current_modified != last_modified:
                    print(
                        f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
                        f"File was modified"
                    )
                    print(
                        f"New size: {current_size} bytes "
                        f"({current_size - last_size:+d} bytes)"
                    )

                    last_modified = current_modified
                    last_size = current_size

            # File doesn't exist yet
            else:
                if last_modified is None:  # Only print once when starting
                    print("Waiting for file to be created...")
                    last_modified = 0

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nWatch stopped by user")
    except Exception as e:
        print(f"\nError: {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Watch for file creation and modifications"
    )
    parser.add_argument("filepath", help="Path to the file to watch")
    parser.add_argument(
        "-i",
        "--interval",
        type=int,
        default=1,
        help="Check interval in seconds (default: 1)",
    )

    args = parser.parse_args()
    watch_file(args.filepath, args.interval)
