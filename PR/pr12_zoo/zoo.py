"""A small exercise in zookeeping."""


class Animal:
    """Animal."""

    def __init__(self, species: str, scientific_name: str, age_up_to: int, weight_range: tuple, height_range: tuple,
                 diet: str, habitat: str):
        """Initialize the Animal object."""
        self.species = species
        self.scientific_name = scientific_name
        self.age_up_to = age_up_to
        self.weight_range = weight_range
        self.height_range = height_range
        self.diet = diet
        self.habitat = habitat

    def __repr__(self):
        """Animal object representation."""
        return self.species


def find_smallest_animal_by_weight(animal_list: list) -> Animal:
    """Testeri lemmik osa."""
    minimal = min(animal_list, key=lambda x: x.weight_range[0])

    return minimal


def list_species_and_scientific_names(animal_list: list) -> list:
    """Testeri lemmik osa."""
    result_list = []
    for an in animal_list:
        result_list.append((an.species, an.scientific_name))
    return result_list


def find_how_many_pumpkins_are_needed_to_feed_animals(animal_list: list) -> int:
    """Testeri lemmik osa."""
    result = 0
    for an in animal_list:
        if an.diet != "carnivorous":
            medium_weight_x2 = (an.weight_range[0] + an.weight_range[1])  # [x2] because 2 animals of every type
            eat_at_day = round((medium_weight_x2 * 0.06), 1)
            eat_pumpkin = eat_at_day / 3
            eat_90 = eat_pumpkin * 90
            result += eat_90
            # print(medium_weight_x2, eat_at_day, eat_pumpkin, eat_90)
    return int(result)


def sort_alphabetically_by_scientific_name(animal_list: list) -> list:
    """Testeri lemmik osa."""
    sorted_list = sorted(animal_list, key=lambda x: x.scientific_name)
    return sorted_list


def find_animals_whose_height_is_less_than(animal_list: list, height_limit: int) -> list:
    """Testeri lemmik osa."""
    filtered = filter(lambda x: x.height_range[1] < height_limit, animal_list)
    result = list(filtered)
    return result


def filter_animals_based_on_diet(animal_list: list, diet: str) -> list:
    """Testeri lemmik osa."""
    filtered = filter(lambda x: x.diet == diet, animal_list)
    result = list(filtered)
    return result


def find_animal_with_longest_lifespan(animal_list: list) -> Animal:
    """Testeri lemmik osa."""
    max_life = max(animal_list, key=lambda x: x.age_up_to)
    return max_life


def create_animal_descriptions(animal_list: list) -> list:
    """Testeri lemmik osa."""
    res_list = []
    for an in animal_list:
        out_string = f"{an.species} ({an.scientific_name}) lives in {an.habitat} and its diet is {an.diet}. " \
                     f"These animals can live up to {an.age_up_to} years and they weigh between {an.weight_range[0]} " \
                     f"kg and {an.weight_range[1]} kg as adults."
        res_list.append(out_string)

    return res_list
