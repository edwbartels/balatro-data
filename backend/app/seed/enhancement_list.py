from app.database.models.enhancements import Enhancement

enhancements = [
    Enhancement(name="Bonus", desc="+30 Chips"),
    Enhancement(name="Mult", desc="+4 Mult"),
    Enhancement(name="Wild", desc="Is considered to be every suit simultaneously"),
    Enhancement(
        name="Glass",
        desc="X2 Mult, 1 in 4 chance to destroy card after all scoring is finished",
    ),
    Enhancement(name="Steel", desc="X1.5 Mult while this card stays in hand"),
    Enhancement(name="Stone", desc="+50 Chips, No rank or sui, Card always scores"),
    Enhancement(name="Gold", desc="$3 if this card is held in hand at end of round"),
    Enhancement(
        name="Lucky",
        desc="1 in 5 chance for +20 Mult, 1 in 15 chance to win $20, (Both can trigger on the same turn)",
    ),
]
