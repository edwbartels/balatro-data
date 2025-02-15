from app.database.models.decks import Deck

decks = [
    Deck(id="b_red", name="Red Deck", desc="+1 discard every round"),
    Deck(id="b_blue", name="Blue Deck", desc="+1 hand every round"),
    Deck(id="b_yellow", name="Yellow Deck", desc="Start with an extra $10"),
    Deck(
        id="b_green",
        name="Green Deck",
        desc="You don't earn interest. Instead, gain $2 per remaining Hand and $1 per remaining Discard at the end of each round.",
    ),
    Deck(
        id="b_black", name="Black Deck", desc="+1 Joker slot, but -2 hand every round"
    ),
    Deck(
        id="b_magic",
        name="Magic Deck",
        desc="Start run with the Crystal Ball voucher and 2 copies of The Fool",
    ),
    Deck(
        id="b_nebula",
        name="Nebula Deck",
        desc="Start run with the Telescrope voucher but -1 consumable slot",
    ),
    Deck(
        id="b_ghost",
        name="Ghost Deck",
        desc="Spectral Cards may appear individually in the shop, and you start with a Hex card",
    ),
    Deck(
        id="b_abandoned",
        name="Abandoned Deck",
        desc="Start run with no Face Cards(Jacks, Queens, or Kings) in your deck",
    ),
    Deck(
        id="b_checkered",
        name="Checkered Deck",
        desc="Start run with 26 Spades and 26 Hears in deck, and no Clubs or Diamonds",
    ),
    Deck(
        id="b_zodiac",
        name="Zodiac Deck",
        desc="Start the run with Tarot Merchant, Planet Merchant, and Overstock vouchers",
    ),
    Deck(id="b_painted", name="Painted Deck", desc="+2 Hand Size, -1 Joker Slot"),
    Deck(
        id="b_anaglyph",
        name="Anaglyph Deck",
        desc="After defeating each Boss Blind, gain a Double Tag",
    ),
    Deck(
        id="b_plasma",
        name="Plasma Deck",
        desc="Balance Chips and Mult when calculating scor for played hand. X2 base Blind size. (Your chips and mult become averaged before scoring)",
    ),
    Deck(
        id="b_erratic",
        name="Erratic Deck",
        desc="All Ranks and Suits in deck are randomized",
    ),
]
