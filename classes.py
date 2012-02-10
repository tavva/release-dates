class Region:
    def __init__(self, region_id, name, weight, children):
        self.region_id = region_id
        self.name = name
        self.weight = weight
        self.children = children

regions = {
    'india': Region(4, 'india', 3, []),
    'china': Region(5, 'china', 3, []),
    'britain': Region(6, 'britain', 3, []),
    'france': Region(7, 'france', 3, []),
}

regions.update({
    'asia': Region(2, 'asia', 2, [4, 5]),
    'europe': Region(3, 'europe', 2, [6, 7]),
})

regions.update({
    'global': Region(1, 'global', 1, [2, 3]),
})

class Game:
    def __init__(self, name):
        self.name = name

class ReleaseDate:
    def __init__(self, game, region, date):
        self.game = game
        self.date = date
        self.region = region
