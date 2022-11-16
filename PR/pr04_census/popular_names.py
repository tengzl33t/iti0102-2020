"""Order names by popularity."""


def read_from_file() -> list:
    """Sample text."""
    names = []
    with open("popular_names.txt", encoding="utf-8") as file:
        for line in file:
            names.append(line.strip())

    return names


def to_dictionary(names: list) -> dict:
    """Sample text."""
    names_dict = {}
    if names:
        for i in names:
            if i not in names_dict:
                names_dict[i] = names.count(i)

    return names_dict


def to_sex_dicts(names_dict: dict) -> tuple:
    """Sample text."""
    male_names = {}
    female_names = {}
    for i in names_dict:
        sex_value = i[-1]
        a = i[:-2]
        if sex_value == "M":
            male_names[a] = names_dict[i]
        else:
            female_names[a] = names_dict[i]
    return (male_names, female_names)


def most_popular(names_dict: dict) -> str:
    """Sample text."""
    if names_dict:
        max_count = max(names_dict, key=names_dict.get)
    else:
        max_count = "Empty dictionary."

    return max_count


def number_of_people(names_dict: dict) -> int:
    """Sample text."""
    counter = 0
    for i in names_dict:
        counter += names_dict[i]

    return counter


def names_by_popularity(names_dict: dict) -> str:
    """Sample text."""
    if names_dict:
        sorted_dict = sorted(names_dict, key=names_dict.get, reverse=True)
        sorted_values = sorted(names_dict.values(), reverse=True)

        rankings = ""
        index = 0
        for i in range(len(sorted_dict)):
            index = index + 1
            res_string = (
                str(index) + ". " + sorted_dict[i] + ": " + str(sorted_values[i]) + "\n"
            )
            rankings += res_string

        return rankings
    else:
        return ""
