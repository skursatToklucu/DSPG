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

# region Quintuplet
quintupletCombinations = n_length_combo('RLrl', 5)
quinData = []


def create_all_quintuplets():
    item = []
    x = 0
    for quin in quintupletCombinations:
        x = x + 1
        item = {'id': x, 'pattern': quin}
        quinData.append(item)
    return json.dumps(list(quinData))


# endregion

# region Sextuplet
sextupletCombinations = n_length_combo('RLrl', 6)
sextupletData = []


def create_all_sextuplet():
    item = []
    x = 0
    for sextuplet in sextupletCombinations:
        x = x + 1
        item = {'id': x, 'pattern': sextuplet}
        sextupletData.append(item)
    return json.dumps(list(sextupletData))


# endregion


# region Septuplet
septupletCombinations = n_length_combo('RLrl', 7)
septupletData = []


def create_all_septuplets():
    item = []
    x = 0
    for septuplet in septupletCombinations:
        x = x + 1
        item = {'id': x, 'pattern': septuplet}
        septupletData.append(item)
    return json.dumps(list(septupletData))
# endregion


