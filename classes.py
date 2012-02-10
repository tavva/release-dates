class Region:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

regions = {
    'india': Region('india', 3, []),
    'china': Region('china', 3, []),
    'britain': Region('britain', 3, []),
    'france': Region('france', 3, []),
}

regions.update({
    'asia': Region('asia', 2, [regions['india'], regions['china']]),
    'europe': Region('europe', 2, [regions['britain'], regions['france']]),
})

regions.update({
    'global': Region('global', 1, [regions['asia'], regions['europe']]),
})

class Game:
    def __init__(self, name):
        self.name = name

class ReleaseDate:
    def __init__(self, game, date, region):
        self.game = game
        self.date = date
        self.region = region
