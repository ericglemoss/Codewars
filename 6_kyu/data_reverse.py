# A stream of data is received and needs to be reversed.
# Each segment is 8 bits long, meaning the order of these segments needs to be reversed


def data_reverse(data):
    vec = []
    while data:
        for i in data[-8:]:
            vec.append(i)
        data = data[:-8]
    return vec
