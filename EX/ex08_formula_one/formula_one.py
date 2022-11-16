"""Formula One."""
import re
import csv
import os


class Driver:
    """Driver class."""

    def __init__(self, name: str, team: str):
        """Sample text."""
        self._name = name
        self._team = team
        self._points = 0
        self._results = {}

        pass

    def get_results(self) -> dict:
        """Sample text."""
        return self._results

    def get_points(self) -> int:
        """Sample text."""
        self.set_points()

        return int(self._points)

    def set_points(self):
        """Sample text."""
        self._points = 0
        for i in self._results.values():
            self._points += i
        pass

    def add_result(self, race_number: int, points: int):
        """Sample text."""
        self._results[race_number] = points

        pass


class Race:
    """Race class."""

    def __init__(self, file):
        """Sample text."""
        self._file = file
        self._file_data = []
        self.read_file_to_list()  # need to fill "_file_data" list with data
        if os.path.exists(self._file):
            self._rcount = self._file_data.pop(0)
            # delete first line in data (count of races), and return it into "_rcount"

        pass

    @property
    def rcount(self):
        """Sample text."""
        return int(self._rcount)  # not used, maybe need for write_championship_to_file

    def read_file_to_list(self):
        """Sample text."""
        if os.path.exists(self._file):  # if file found
            with open(self._file, encoding="utf-8") as file:
                for line in file:
                    self._file_data.append(line.rstrip())  # remove spaces in the end
                    pass
        else:
            raise FileNotFoundError("No file found!")  # if not found give raise...

    @staticmethod
    def extract_info(line: str) -> dict:
        """Sample text."""
        out_dict = {}
        res = re.split(r"\s\s+", line)  # regex? Add spaces?
        if len(res) > 1:
            out_dict["Name"] = str(res[0])
            out_dict["Team"] = str(res[1])
            out_dict["Time"] = int(res[2])
            out_dict["Diff"] = ""
            out_dict["Race"] = int(res[3])

        return out_dict

    def filter_data_by_race(self, race_number: int) -> list:
        """Sample text."""
        res_list = []
        file_list = []
        for i in self._file_data:
            file_list.append(self.extract_info(i))

        for i in file_list:
            if int(i.get("Race")) == race_number:  # filter by race number
                res_list.append(i)

        return res_list

    @staticmethod
    def format_time(time: str) -> str:
        """Sample text."""
        millis = int(time)

        seconds = (millis / 1000) % 60
        seconds = int(seconds)

        minutes = (millis / (1000 * 60)) % 60
        minutes = int(minutes)

        millis = str(millis)[-3:]

        res = "{0}:{1}.{2}".format(str(minutes).zfill(1), str(seconds).zfill(2), millis.zfill(3))
        # zfill add whitespaces to required length of string

        return res

    @staticmethod
    def calculate_time_difference(first_time: int, second_time: int) -> str:
        """Sample text."""
        res = "+" + Race.format_time(int(second_time) - int(first_time))

        return res

    @staticmethod
    def sort_data_by_time(results: list) -> list:
        """Sample text."""
        res = sorted(results, key=lambda x: int(x["Time"]))

        return res

    def get_results_by_race(self, race_number: int) -> list:
        """Sample text."""
        points = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]  # if place lower than 10 so 0 points.
        data_list = Race.sort_data_by_time(self.filter_data_by_race(race_number))

        fp_time = data_list[0]["Time"]  # get best time
        place_counter = 1

        for d in data_list:
            if place_counter != 1:  # for first place don't need to add diff
                d["Diff"] = self.calculate_time_difference(fp_time, d["Time"])
            else:
                d["Diff"] = ""
            d["Place"] = place_counter
            d["Points"] = points[place_counter - 1] if place_counter <= 10 else 0  # if place > 10 give 0 points
            d["Time"] = self.format_time(d.get("Time"))  # do format for time and overwrite it
            place_counter += 1

        return data_list

    def get_results(self):
        """Sample text."""
        return self._file_data  # not used, maybe need for write_championship_to_file


class FormulaOne:
    """FormulaOne class."""

    def __init__(self, file):
        """Sample text."""
        self._file = file
        self._race = Race(file)

        pass

    def write_race_results_to_file(self, race_number: int):
        """Sample text."""
        write_file = f"results_for_race_{race_number}.txt"
        h_dict = {"PLACE": 10, "NAME": 25, "TEAM": 25, "TIME": 15, "DIFF": 15, "POINTS": 6}  # header data

        h = ""
        for k, v in h_dict.items():
            h += ("{:%d}" % v).format(k)
        h += "\n"
        h += "-" * 96  # add "---" line

        listdict = self._race.get_results_by_race(race_number)

        with open(write_file, "w") as file:
            file.write(h)

            for d in listdict:
                data = "\n"
                for k, v in h_dict.items():
                    data += ("{:<%d}" % v).format(d[k.title()])  # format for add whitespaces and/or align
                file.write("".join(data))
            file.write("\n")

        pass

    def write_race_results_to_csv(self, race_number: int):
        """Sample text."""
        write_file = f"race_{race_number}_results.csv"
        h = ["Place", "Name", "Team", "Time", "Diff", "Points", "Race"]

        with open(write_file, "w", newline='') as file:
            writer = csv.writer(file, delimiter=",")

            writer.writerow(h)
            listdict = self._race.get_results_by_race(race_number)
            for d in listdict:
                res = [d["Place"], d["Name"], d["Team"], d["Time"], d["Diff"], d["Points"], d["Race"]]
                writer.writerow(res)

        pass

    def write_championship_to_file(self):
        """Sample text."""
        pass
