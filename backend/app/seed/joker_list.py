from app.database.models.jokers import (
    Joker,
    JokerEdition,
    JokerInstance,
    JokerPersistence,
)
from sqlalchemy.orm import Session
from itertools import product


jokers = [
    Joker(
        id="j_8_ball",
        name="8 Ball",
        rarity=1,
        desc="1 in 2 chance for each played 8 to create a Tarot card when scored (Must have room)",
    ),
    Joker(
        id="j_abstract",
        name="Abstract Joker",
        rarity=1,
        desc="+3 Mult for each Joker card",
    ),
    Joker(
        id="j_acrobat", name="Acrobat", rarity=2, desc="X3 Mult on final hand of round"
    ),
    Joker(
        id="j_ancient",
        name="Ancient Joker",
        rarity=3,
        desc="Each played card with *suit* gives X1.5 Mult when scored, suit changes at end of round",
    ),
    Joker(
        id="j_arrowhead",
        name="Arrowhead",
        rarity=2,
        desc="Played cards with Spade suit give +50 Chips when scored",
    ),
    Joker(
        id="j_astronomer",
        name="Astronomer",
        rarity=2,
        desc="All Planet cards and Celestial Packs in the shop are free",
    ),
    Joker(
        id="j_banner",
        name="Banner",
        rarity=1,
        desc="+30 Chips for each remaining discard",
    ),
    Joker(
        id="j_baron",
        name="Baron",
        rarity=3,
        desc="Each King held in hand gives X1.5 Mult",
    ),
    Joker(
        id="j_baseball",
        name="Baseball Card",
        rarity=3,
        desc="Uncommon Jokers each give X1.5 Mult",
    ),
    Joker(
        id="j_blackboard",
        name="Blackboard",
        rarity=2,
        desc="X3 Mult if all cards held in hand are Spades or Clubs",
    ),
    Joker(
        id="j_bloodstone",
        name="Bloodstone",
        rarity=2,
        desc="1 in 2 chance for played cards with the Heart suit to give X1.5 Mult when scored",
    ),
    Joker(
        id="j_blue_joker",
        name="Blue Joker",
        rarity=1,
        desc="+2 Chips for each remaining card in deck",
    ),
    Joker(
        id="j_blueprint",
        name="Blueprint",
        rarity=3,
        desc="Copies ability of Joker to the right",
    ),
    Joker(
        id="j_bootstraps",
        name="Bootstraps",
        rarity=2,
        desc="Have at least 2 Polychrome Jokers at the same time",
    ),
    Joker(
        id="j_brainstorm",
        name="Brainstorm",
        rarity=3,
        desc="Copies the ability of leftmost Joker",
    ),
    Joker(id="bull", name="Bull", rarity=2, desc="+2 Chips for each $1 you have"),
    Joker(
        id="j_burglar",
        name="Burglar",
        rarity=2,
        desc="When Blind is selected, gain +3 Hands and lose all discards",
    ),
    Joker(
        id="j_burnt",
        name="Burnt Joker",
        rarity=2,
        desc="Upgrade the level of the first discarded poker hand each round",
    ),
    Joker(
        id="j_business",
        name="Business Card",
        rarity=1,
        desc="Played face cards have a 1 in 2 chance to give $2 when scored",
    ),
    Joker(
        id="j_campfire",
        name="Campfire",
        rarity=3,
        desc="This Joker gains X0.25 Mult for each card sold, resets when Boss Blind is defeated",
    ),
    Joker(
        id="j_caino",
        name="Canio",
        rarity=4,
        desc="This Joker gains X1 Mult when a face card is destroyed",
    ),
    Joker(
        id="j_card_sharp",
        name="Card Sharp",
        rarity=2,
        desc="X3 Mult if played poker hand has already been played this round",
    ),
    Joker(
        id="j_cartomancer",
        name="Cartomancer",
        rarity=2,
        desc="Create a Tarot card when Blind is selected (Must have room)",
    ),
    Joker(
        id="j_castle",
        name="Castle",
        rarity=2,
        desc="This Joker gains +3 Chips per discarded *suit* card, suit changes every round",
    ),
    Joker(
        id="j_cavendish",
        name="Cavendish",
        rarity=1,
        desc="X3 Mult, 1 in 1000 chance this card is destroyed at end of round",
    ),
    Joker(
        id="j_ceremonial",
        name="Ceremonial Dagger",
        rarity=2,
        desc="When Blind is selected, destroy Joker to the right and permanently add double its sell value to this Mult",
    ),
    Joker(
        id="j_certificate",
        name="Certificate",
        rarity=2,
        desc="When round begins, add a random playing card with a random seal to your hand",
    ),
    Joker(
        id="j_chaos", name="Chaos the Clown", rarity=1, desc="1 free Reroll per shop"
    ),
    Joker(
        id="j_chicot",
        name="Chicot",
        rarity=4,
        desc="Disables effect of every Boss Blind",
    ),
    Joker(
        id="j_clever",
        name="Clever Joker",
        rarity=1,
        desc="+80 Chips if played hand contains a Two Pair",
    ),
    Joker(
        id="j_cloud_9",
        name="Cloud 9",
        rarity=2,
        desc="Earn $1 for each 9 in your full deck at end of round",
    ),
    Joker(
        id="j_constellation",
        name="Constellation",
        rarity=2,
        desc="This Joker gains X0.1 Mult every time a Planet card is used",
    ),
    Joker(
        id="j_crafty",
        name="Crafty Joker",
        rarity=1,
        desc="+80 Chips if played hand contains a Flush",
    ),
    Joker(
        id="j_crazy",
        name="Crazy Joker",
        rarity=1,
        desc="+12 Mult if played hand contains a Straight",
    ),
    Joker(
        id="j_credit_card", name="Credit Card", rarity=1, desc="Go up to -$20 in debt"
    ),
    Joker(
        id="j_dna",
        name="DNA",
        rarity=3,
        desc="If first hand of round has only 1 card, add a permanent copy to deck and draw it to hand",
    ),
    Joker(
        id="j_delayed_grat",
        name="Delayed Gratification",
        rarity=1,
        desc="Earn $2 per discard if no discards are used by end of the round",
    ),
    Joker(
        id="j_devious",
        name="Devious Joker",
        rarity=1,
        desc="+100 Chips if played hand contains a Straight",
    ),
    Joker(
        id="j_diet_cola",
        name="Diet Cola",
        rarity=2,
        desc="Sell this card to create a free Double Tag",
    ),
    Joker(
        id="j_drivers_license",
        name="Driver's License",
        rarity=3,
        desc="X3 Mult if you have at least 16 Enhanced cards in your full deck",
    ),
    Joker(
        id="j_droll",
        name="Droll Joker",
        rarity=1,
        desc="+10 Mult if played hand contains a Flush",
    ),
    Joker(id="j_drunkard", name="Drunkard", rarity=1, desc="+1 discard each round"),
    Joker(
        id="j_dusk",
        name="Dusk",
        rarity=2,
        desc="Retrigger all played cards in final hand of round",
    ),
    Joker(
        id="j_egg", name="Egg", rarity=1, desc="Gains $3 of sell value at end of round"
    ),
    Joker(
        id="j_erosion",
        name="Erosion",
        rarity=2,
        desc="+4 Mult for each card below *the deck's starting size* in your full deck",
    ),
    Joker(
        id="j_even_steven",
        name="Even Steven",
        rarity=1,
        desc="Played cards with even rank give +4 Mult when scored (10, 8, 6, 4, 2)",
    ),
    Joker(
        id="j_faceless",
        name="Faceless Joker",
        rarity=1,
        desc="Earn $5 if 3 or more face cards are discarded at the same time",
    ),
    Joker(
        id="j_fibonacci",
        name="Fibonacci",
        rarity=2,
        desc="Each played Ace, 2, 3, 5, or 8 gives +8 Mult when scored",
    ),
    Joker(
        id="j_flash",
        name="Flash Card",
        rarity=2,
        desc="This Joker gains +2 Mult per reroll in the shop",
    ),
    Joker(
        id="j_flower_pot",
        name="Flower Pot",
        rarity=2,
        desc="X3 Mult if poker hand contains a Diamond card, Club card, Heart card, and Spade card",
    ),
    Joker(
        id="j_fortune_teller",
        name="Fortune Teller",
        rarity=1,
        desc="+1 Mult per Tarot card used this run",
    ),
    Joker(
        id="j_four_fingers",
        name="Four Fingers",
        rarity=2,
        desc="All Flushes and Straights can be made with 4 cards",
    ),
    Joker(
        id="j_gift",
        name="Gift Card",
        rarity=2,
        desc="Add $1 of sell value to every Joker and Consumable card at end of round",
    ),
    Joker(
        id="j_glass",
        name="Glass Joker",
        rarity=2,
        desc="This Joker gains X0.75 Mult for every Glass Card that is destroyed",
    ),
    Joker(
        id="j_gluttenous_joker",
        name="Gluttonous Joker",
        rarity=1,
        desc="Played cards with Club suit give +3 Mult when scored",
    ),
    Joker(id="j_golden", name="Golden Joker", rarity=1, desc="Earn $4 at end of round"),
    Joker(
        id="j_ticket",
        name="Golden Ticket",
        rarity=1,
        desc="Played Gold cards earn $4 when scored",
    ),
    Joker(
        id="j_greedy_joker",
        name="Greedy Joker",
        rarity=1,
        desc="Played cards with Diamond suit give +3 Mult when scored",
    ),
    Joker(
        id="j_green_joker",
        name="Green Joker",
        rarity=1,
        desc="+1 Mult per hand played, -1 Mult per discard",
    ),
    Joker(
        id="j_gros_michel",
        name="Gros Michel",
        rarity=1,
        desc="+15 Mult, 1 in 6 chance this card is destroyed at end of round",
    ),
    Joker(
        id="j_hack", name="Hack", rarity=2, desc="Retrigger each played 2, 3, 4, or 5"
    ),
    Joker(
        id="j_half",
        name="Half Joker",
        rarity=1,
        desc="+20 Mult if played hand contains 3 or fewer cards",
    ),
    Joker(
        id="j_hallucination",
        name="Hallucination",
        rarity=1,
        desc="1 in 2 chance to create a Tarot card when any Booster Pack is opened (Must have room)",
    ),
    Joker(
        id="j_hanging_chad",
        name="Hanging Chad",
        rarity=1,
        desc="Retrigger first played card used in scoring 2 additional times",
    ),
    Joker(
        id="j_hiker",
        name="Hiker",
        rarity=2,
        desc="Every played card permanently gains +5 Chips when scored",
    ),
    Joker(
        id="j_hit_the_road",
        name="Hit the Road",
        rarity=3,
        desc="This Joker gains X0.5 Mult for every Jack discarded this round",
    ),
    Joker(
        id="j_hologram",
        name="Hologram",
        rarity=2,
        desc="This Joker gains X0.25 Mult every time a playing card is added to your deck",
    ),
    Joker(
        id="j_ice_cream",
        name="Ice Cream",
        rarity=1,
        desc="+100 Chips, -5 Chips for every hand played",
    ),
    Joker(
        id="j_invisible",
        name="Invisible Joker",
        rarity=3,
        desc="After 2 rounds, sell this card to Duplicate a random Joker",
    ),
    Joker(id="j_joker", name="Joker", rarity=1, desc="+4 Mult"),
    Joker(
        id="j_stencil",
        name="Joker Stencil",
        rarity=2,
        desc="X1 Mult for each empty Joker slot, Joker Stencil included",
    ),
    Joker(
        id="j_jolly",
        name="Jolly Joker",
        rarity=1,
        desc="+8 Mult if played hand contains a Pair",
    ),
    Joker(id="j_juggler", name="Juggler", rarity=1, desc="+1 hand size"),
    Joker(
        id="j_loyalty_card",
        name="Loyalty Card",
        rarity=2,
        desc="X4 Mult every 6 hands played",
    ),
    Joker(
        id="j_luchador",
        name="Luchador",
        rarity=2,
        desc="Sell this card to disable the current Boss Blind",
    ),
    Joker(
        id="j_lucky_cat",
        name="Lucky Cat",
        rarity=2,
        desc="This Joker gains X0.25 Mult every time a Lucky card successfully triggers",
    ),
    Joker(
        id="j_lusty_joker",
        name="Lusty Joker",
        rarity=1,
        desc="Played cards with Heart suit give +3 Mult when scored",
    ),
    Joker(
        id="j_mad",
        name="Mad Joker",
        rarity=1,
        desc="+10 Mult if played hand contains a Two Pair",
    ),
    Joker(
        id="j_madness",
        name="Madness",
        rarity=2,
        desc="When Small Blind or Big Blind is selected, gain X0.5 Mult and destroy a random Joker",
    ),
    Joker(
        id="j_mail",
        name="Mail-In Rebate",
        rarity=1,
        desc="Earn $5 for each discarded *rank*, rank changes every round",
    ),
    Joker(
        id="j_marble",
        name="Marble Joker",
        rarity=2,
        desc="Adds one Stone card to deck when Blind is selected",
    ),
    Joker(
        id="j_matador",
        name="Matador",
        rarity=2,
        desc="Earn $8 if played hand triggers the Boss Blind ability",
    ),
    Joker(
        id="j_merry_andy",
        name="Merry Andy",
        rarity=2,
        desc="+3 discards each round, -1 hand size",
    ),
    Joker(
        id="j_midas_mask",
        name="Midas Mask",
        rarity=2,
        desc="All played face cards become Gold cards when scored",
    ),
    Joker(
        id="j_mime",
        name="Mime",
        rarity=2,
        desc="Retrigger all card held in hand abilities",
    ),
    Joker(
        id="j_misprint",
        name="Misprint",
        rarity=1,
        desc="adds a random Mult value from 0 to 23",
    ),
    Joker(
        id="j_mr_bones",
        name="Mr. Bones",
        rarity=2,
        desc="Prevents Death if chips scored are at least 25% of required chips, self destructs",
    ),
    Joker(
        id="j_mystic_summit",
        name="Mystic Summit",
        rarity=1,
        desc="+15 Mult when 0 discards remaining",
    ),
    Joker(
        id="j_obelisk",
        name="Obelisk",
        rarity=3,
        desc="This Joker gains X0.2 Mult per consecutive hand played without playing your most played poker hand",
    ),
    Joker(
        id="j_odd_todd",
        name="Odd Todd",
        rarity=1,
        desc="Played cards with odd rank give +31 Chips when scored (A, 9, 7, 5, 3)",
    ),
    Joker(
        id="j_onyx_agate",
        name="Onyx Agate",
        rarity=2,
        desc="Played cards with Club suit give +7 Mult when scored",
    ),
    Joker(
        id="j_oops",
        name="Oops! All 6s",
        rarity=2,
        desc="Doubles all listed probabilities (ex: 1 in 3 -> 2 in 3)",
    ),
    Joker(
        id="j_pareidolia",
        name="Pareidolia",
        rarity=2,
        desc="All cards are considered face cards",
    ),
    Joker(
        id="j_perkeo",
        name="Perkeo",
        rarity=4,
        desc="Creates a Negative copy of 1 random consumable card in your possession at the end of the shop",
    ),
    Joker(
        id="j_photograph",
        name="Photograph",
        rarity=1,
        desc="First played face card gives X2 Mult when scored",
    ),
    Joker(
        id="j_popcorn",
        name="Popcorn",
        rarity=1,
        desc="+20 Mult -4 Mult per round played",
    ),
    Joker(
        id="j_raised_fist",
        name="Raised Fist",
        rarity=1,
        desc="Adds double the rank of lowest ranked card held in hand to Mult",
    ),
    Joker(
        id="j_ramen",
        name="Ramen",
        rarity=2,
        desc="X2 Mult, loses X0.01 Mult per card discarded",
    ),
    Joker(
        id="j_red_card",
        name="Red Card",
        rarity=1,
        desc="This Joker gains +3 Mult when any Booster Pack is skipped",
    ),
    Joker(
        id="j_reserved_parking",
        name="Reserved Parking",
        rarity=2,
        desc="Each face card held in hand has a 1 in 2 chance to give $1",
    ),
    Joker(
        id="j_ride_the_bus",
        name="Ride the Bus",
        rarity=1,
        desc="This Joker gains +1 Mult per consecutive hand played without a scoring face card",
    ),
    Joker(
        id="j_riff_raff",
        name="Riff-raff",
        rarity=1,
        desc="When Blind is selected, create 2 Common Jokers (Must have room)",
    ),
    Joker(
        id="j_rocket",
        name="Rocket",
        rarity=2,
        desc="Earn $1 at end of round. Payout increases by $2 when Boss Blind is defeated",
    ),
    Joker(
        id="j_rough_gem",
        name="Rough Gem",
        rarity=2,
        desc="Played cards with Diamond suit earn $1 when scored",
    ),
    Joker(
        id="j_runner",
        name="Runner",
        rarity=1,
        desc="Gains +15 Chips if played hand contains a Straight",
    ),
    Joker(
        id="j_satellite",
        name="Satellite",
        rarity=2,
        desc="Earn $1 at end of round per unique Planet card used this run",
    ),
    Joker(
        id="j_scary_face",
        name="Scary Face",
        rarity=1,
        desc="Played face cards give +30 Chips when scored",
    ),
    Joker(
        id="j_scholar",
        name="Scholar",
        rarity=1,
        desc="Played Aces give +20 Chips and +4 Mult when scored",
    ),
    Joker(
        id="j_seance",
        name="Seance",
        rarity=3,
        desc="If poker hand is a Straight Flush, create a random Spectral card (Must have room)",
    ),
    Joker(
        id="j_seeing_double",
        name="Seeing Double",
        rarity=2,
        desc="X2 Mult if played hand has a scoring Club card and a scoring card of any other suit",
    ),
    Joker(
        id="j_seltzer",
        name="Seltzer",
        rarity=2,
        desc="Retrigger all cards played for the next 10 hands",
    ),
    Joker(
        id="j_shoot_the_moon",
        name="Shoot the Moon",
        rarity=1,
        desc="Each Queen held in hand gives +13 Mult",
    ),
    Joker(
        id="j_shortcut",
        name="Shortcut",
        rarity=2,
        desc="Allows Straights to be made with gaps of 1 rank (ex: 10 8 6 5 3)",
    ),
    Joker(
        id="j_ring_master",
        name="Showman",
        rarity=2,
        desc="Joker, Tarot, Planet, and Spectral cards may appear multiple times",
    ),
    Joker(
        id="j_sixth_sense",
        name="Sixth Sense",
        rarity=3,
        desc="If first hand of round is a single 6, destroy it and create a Spectral card (Must have room)",
    ),
    Joker(
        id="j_sly",
        name="Sly Joker",
        rarity=1,
        desc="+50 Chips if played hand contains a Pair",
    ),
    Joker(
        id="j_smeared",
        name="Smeared Joker",
        rarity=2,
        desc="Hearts and Diamonds count as the same suit, Spades and Clubs count as the same suit",
    ),
    Joker(
        id="j_smiley",
        name="Smiley Face",
        rarity=1,
        desc="Played face cards give +5 Mult when scored",
    ),
    Joker(
        id="j_sock_and_buskin",
        name="Sock and Buskin",
        rarity=2,
        desc="Retrigger all played face cards",
    ),
    Joker(
        id="j_space",
        name="Space Joker",
        rarity=2,
        desc="1 in 4 chance to upgrade level of played poker hand",
    ),
    Joker(
        id="j_trousers",
        name="Spare Trousers",
        rarity=2,
        desc="This Joker gains +2 Mult if played hand contains a Two Pair",
    ),
    Joker(
        id="j_splash",
        name="Splash",
        rarity=1,
        desc="Every played card counts in scoring",
    ),
    Joker(
        id="j_square",
        name="Square Joker",
        rarity=1,
        desc="This Joker gains +4 Chips if played hand has exactly 4 cards",
    ),
    Joker(
        id="j_steel_joker",
        name="Steel Joker",
        rarity=2,
        desc="Gives X0.2 Mult for each Steel Card in your full deck",
    ),
    Joker(
        id="j_stone",
        name="Stone Joker",
        rarity=2,
        desc="Gives +25 Chips for each Stone Card in your full deck",
    ),
    Joker(id="j_stuntman", name="Stuntman", rarity=2, desc="+250 Chips, -2 hand size"),
    Joker(
        id="j_supernova",
        name="Supernova",
        rarity=1,
        desc="Adds the number of times poker hand has been played this run to Mult",
    ),
    Joker(
        id="j_superposition",
        name="Superposition",
        rarity=1,
        desc="Create a Tarot card if poker hand contains an Ace and a Straight (Must have room)",
    ),
    Joker(
        id="j_swashbuckler",
        name="Swashbuckler",
        rarity=1,
        desc="Adds the sell value of all other owned Jokers to Mult",
    ),
    Joker(
        id="j_duo",
        name="The Duo",
        rarity=3,
        desc="X2 Mult if played hand contains a Pair",
    ),
    Joker(
        id="j_family",
        name="The Family",
        rarity=3,
        desc="X4 Mult if played hand contains a Four of a Kind",
    ),
    Joker(
        id="j_idol",
        name="The Idol",
        rarity=2,
        desc="Each played *rank* of *suit* gives X2 Mult when scored, Card changes every round",
    ),
    Joker(
        id="j_order",
        name="The Order",
        rarity=3,
        desc="X3 Mult if played hand contains a Straight",
    ),
    Joker(
        id="j_tribe",
        name="The Tribe",
        rarity=3,
        desc="X2 Mult if played hand contains a Flush",
    ),
    Joker(
        id="j_trio",
        name="The Trio",
        rarity=3,
        desc="X3 Mult if played hand contains a Three of a Kind",
    ),
    Joker(
        id="j_throwback",
        name="Throwback",
        rarity=2,
        desc="X0.25 Mult for each Blind skipped this run",
    ),
    Joker(
        id="j_todo_list",
        name="To Do List",
        rarity=1,
        desc="Earn $4 if poker hand is a *poker hand*, poker hand changes at end of round",
    ),
    Joker(
        id="j_to_the_moon",
        name="To The Moon",
        rarity=2,
        desc="Earn an extra $1 of interest for every $5 you have at end of round",
    ),
    Joker(
        id="j_trading",
        name="Trading Card",
        rarity=2,
        desc="If first discard of round has only 1 card, destroy it and earn $3",
    ),
    Joker(
        id="j_triboulet",
        name="Triboulet",
        rarity=4,
        desc="Played Kings and Queens each give X2 Mult when scored",
    ),
    Joker(
        id="j_troubadour",
        name="Troubadour",
        rarity=2,
        desc="+2 hand size, -1 hand each round",
    ),
    Joker(
        id="j_turtle_bean",
        name="Turtle Bean",
        rarity=2,
        desc="+5 hand size, reduces by 1 every round",
    ),
    Joker(
        id="j_vagabond",
        name="Vagabond",
        rarity=3,
        desc="Create a Tarot card if hand is played with $4 or less",
    ),
    Joker(
        id="j_vampire",
        name="Vampire",
        rarity=2,
        desc="This Joker gains X0.1 Mult per scoring Enhanced card played, removes card Enhancement",
    ),
    Joker(
        id="j_walkie_talkie",
        name="Walkie Talkie",
        rarity=1,
        desc="Each played 10 or 4 gives +10 Chips and +4 Mult when scored",
    ),
    Joker(
        id="j_wee",
        name="Wee Joker",
        rarity=3,
        desc="This Joker gains +8 Chips when each played 2 is scored",
    ),
    Joker(
        id="j_wily",
        name="Wily Joker",
        rarity=1,
        desc="+100 Chips if played hand contains a Three of a Kind",
    ),
    Joker(
        id="j_wrathful_joker",
        name="Wrathful Joker",
        rarity=1,
        desc="Played cards with Spade suit give +3 Mult when scored",
    ),
    Joker(
        id="j_yorick",
        name="Yorick",
        rarity=4,
        desc="This Joker gains X1 Mult every 23 cards discarded",
    ),
    Joker(
        id="j_zany",
        name="Zany Joker",
        rarity=1,
        desc="+12 Mult if played hand contains a Three of a Kind",
    ),
]


