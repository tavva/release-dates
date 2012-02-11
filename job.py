from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol, PickleProtocol, RawValueProtocol

from classes import regions

class Calculator(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    OUTPUT_PROTOCOL = JSONValueProtocol

    def mapper(self, key, line):
        date, region_name, weight = line.split(',')

        region = regions[region_name]

        yield region, (date, weight)

        for region in region.children:
            yield region, (date, weight)

    def reducer(self, region, values):
        sort_key = lambda date: -int(date[1])

        yield region.name, (region.name, sorted(values, key=sort_key)[0][0])

if __name__ == "__main__":
    Calculator.run()
