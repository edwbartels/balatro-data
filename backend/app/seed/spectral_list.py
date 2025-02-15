from app.database.models.spectrals import Spectral

spectrals = [
    Spectral(
        name="Ankh", desc="Create a copy of a random Joker, destroy all other Jokers"
    ),
    Spectral(
        name="Aura",
        desc="Add Foil, Holographic, or Polychrome effect to 1 selected card in hand",
    ),
    Spectral(name="Black Hole", desc="Upgrade every poker hand by 1 level"),
    Spectral(name="Cryptid", desc="Create 2 copies of 1 selected card in your hand"),
    Spectral(name="Deja Vu", desc="Add a Red Seal to 1 selected card in your hand"),
    Spectral(name="Ectoplasm", desc="Add Negative to a random Joker, -1 hand size"),
    Spectral(
        name="Familiar",
        desc="Destroy 1 random card in your hand, add 3 random Enhanced face cards to your hand",
    ),
    Spectral(
        name="Grim",
        desc="Destroy 1 random card in your hand, add 2 random Enhanced Aces to your hand",
    ),
    Spectral(
        name="Hex", desc="Add Polychrome to a random Joker, destroy all other Jokers"
    ),
    Spectral(name="Immolate", desc="Destroys 5 random cards in hand, gain $20"),
    Spectral(
        name="Incantation",
        desc="Destroy 1 random card in your hand, add 4 random Enhanced numbered cards to your hand",
    ),
    Spectral(name="Medium", desc="Add a Purple Seal to 1 selected card in your hand"),
    Spectral(
        name="Ouija",
        desc="Converts all cards in hand to a single random rank, -1 hand size",
    ),
    Spectral(name="Sigil", desc="Converts all cards in hand to a single random suit"),
    Spectral(name="The Soul", desc="Creates a Legendary Joker (Must have room)"),
    Spectral(name="Talisman", desc="Add a Gold Seal to 1 selected card in your hand"),
    Spectral(name="Trance", desc="Add a Blue Seal to 1 selected card in your hand"),
    Spectral(name="Wraith", desc="Creates a random Rare Joker, sets money to $0"),
]
