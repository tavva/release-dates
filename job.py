from mrjob.job import MRJob

from classes import regions

class Calculator(MRJob):
    def mapper(self, key, line):
        date, region_name, weight = line.split(',')

        region = regions[region_name]

        yield region, (date, weight)

        for region_name in region.children:
            yield regions[region_name], (date, weight)

    def reducer(self, region, values):
        sort_key = lambda date: date[1]

        yield region, sorted(values, key=sort_key)[0][0]

if __name__ == "__main__":
    Calculator.run()
