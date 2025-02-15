from app.database.models.editions import Edition

editions = [
    Edition(name="Base", desc="No extra effects"),
    Edition(name="Foil", desc="+50 Chips"),
    Edition(name="Holographic", desc="+10 Mult"),
    Edition(name="Polychrome", desc="X1.5 Mult"),
    Edition(
        name="Negative",
        desc="+1 Joker slot when on Jokers, +1 Consumable slot when on Consumables (only through Perkeo)",
    ),
]
