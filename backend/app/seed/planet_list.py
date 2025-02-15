from app.database.models.planets import Planet


planets = [
    Planet(name="Pluto", hand="High Card", chips=10, mult=1),
    Planet(name="Mercury", hand="Pair", chips=15, mult=10),
    Planet(name="Uranus", hand="Two Pair", chips=20, mult=1),
    Planet(name="Venus", hand="Three of a Kind", chips=20, mult=2),
    Planet(name="Saturn", hand="Straight", chips=30, mult=3),
    Planet(name="Jupiter", hand="Flush", chips=15, mult=2),
    Planet(name="Earth", hand="Full House", chips=25, mult=2),
    Planet(name="Mars", hand="Four of a Kind", chips=30, mult=3),
    Planet(name="Neptune", hand="Straight Flush", chips=40, mult=4),
    Planet(name="Planet X", hand="Five of a Kind", chips=35, mult=3),
    Planet(name="Ceres", hand="Flush House", chips=40, mult=4),
    Planet(name="Eris", hand="Flush Five", chips=50, mult=3),
]
