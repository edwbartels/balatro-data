import os
import time
import zlib
import json
import subprocess
from datetime import datetime
from typing import Dict, Set, Any, Union
from dataclasses import dataclass
from pathlib import Path
from app.util.process_change import process_change
from app.util.process_save_json import process_save_file
from app.util.db_inserts import update_db
from app.util.db_updates import update_win


@dataclass
class WatcherConfig:
    save_file: str
    temp_lua_file: str
    temp_json_file: str
    lua_converter_script: str
    fields_to_watch: Set[str]
    check_interval: int = 1


class StateWatcher:
    def __init__(self, config: WatcherConfig):
        self.config = config
        self.last_modified_time = 0
        self.last_state: Dict[str, Any] = {}

    def get_nested_value(self, data: Dict[str, Any], field_path: str) -> Any:
        """
        Get a value from nested dictionary using either dot notation or dict notation
        Examples:
            - "GAME.STOP_USE"
            - "GAME['STOP_USE']"
            - "GAME[\"STOP_USE\"]"
        """
        # Handle dictionary-style notation
        if "[" in field_path:
            parts = (
                field_path.replace("]", "").replace('"', "").replace("'", "").split("[")
            )
            current = data
            for part in parts:
                if part not in current:
                    return None
                current = current[part]
            return current

        # Handle dot notation
        parts = field_path.split(".")
        current = data
        for part in parts:
            if part not in current:
                return None
            current = current[part]
        return current

    def decompress_save(self, save_file: str, output_file: str) -> None:
        """Decompress the .jkr save file into a Lua file"""
        with open(save_file, "rb") as f:
            compressed_data = f.read()

        decompressed = zlib.decompress(compressed_data, wbits=-zlib.MAX_WBITS)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(decompressed.decode("utf-8"))

    def convert_lua_to_json(self, lua_file: str, json_file: str) -> None:
        """Convert Lua file to JSON using the Lua converter script"""
        result = subprocess.run(
            ["lua", self.config.lua_converter_script, lua_file, json_file],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError(f"Lua conversion failed: {result.stderr}")

    def load_json_state(self, json_file: str) -> Dict[str, Any]:
        """Load and parse the JSON state file"""
        with open(json_file, "r") as f:
            return json.load(f)

    def detect_field_changes(self, new_state: Dict[str, Any]) -> Dict[str, tuple]:
        """Detect changes in watched fields between states"""
        changes = {}
        for field in self.config.fields_to_watch:
            old_value = self.get_nested_value(self.last_state, field)
            new_value = self.get_nested_value(new_state, field)
            if old_value != new_value:
                changes[field] = (old_value, new_value)
        return changes

    def process_state_update(self) -> None:
        """Process a complete state update cycle"""
        try:
            # Decompress .jkr to Lua
            self.decompress_save(self.config.save_file, self.config.temp_lua_file)

            # Convert Lua to JSON
            self.convert_lua_to_json(
                self.config.temp_lua_file, self.config.temp_json_file
            )

            # Load new state
            new_state = self.load_json_state(self.config.temp_json_file)

            # Detect and report changes
            if self.last_state:  # Only check for changes if we have a previous state
                changes = self.detect_field_changes(new_state)
                if changes:
                    print(
                        f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] State changes detected:"
                    )
                    print("changes", changes.items())
                    filtered_save = process_save_file(new_state)
                    if "won" in changes.keys():
                        update_win(filtered_save)
                    update_db(filtered_save)
                    # print(filtered_save)
                    # for field, (old_val, new_val) in changes.items():
                    #     if field == "GAME.round":
                    #         print("Jokers: ")
                    #         for idx, joker in enumerate(
                    #             new_state["cardAreas"]["jokers"]["cards"].values()
                    #         ):
                    #             print(
                    #                 f"    label: {joker['label']}, save_fields.center: {joker['save_fields']['center']}, edition: {joker['edition']['type'] if 'edition' in joker.keys() else 'base'}"
                    #             )
                    #             # print(joker["ability"]["name"])
                    #             # print(f"{joker['name']}\n")
                    #         # print(new_state.keys())
                    #         # print(new_state["cardAreas"]["jokers"]["cards"])
                    #         # print(new_state.cardAreas.jokers)
                    #         # for joker in new_state.cardAreas.jokers.cards:
                    #         #     print(f"{joker.name}\n")
                    #         print("\n")
                    #     # elif field == "cardAreas.deck.cards":
                    #     #     continue
                    #     # elif (
                    #     #     field == "GAME.round"
                    #     #     or field == "GAME.pseudorandom.hashed_seed"
                    #     # ):
                    #     #     process_change(new_state)
                    #     #     print(f"  {field}: {old_val} -> {new_val}")

                    #     # else:
                    #     #     print(f"  {field}: {old_val} -> {new_val}")
            else:
                print(
                    f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Initial state loaded"
                )
                # Print initial values of watched fields
                filtered_save = process_save_file(new_state)
                # print(type(filtered_save))
                update_db(filtered_save)
                # print(filtered_save)

            #     for field in self.config.fields_to_watch:
            #         value = self.get_nested_value(new_state, field)
            #         if field in [
            #             "cardAreas.jokers.cards",
            #             "GAME.pseudorandom.hashed_seed",
            #         ]:
            #             filtered_save = process_save_file(new_state)
            #             print(filtered_save)
            #         # elif field == "cardAreas.deck.cards":
            #         #     for card in new_state["cardAreas"]["deck"]["cards"].values():
            #         #         "card"
            #         #         "edition" in card and print(card["edition"])
            #         #         "effect" in card["ability"] and print(
            #         #             card["ability"]["effect"]
            #         #         )
            #         #         "seal" in card and print(card["seal"])
            #         # else:
            #         #     print(f"  {field}: {value}")

            #         # process_change(new_state)

            # # Update last state
            self.last_state = new_state

        except Exception as e:
            print(f"Error processing state update: {e}")

    def watch(self) -> None:
        """Main watch loop"""
        print(f"Starting state watcher...")
        print(f"Watching save file: {self.config.save_file}")
        print(f"Tracking fields: {', '.join(self.config.fields_to_watch)}")

        while True:
            try:
                if os.path.exists(self.config.save_file):
                    current_modified_time = os.path.getmtime(self.config.save_file)

                    if current_modified_time > self.last_modified_time:
                        print(
                            f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Save file updated"
                        )
                        self.process_state_update()
                        self.last_modified_time = current_modified_time
                else:
                    if self.last_modified_time != 0:  # File was deleted
                        print(
                            f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Save file deleted"
                        )
                        self.last_modified_time = 0
                        self.last_state = {}

            except Exception as e:
                print(f"Error in watch loop: {e}")

            time.sleep(self.config.check_interval)


