"""Test for formula_one.py."""
import csv
from formula_one import Driver, Race, FormulaOne


# Driver tests

def test_get_results():
    """Test for formula_one.py."""
    d = Driver("Debilich", "Dream Team")
    d.add_result(1, 15)
    assert d.get_results() == {1: 15}
    # d1.set_points()


def test_get_points():
    """Test for formula_one.py."""
    d = Driver("Debilich", "Dream Team")
    d.add_result(1, 15)
    d.set_points()
    assert d.get_points() == 15


def test_set_points():
    """Test for formula_one.py."""
    # testing in get_results
    pass


def test_add_result():
    """Test for formula_one.py."""
    # testing in get_points
    pass


# Race tests

def test_read_file_to_list():
    """Test for formula_one.py."""
    r = Race("ex08_example_data.txt")
    r.read_file_to_list()
    needtobe = "Mika Hakkinen  Mclaren-Mercedes   79694  1"
    assert r._file_data[0] == needtobe


def test_extract_info():
    """Test for formula_one.py."""
    line1 = "Mika Hakkinen  Mclaren-Mercedes   79694  1"
    dict1 = {'Name': 'Mika Hakkinen', 'Team': 'Mclaren-Mercedes',
             'Time': 79694, 'Diff': '', 'Race': 1}
    assert Race.extract_info(line1) == dict1


def test_filter_data_by_race():
    """Test for formula_one.py."""
    r = Race("ex08_example_data.txt")
    dict1 = {'Name': 'David Coulthard', 'Team': 'Mclaren-Mercedes', 'Time': 77522, 'Diff': '', 'Race': 2}
    data1 = r.filter_data_by_race(2)[1]
    assert data1 == dict1


def test_format_time():
    """Test for formula_one.py."""
    assert Race.format_time(123456) == "2:03.456"
    assert Race.format_time(456) == "0:00.456"


def test_calculate_time_difference():
    """Test for formula_one.py."""
    assert Race.calculate_time_difference(50, 100) == "+0:00.050"
    assert Race.calculate_time_difference(77522, 79061) == "+0:01.539"


def test_sort_data_by_time():
    """Test for formula_one.py."""
    testlist = [{'Name': 'David Coulthard', 'Team': 'Mclaren-Mercedes', 'Time': 77522, 'Diff': '', 'Race': 2},
                {'Name': 'Heinz-Harald Frentzen', 'Team': 'Jordan-Mugen-Honda', 'Time': 81516, 'Diff': '', 'Race': 2},
                {'Name': 'Jacques Villeneuve', 'Team': 'BAR-Honda', 'Time': 84254, 'Diff': '', 'Race': 2},
                {'Name': 'Jenson Button', 'Team': 'Williams-BMW', 'Time': 79459, 'Diff': '', 'Race': 2}]

    reslist = [{'Name': 'David Coulthard', 'Team': 'Mclaren-Mercedes', 'Time': 77522, 'Diff': '', 'Race': 2},
               {'Name': 'Jenson Button', 'Team': 'Williams-BMW', 'Time': 79459, 'Diff': '', 'Race': 2},
               {'Name': 'Heinz-Harald Frentzen', 'Team': 'Jordan-Mugen-Honda', 'Time': 81516, 'Diff': '', 'Race': 2},
               {'Name': 'Jacques Villeneuve', 'Team': 'BAR-Honda', 'Time': 84254, 'Diff': '', 'Race': 2}]
    assert Race.sort_data_by_time(testlist) == reslist


def test_get_results_by_race():
    """Test for formula_one.py."""
    r = Race("ex08_example_data.txt")
    res1 = {'Name': 'David Coulthard', 'Team': 'Mclaren-Mercedes', 'Time': '1:17.522', 'Diff': '',
            'Race': 2, 'Place': 1, 'Points': 25}
    res2 = {'Name': 'kkkj gf', 'Team': 'Sauber-Petronas', 'Time': '15:56.565', 'Diff': '+14:38.959',
            'Race': 1, 'Place': 12, 'Points': 0}
    assert r.get_results_by_race(2)[0] == res1
    assert r.get_results_by_race(1)[-1] == res2


# Formula One tests

def test_write_race_results_to_file():
    """Test for formula_one.py."""
    resline0 = "PLACE     NAME                     TEAM                     TIME           DIFF           POINTS\n"
    resline1 = "------------------------------------------------------------------------------------------------\n"
    resline2 = "1         David Coulthard          Mclaren-Mercedes         1:17.522                      25    \n"
    resline5 = "4         Jenson Button            Williams-BMW             1:19.459       +0:01.937      12    \n"

    f1 = FormulaOne("ex08_example_data.txt")
    f1.write_race_results_to_file(2)
    res_file = "results_for_race_2.txt"
    reslist = []
    with open(res_file, encoding="utf-8") as file:
        for line in file:
            reslist.append(line)

    assert reslist[0] == resline0
    assert reslist[1] == resline1
    assert reslist[2] == resline2
    assert reslist[5] == resline5


def test_write_race_results_to_csv():
    """Test for formula_one.py."""
    resline0 = ['Place', 'Name', 'Team', 'Time', 'Diff', 'Points', 'Race']
    resline1 = ['1', 'David Coulthard', 'Mclaren-Mercedes', '1:17.522', '', '25', '2']
    resline2 = ['2', 'hhh Hakfgfgytginen', 'Mclaren-Mercedes', '1:17.522', '+0:00.000', '18', '2']
    resline5 = ['5', 'Heinz-Harald Frentzen', 'Jordan-Mugen-Honda', '1:21.516', '+0:03.994', '10', '2']

    f1 = FormulaOne("ex08_example_data.txt")
    f1.write_race_results_to_csv(2)
    res_file = "race_2_results.csv"
    reslist = []
    with open(res_file, encoding="utf-8") as file:
        reader = csv.reader(file)
        for line in reader:
            reslist.append(line)

    assert reslist[0] == resline0
    assert reslist[1] == resline1
    assert reslist[2] == resline2
    assert reslist[5] == resline5


def test_write_championship_to_file():
    """Test for formula_one.py."""
    # incorrect reslines, because i don't know which output must be.
    resline0 = "PLACE     NAME                     TEAM                     POINTS\n"
    resline1 = "------------------------------------------------------------------\n"
    resline2 = "1         David Coulthard          Mclaren-Mercedes         25    \n"
    resline5 = "4         Jenson Button            Williams-BMW             12    \n"

    f1 = FormulaOne("ex08_example_data.txt")
    f1.write_championship_to_file()
    res_file = "championship_results.txt"
    reslist = []
    with open(res_file, encoding="utf-8") as file:
        for line in file:
            reslist.append(line)

    # dont have this function in formula_one.py
    assert reslist[0] == resline0
    assert reslist[1] == resline1
    assert reslist[2] == resline2
    assert reslist[5] == resline5
