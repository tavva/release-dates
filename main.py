import datetime

from job import Calculator

from classes import Game, ReleaseDate, regions

if __name__ == "__main__":
    game = Game('Super Mental 2')

    release_dates = [
        ReleaseDate(game, datetime.date(2012, 1, 1), regions['global']),
        ReleaseDate(game, datetime.date(2012, 1, 2), regions['asia']),
        ReleaseDate(game, datetime.date(2012, 1, 3), regions['europe']),
        ReleaseDate(game, datetime.date(2012, 1, 4), regions['china']),
        ReleaseDate(game, datetime.date(2012, 1, 5), regions['britain']),
    ]

    Calculator.run(dates)
