from app.database.models.packs import Pack


packs = [
    Pack(cat="standard", family="normal", size=3, selections=1),
    Pack(cat="standard", family="arcana", size=3, selections=1),
    Pack(cat="standard", family="celestial", size=3, selections=1),
    Pack(cat="standard", family="buffoon", size=2, selections=1),
    Pack(cat="standard", family="spectral", size=2, selections=1),
    Pack(cat="jumbo", family="normal", size=5, selections=1),
    Pack(cat="jumbo", family="arcana", size=5, selections=1),
    Pack(cat="jumbo", family="celestial", size=5, selections=1),
    Pack(cat="jumbo", family="buffoon", size=4, selections=1),
    Pack(cat="jumbo", family="spectral", size=4, selections=1),
    Pack(cat="mega", family="normal", size=5, selections=2),
    Pack(cat="mega", family="arcana", size=5, selections=2),
    Pack(cat="mega", family="celestial", size=5, selections=2),
    Pack(cat="mega", family="buffoon", size=4, selections=2),
    Pack(cat="mega", family="spectral", size=4, selections=2),
]
