import sys


class RecordsBuilder(object):
    """
    This class creates the batches with suitable delivery size
    to a system in a form of an array.
    """
    def make_batches(self, records):
        batch = []
        temp_array = []
        for record in records:
            if (sys.getsizeof(record)) >= 1000000:  # 1MB = 1000000 bytes. I tested with 35.
                continue
            else:
                if len(temp_array) < 500 and sys.getsizeof(temp_array) <= 5000000:  # I tested with <5 and <=80
                    temp_array.append(record)
                else:
                    batch.append(temp_array)
                    temp_array = []
                    temp_array.append(record)

        batch.append(temp_array)
        return batch

