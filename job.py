from mrjob.job import MRJob

class Calculator(MRJob):
    def mapper(self, node):
        yield node.region, node

        for region in node.region.children:
            yield region, node

    def reducer(self, region, dates):
        sort_key = lambda date: date.weight
        yield region, max(sorted(dates, key=sort_key))
