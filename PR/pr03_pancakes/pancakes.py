"""Pancakes."""


def make_n_pancakes(n: int, ingredients: list) -> int:
    """Sample text."""
    dough_count = make_dough(ingredients)
    pancakes = 0

    while can_make_pancake(dough_count) and n > 0:
        dough_count = make_a_pancake(dough_count)
        n -= 1
        pancakes += 1

    return pancakes


def make_dough(ingredients: list) -> int:
    """Sample text."""
    all_count = 0
    dough_amount = 0

    egg_count = ingredients.count("egg")
    milk_count = ingredients.count("milk")
    flour_count = ingredients.count("flour")
    butter_count = ingredients.count("butter")
    sugar_count = ingredients.count("sugar")

    while (
        egg_count >= 1
        and milk_count >= 5
        and flour_count >= 4
        and butter_count >= 1
        and sugar_count >= 2
    ):
        egg_count -= 1
        milk_count -= 5
        flour_count -= 4
        butter_count -= 1
        sugar_count -= 2

        all_count += 1

    while all_count >= 1:
        dough_amount += 7
        all_count -= 1

    return dough_amount


def can_make_pancake(dough: float) -> bool:
    """Sample text."""
    if dough >= 0.8:
        return True
    else:
        return False


def make_a_pancake(dough: float) -> float:
    """Sample text."""
    if can_make_pancake(dough) is True:
        rest_dough = round(dough - 0.8, 2)
        return rest_dough


if __name__ == "__main__":
    ingredients = ["egg"] + ["milk"] * 5 + ["flour"] * 4 + ["butter"] + ["sugar"]
    print(make_dough(ingredients))  # 0 -> not enough sugar.
    ingredients2 = (
        ["egg"] * 4 + ["milk"] * 9 + ["flour"] * 14 + ["butter"] * 3 + ["sugar"] * 7
    )
    print(make_dough(ingredients2))  # 7 -> can make 7dl dough not 7.x dl.
    ingredients3 = (
        ["egg" for _ in range(3)]
        + ["milk" for _ in range(15)]
        + ["flour" for _ in range(7)]
        + ["butter" for _ in range(3)]
        + ["sugar" for _ in range(2)]
    )
    print(make_n_pancakes(8, ingredients3))  # 8
    ingredients4 = (
        ["egg" for _ in range(21)]
        + ["milk" for _ in range(45)]
        + ["flour" for _ in range(4)]
        + ["butter" for _ in range(14)]
        + ["sugar" for _ in range(12)]
    )
    # 4 -> 7dl dough, 0.8dl per pancake -> could make 8 pancakes, we want 4
    print(make_n_pancakes(4, ingredients4))
