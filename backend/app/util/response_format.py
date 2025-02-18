def format_deck_response(deck_data):
    formatted_stats = {}

    for stat in deck_data.pop("stake_stats", []):
        formatted_stats[stat]["stake"] = {
            "win_rate": stat["win_rate"],
            "win_rate_updated_at": stat["win_rate_updated_at"],
        }

    deck_data["stake_stats"] = formatted_stats

    return deck_data
