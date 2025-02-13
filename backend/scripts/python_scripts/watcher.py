import time
import os
from read_game_state import read_save_file


def check_file():
    print("Starting file monitor...")
    last_size = 0
    while True:
        try:
            if os.path.exists(
                "/mnt/f/SteamLibrary/steamapps/common/Balatro/round_trigger.txt"
            ):
                current_size = os.path.getsize(
                    "/mnt/f/SteamLibrary/steamapps/common/Balatro/round_trigger.txt"
                )
                if current_size > last_size:
                    with open(
                        "/mnt/f/SteamLibrary/steamapps/common/Balatro/round_trigger.txt",
                        "r",
                    ) as f:
                        print("New round detected!")
                        read_save_file(
                            "/mnt/c/Users/Maljik/AppData/Roaming/Balatro/1/save.jkr",
                            "../save_states/save_state.lua",
                        )
                        print(f.read())
                    last_size = current_size
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(5)  # Check every five seconds


if __name__ == "__main__":
    check_file()
