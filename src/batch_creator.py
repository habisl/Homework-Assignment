"""
Main function to form the batches
"""

import sys


def make_batches(records):
    batch = []
    temp_array = []
    for record in records:
        if (sys.getsizeof(record)) >= 1000000:  # 1MB = 1000000 bytes
            continue
        else:
            if len(temp_array) < 5 and sys.getsizeof(temp_array) <= 50:
                temp_array.append(record)
            else:
                batch.append(temp_array)
                temp_array = []
                temp_array.append(record)

    batch.append(temp_array)
    return batch
