import sys


def get_batches(records):
    batch = []
    for record in records:
        temp_array = []
        if (sys.getsizeof(record)) >= 1000000:  # 1MB = 1000000 bytes
            continue
        else:
            if len(temp_array) <= 5 and sys.getsizeof(temp_array) <= 5000000:
                temp_array.append(record)
            else:
                batch.append(temp_array)
                temp_array = []
                temp_array.append(record)

    return batch
