from types import SimpleNamespace
import json
from typing import Dict, Any, Optional


class DotDict:
    """Convert nested dictionary to dot notation access with defaults"""

    def __init__(self, dictionary: Dict[str, Any], defaults: Dict[str, Any] = None):
        self._defaults = defaults or {}

        for key, value in dictionary.items():
            if isinstance(value, dict):
                # Pass along any nested defaults
                nested_defaults = (
                    self._defaults.get(key, {})
                    if isinstance(self._defaults.get(key), dict)
                    else {}
                )
                setattr(self, key, DotDict(value, nested_defaults))
            else:
                setattr(self, key, value)

    def __getattr__(self, name):
        # Return default value if key doesn't exist
        try:
            return super().__getattribute__(name)
        except AttributeError:
            if name in self._defaults:
                default_value = self._defaults[name]

                if isinstance(default_value, dict):
                    return DotDict(default_value)
                return default_value
            return None

    def get(self, name, default=None):
        value = getattr(self, name, default)
        return value if value is not None else default

    def __str__(self):
        return json.dumps(self._to_dict(), indent=2)

    def _to_dict(self):
        result = {}
        for key, value in vars(self).items():
            if key != "_defaults":
                if isinstance(value, DotDict):
                    result[key] = value._to_dict()
                else:
                    result[key] = value
        return result


def filter_game_state(
    data: Dict[str, Any],
    keys_to_keep: Optional[Dict[str, Any]] = None,
    defaults: Optional[Dict[str, Any]] = None,
) -> DotDict:
    """
    Filter game state and apply default values

    Args:
        data: The full game state dictionary
        keys_to_keep: Dictionary specifying which keys to keep
        defaults: Dictionary specifying default values for missing keys
    """
    if keys_to_keep is None:
        keys_to_keep = custom_keys

    if defaults is None:
        defaults = custom_defaults

    def filter_dict(d: Dict[str, Any], filter_keys: Dict[str, Any]) -> Dict[str, Any]:
        if filter_keys is None:
            return d
        if not isinstance(d, dict):
            return d
        if callable(filter_keys):
            return filter_keys(d)

        result = {}
        for key, value in d.items():
            if key in filter_keys:
                if isinstance(filter_keys[key], dict):
                    result[key] = filter_dict(value, filter_keys[key])
                else:  # filter_keys[key] is None, meaning keep all
                    result[key] = value
            elif "*" in filter_keys:
                if callable(filter_keys["*"]):
                    result[key] = filter_keys["*"](value)
                else:
                    result[key] = filter_dict(value, filter_keys["*"])
        return result

    filtered_data = filter_dict(data, keys_to_keep)
    return DotDict(filtered_data, defaults)


def process_save_file(
    json_data: str | Dict[str, Any],
    keys_to_keep: Optional[Dict[str, Any]] = None,
    defaults: Optional[Dict[str, Any]] = None,
) -> DotDict:
    """
    Process save file with custom keys to keep and defaults

    Args:
        json_data: JSON string or dictionary of game state
        keys_to_keep: Dictionary specifying which keys to keep
        defaults: Dictionary specifying default values for missing keys
    """
    if isinstance(json_data, str):
        data = json.loads(json_data)
    else:
        data = json_data
        # print(json_data)

    return filter_game_state(data, keys_to_keep, defaults)


# Example usage:
if __name__ == "__main__":
    # Example custom defaults
    custom_defaults = {
        "GAME": {
            "dollars": 0,
            "chips": 0,
            "round": 1,
            "stake": 1,
            "hands_played": 0,
            "current_round": {
                "hands_left": 4,
                "discards_left": 2,
                "hands_played": 0,
                "dollars": 0,
            },
        }
    }

    # Example keys to keep - now using consistent dictionary structure
    custom_keys = {
        "GAME": {
            "dollars": None,
            "chips": None,
            "round": None,
            "current_round": {"hands_left": None, "discards_left": None},
        }
    }

    # Example usage:
    # state = process_save_file(game_data, custom_keys, custom_defaults)
    # print(state.GAME.dollars)
    # print(state.GAME.current_round.hands_left)


