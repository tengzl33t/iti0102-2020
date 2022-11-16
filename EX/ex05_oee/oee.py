"""EX05 - OEE."""
import csv


def read_production_data(filename: str) -> dict:
    """See, mida tester tahab."""
    file_list = []
    file_dict = {}

    try:

        with open(filename, encoding="utf-8") as file:
            for line in file:
                file_list.append(line.strip().split(","))

            for i in file_list:
                keys = i[0]
                values = i[1:]
                values = [int(i) for i in values]
                file_dict.setdefault(keys, values)

    except FileNotFoundError:
        print({})

    return file_dict


def calculate_quality(production_data: dict) -> dict:
    """See, mida tester tahab."""
    result = {}

    file_dict = production_data
    for k, v in file_dict.items():
        if v[2] != 0:
            result[k] = round(((v[3] / v[2]) * 100), 1)
        else:
            result[k] = 0

    return result


def calculate_availability(production_data: dict) -> dict:
    """See, mida tester tahab."""
    result = {}
    file_dict = production_data
    for k, v in file_dict.items():
        result[k] = round(((v[0] / 420) * 100), 1)

    return result


def calculate_performance(production_data: dict) -> dict:
    """See, mida tester tahab."""
    result = {}
    file_dict = production_data
    for k, v in file_dict.items():
        if v[0] != 0 or v[1] != 0:
            result[k] = round((((v[2] / v[0]) / v[1]) * 100), 1)
        else:
            result[k] = 0

    return result


def calculate_oee(production_data: dict) -> dict:
    """See, mida tester tahab."""
    resultdict = {}
    perf = calculate_performance(production_data)
    av = calculate_availability(production_data)
    qual = calculate_quality(production_data)

    for k, v in perf.items():
        resultdict.setdefault(k, []).append(v)
    for k, v in av.items():
        resultdict[k].append(v)
    for k, v in qual.items():
        resultdict[k].append(v)

    for k, v in resultdict.items():
        resultdict[k] = round(((v[0] * v[1] * v[2]) / 10000), 1)

    return resultdict


def write_results_to_file(production_data: dict, filename: str):
    """See, mida tester tahab."""
    oee = calculate_oee(production_data)
    perf = calculate_performance(production_data)
    av = calculate_availability(production_data)
    qual = calculate_quality(production_data)

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["Liin", "Saadavus", "Tootlus", "Kvaliteet", "OEE"])
        for k in oee.keys() | perf.keys() | av.keys() | qual.keys():
            writer.writerow([k, av[k], perf[k], qual[k], oee[k]])

    pass
