import itertools
import json
from itertools import combinations


def n_length_combo(arr, n):
    return list(map(''.join, itertools.product(arr, repeat=n)))


# region Triplet
tripletCombinations = n_length_combo('RLrl', 3)
tripletData = []


def create_all_triplets():
    item = []
    x = 0
    for triplet in tripletCombinations:
        x = x + 1
        item = {'id': x, 'pattern': triplet}
        tripletData.append(item)
    return json.dumps(list(tripletData))


# endregion


# region Cuarta
cuartaCombinations = n_length_combo('RLrl', 4)
cuartaData = []


def create_all_cuartas():
    item = []
    x = 0
    for cuarta in cuartaCombinations:
        x = x + 1
        item = {'id': x, 'pattern': cuarta}
        cuartaData.append(item)
    return json.dumps(list(cuartaData))
# endregion