def main():
    # Configuration
    config = WatcherConfig(
        save_file="/mnt/c/Users/Maljik/AppData/Roaming/Balatro/1/save.jkr",
        temp_lua_file="/mnt/c/Users/Maljik/Documents/coding-projects/balatro/dashboard/backend/scripts/python_scripts/save_state.lua",
        temp_json_file="/mnt/c/Users/Maljik/Documents/coding-projects/balatro/dashboard/backend/scripts/python_scripts/save_state.json",
        lua_converter_script="/mnt/c/Users/Maljik/Documents/coding-projects/balatro/dashboard/backend/scripts/lua-scripts/save_to_json.lua",
        fields_to_watch={
            # "STATE",
            # "BACK",
            # "BLIND",
            # "GAME.pool_flags",
            # "tags",
            # "cardAreas.deck.cards",
            # "BLIND.boss",
            # "BLIND.disabled",
            # "BLIND.name",
            # "GAME.bosses_used",
            # "GAME.cards_played",
            # "GAME.consumeable_usage",
            # "GAME.hands_played",
            # "GAME.interest_ammount",
            # "GAME.interest_cap",
            "GAME.round",
            # "BACK.key",
            "GAME.pseudorandom.hashed_seed",
            # "GAME.round_resets.blind_states",
            # "GAME.subhash",
            # "GAME.bosses_used",
            # "GAME.used_vouchers",
            # "GAME.tags",
            # "GAME.used_jokers",
            "GAME.won",
            # "GAME.used_vouchers",
            # "GAME.woncardAreas.consumeables.cards",
            # "cardAreas.deck.cards"
            # "cardAreas.jokers.cards",
            # "GAME.round_resets.blind_tags",
            # "GAME.tags",
            # "tags",
            # "GAME['CURRENT_ROUND']",  # Using dictionary notation
        },
    )

    # Create and run watcher
    watcher = StateWatcher(config)
    watcher.watch()


if __name__ == "__main__":
    main()
