from app.database.models.tarots import Tarot

tarots = [
    Tarot(
        name="The Chariot",
        desc="Enhances 1 selected card into a Steel card",
    ),
    Tarot(
        name="Death",
        desc="Select 2 cards, convert the left card into the right card (Drag to rearrange)",
    ),
    Tarot(
        name="The Devil",
        desc="Enhances 1 selected card into a Gold card",
    ),
    Tarot(
        name="The Emperor",
        desc="Creates up to 2 random Tarot cards (Must have room)",
    ),
    Tarot(
        name="The Empress",
        desc="Enhances 2 selected cards into Mult cards",
    ),
    Tarot(
        name="The Fool",
        desc="Creates the last Tarot or Planet card used during this run (The Fool excluded)",
    ),
    Tarot(
        name="The Hanged Man",
        desc="Destroys up to 2 selected cards",
    ),
    Tarot(
        name="The Hierophant",
        desc="Enhances 2 selected cards to Bonus cards",
    ),
    Tarot(name="The Hermit", desc="Doubles money (Max of $20)"),
    Tarot(
        name="The High Priestess",
        desc="Creates up to 2 random Planet cards (Must have room)",
    ),
    Tarot(
        name="Judgement",
        desc="Creates a random Joker card (Must have room)",
    ),
    Tarot(
        name="Justice",
        desc="Enhances 1 selected card into a Glass card",
    ),
    Tarot(
        name="The Lovers",
        desc="Enhances 1 selected card into a Wild card",
    ),
    Tarot(
        name="The Magician",
        desc="Enhances 2 selected cards into Lucky cards",
    ),
    Tarot(name="The Moon", desc="Converts up to 3 selected cards to Clubs"),
    Tarot(
        name="The Star",
        desc="Converts up to 3 selected cards to Diamonds",
    ),
    Tarot(
        name="Strength",
        desc="Increases rank of up to 2 selected cards by 1",
    ),
    Tarot(name="The Sun", desc="Converts up to 3 selected cards to Hearts"),
    Tarot(
        name="Temperance",
        desc="Gives the total sell value of all current Jokers (Max of $50)",
    ),
    Tarot(
        name="The Tower",
        desc="Enhances 1 selected card into a Stone card",
    ),
    Tarot(
        name="The Wheel of Fortune",
        desc="1 in 4 chance to add Foil, Holographic, or Polychrome edition to a random Joker",
    ),
    Tarot(
        name="The World",
        desc="Converts up to 3 selected cards to Spades",
    ),
]