def create_card_filter(base_ability_keys, special_card_configs):
    def filter_card(card_data):
        if not isinstance(card_data, dict):
            return card_data

        result = {}

        card_id = card_data.get("save_fields", {}).get("center")

        ability_keys = base_ability_keys.copy()

        if card_id in special_card_configs:
            ability_keys.update(special_card_configs[card_id])

        for key, value in card_data.items():
            if key == "ability":
                result[key] = {k: v for k, v in value.items() if k in ability_keys}
            elif key in base_card_keys:
                result[key] = value
        return result

    return filter_card


base_ability_keys = {
    "eternal": None,
    "perishable": None,
    "perish_tally": None,
    "rental": None,
}

special_card_configs = {
    "j_todo_list": {
        "to_do_poker_hand": None,
    }
}

base_card_keys = {"save_fields": None, "label": None, "edition": None}

custom_keys = {
    "BACK": {"key": None},
    "BLIND": {
        "boss": None,
        "chips": None,
        "config_blind": None,
        "disabled": None,
        "name": None,
    },
    "GAME": {
        "bosses_used": {
            "bl_arm": None,
            "bl_club": None,
            "bl_eye": None,
            "bl_final_acorn": None,
            "bl_final_bell": None,
            "bl_final_heart": None,
            "bl_final_leaf": None,
            "bl_final_vessel": None,
            "bl_fish": None,
            "bl_flint": None,
            "bl_goad": None,
            "bl_head": None,
            "bl_hook": None,
            "bl_house": None,
            "bl_manacle": None,
            "bl_mark": None,
            "bl_mouth": None,
            "bl_needle": None,
            "bl_ox": None,
            "bl_pillar": None,
            "bl_plant": None,
            "bl_psychic": None,
            "bl_serpent": None,
            "bl_tooth": None,
            "bl_wall": None,
            "bl_water": None,
            "bl_wheel": None,
            "bl_window": None,
        },
        "chips": None,
        "facing_blind": None,
        "first_shop_bufoon": None,
        "last_blind": {"boss": None, "name": None},
        "pool_flags": {"gros_michel_extinct": None},
        "pseudorandom": {"hashed_seed": None, "seed": None},
        "round": None,
        "round_resets": {
            "blind": {"boss": None, "defeated": None, "key": None},
            "blind_ante": None,
            "blind_states": {"Big": None, "Boss": None, "Small": None},
            "blind_tags": {"Big": None, "Small": None},
            "boss_rerolled": None,
            "loc_blind_states": {"Big": None, "Boss": None, "Small": None},
        },
        "stake": None,
        "used_jokers": None,
        "used_vouchers": None,
        "won": None,
    },
    # "cardAreas": {
    #     "jokers": {
    #         "cards": {"*": create_card_filter(base_ability_keys, special_card_configs)}
    #     }
    # },
    "cardAreas": {"jokers": {"cards": None}},
}

custom_defaults = {
    "BLIND": {"boss": False, "chips": 0, "disabled": False, "name": ""},
    "GAME": {
        "bosses_used": {
            "bl_arm": 0,
            "bl_club": 0,
            "bl_eye": 0,
            "bl_final_acorn": 0,
            "bl_final_bell": 0,
            "bl_final_heart": 0,
            "bl_final_leaf": 0,
            "bl_final_vessel": 0,
            "bl_fish": 0,
            "bl_flint": 0,
            "bl_goad": 0,
            "bl_head": 0,
            "bl_hook": 0,
            "bl_house": 0,
            "bl_manacle": 0,
            "bl_mark": 0,
            "bl_mouth": 0,
            "bl_needle": 0,
            "bl_ox": 0,
            "bl_pillar": 0,
            "bl_plant": 0,
            "bl_psychic": 0,
            "bl_serpent": 0,
            "bl_tooth": 0,
            "bl_wall": 0,
            "bl_water": 0,
            "bl_wheel": 0,
            "bl_window": 0,
        },
        "chips": 0,
        "first_shop_bufoon": False,
        "last_blind": {"boss": False, "name": ""},
        "pool_flags": {"gros_michel_extinct": False},
        "won": False,
    },
    "cardAreas": {"jokers": {"cards": {}}},
}