def create_all_joker_instances(session: Session) -> None:
    editions = list(JokerEdition)
    persistence_states = list(JokerPersistence)
    rental_states = [True, False]

    base_jokers = session.query(Joker).all()

    for joker in base_jokers:
        combinations = product([joker.id], editions, persistence_states, rental_states)

        for joker_id, edition, persistence, is_rental in combinations:
            instance = JokerInstance(
                joker_id=joker_id,
                edition=edition,
                persistence=persistence,
                is_rental=is_rental,
            )
            session.add(instance)

    session.commit()


def calc_expected():
    num_editions = len(JokerEdition)
    num_persistence = len(JokerPersistence)
    num_rental = 2

    return num_editions * num_persistence * num_rental


def verify_seed(session: Session) -> None:
    expected_per_joker = calc_expected()
    expected_total = 0
    result_total = 0
    for joker in session.query(Joker).all():
        instance_count = (
            session.query(JokerInstance)
            .filter(JokerInstance.joker_id == joker.id)
            .count()
        )
        expected_total += expected_per_joker
        result_total += instance_count

        print(f"{joker.name}: {instance_count} instances")
        print(f"Expected: {expected_per_joker} instances")

    print(f"Expected {expected_total} joker_instances.")
    print(f"Seeded {result_total} joker_instances.")
