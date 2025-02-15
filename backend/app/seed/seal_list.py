from app.database.models.seals import Seal

seals = [
    Seal(name="Gold", desc="Earn $3 when this card is played and scores"),
    Seal(
        name="Red",
        desc="Retrigger this card 1 time. As well as when being scored in a poker hand, this also includes in-hand effects",
    ),
    Seal(
        name="Blue",
        desc="Creates a Planet card for the final played poker hand of round if held in hand (Must have room)",
    ),
    Seal(name="Purple", desc="Creates a Tarot card when discarded (Must have room)"),
]
