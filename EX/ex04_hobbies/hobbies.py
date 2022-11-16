"""Hobbies."""
import csv


def create_list_from_file(file) -> list:
    """Sample text."""
    file_list = []
    with open(file, encoding="utf-8") as file:
        for line in file:
            file_list.append(line.strip())

    return file_list


def create_dictionary(file) -> dict:
    """Sample text."""
    file_dict = {}
    file_list = create_list_from_file(file)
    for i in range(len(file_list)):
        splitted = file_list[i].split(":")
        name = splitted[0]
        hobby = splitted[1]

        if name in file_dict:
            file_dict[name].append(hobby)
        else:
            file_dict.setdefault(name, []).append(hobby)

    file_dict_result = {key: list(set(value)) for key, value in file_dict.items()}

    return file_dict_result


def find_person_with_most_hobbies(file):
    """Sample text."""
    file_dict = create_dictionary(file)
    res_keys = []

    for k, v in file_dict.items():
        file_dict[k] = len(v)

    value = max(file_dict.values())

    for k, v in file_dict.items():
        if v == value:
            res_keys.append(k)

    return res_keys


def find_person_with_least_hobbies(file):
    """Sample text."""
    file_dict = create_dictionary(file)
    res_keys = []

    for k, v in file_dict.items():
        file_dict[k] = len(v)

    value = min(file_dict.values())

    for k, v in file_dict.items():
        if v == value:
            res_keys.append(k)
    return res_keys


def find_most_popular_hobby(file):
    """Sample text."""
    file_dict = create_dictionary(file)
    hobby_list = []
    hobby_list_count = []
    res_list = []

    for v in file_dict.values():
        for i in v:
            hobby_list.append(i)
    hobby_list = sorted(hobby_list)

    for a in hobby_list:
        freq = hobby_list.count(a)
        hobby_list_count.append(freq)
        hobby_max = max(hobby_list_count)

    for i in hobby_list:
        if hobby_list.count(i) == hobby_max:
            res_list.append(i)

    res_list = list(set(res_list))
    return res_list


def find_least_popular_hobby(file):
    """Sample text."""
    file_dict = create_dictionary(file)
    hobby_list = []
    hobby_list_count = []
    res_list = []

    for v in file_dict.values():
        for i in v:
            hobby_list.append(i)
    hobby_list = sorted(hobby_list)

    for a in hobby_list:
        freq = hobby_list.count(a)
        hobby_list_count.append(freq)
        hobby_min = min(hobby_list_count)

    for i in hobby_list:
        if hobby_list.count(i) == hobby_min:
            res_list.append(i)

    res_list = list(set(res_list))
    return res_list


def write_corrected_database(file, file_to_write):
    """Sample text."""
    file_dict = create_dictionary(file)

    with open(file_to_write, "w", newline="") as csvfile:

        writer = csv.writer(csvfile, delimiter=",")
        name = "Name"
        hobbies = "Hobbies"
        writer.writerow([name, hobbies])
        for k in sorted(file_dict.keys()):
            row = [k, "-".join(sorted(file_dict[k]))]
            writer.writerow(row)
