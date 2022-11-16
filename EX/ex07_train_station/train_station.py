"""Train Station."""


class Passenger:
    """Automaattesteri lemmik asi."""

    def __init__(self, passenger_id: str, seat: str):
        """Automaattesteri lemmik asi."""
        self._passenger_id = passenger_id
        self._seat = seat

    @property
    def passenger_id(self) -> str:
        """Automaattesteri lemmik asi."""
        return self._passenger_id

    @property
    def seat(self) -> str:
        """Automaattesteri lemmik asi."""
        return self._seat


class Train:
    """Automaattesteri lemmik asi."""

    def __init__(self, train_id: str, carriages: int, seats_in_carriage: int):
        """Automaattesteri lemmik asi."""
        self._train_id = train_id
        self._carriages = carriages
        self._seats_in_carriage = seats_in_carriage
        self._passengers = []
        pass

    @property
    def carriages(self) -> int:
        """Automaattesteri lemmik asi."""
        return self._carriages

    @property
    def train_id(self) -> str:
        """Automaattesteri lemmik asi."""
        return self._train_id

    @property
    def seats_in_carriage(self) -> int:
        """Automaattesteri lemmik asi."""
        return self._seats_in_carriage

    @property
    def passengers(self) -> list:
        """Automaattesteri lemmik asi."""
        return self._passengers

    def get_seats_in_train(self) -> int:
        """Automaattesteri lemmik asi."""
        return self._seats_in_carriage * self._carriages

    def get_number_of_passengers(self) -> int:
        """Automaattesteri lemmik asi."""
        return len(self._passengers)  # passengers is list, so can use len()

    def get_passengers_in_carriages(self) -> dict:
        """Automaattesteri lemmik asi."""
        res_dict = {}
        for c in range(
            self._carriages
        ):  # range method get from 1 (we don't need here 0, because can't be zero carriage)
            res_dict[str(c + 1)] = []  # here we make dict key with empty list
        for passenger in self._passengers:
            wag_num = passenger.seat.split("-")[1]
            res_dict[wag_num].append(
                passenger
            )  # place passenger into list in dict which made earlier (key is carriage number)
        return res_dict

    @train_id.setter
    def train_id(self, value: str):
        """Automaattesteri lemmik asi."""
        self._train_id = value
        pass

    @carriages.setter
    def carriages(self, value: int):
        """Automaattesteri lemmik asi."""
        self._carriages = value
        pass

    @seats_in_carriage.setter
    def seats_in_carriage(self, value: int):
        """Automaattesteri lemmik asi."""
        self._seats_in_carriage = value

    pass

    def add_passenger(self, passenger: Passenger) -> Passenger:
        """Automaattesteri lemmik asi."""
        splitter = passenger.seat.split(
            "-"
        )  # take all data (train id, carriage, seat number from passenger data)
        tr_id = splitter[0]
        wag_num = int(splitter[1])
        seat_num = int(splitter[2])
        res = None  # if "if" requirements is false return None into Passenger
        if (
            tr_id == self._train_id
            and wag_num > 0
            and wag_num <= self._carriages
            and seat_num > 0
            and seat_num <= self._seats_in_carriage
        ):
            for p in self._passengers:
                if passenger.seat == p.seat:
                    return res
            res = passenger
            self._passengers.append(passenger)
        return res


class TrainStation:
    """Automaattesteri lemmik asi."""

    def __init__(self, trains: list, passengers: list):
        """Automaattesteri lemmik asi."""
        self._passengers = passengers
        self._trains = trains
        self.pass_trains()  # it's not good to place to much data into init, so...
        pass

    def get_station_overview(self) -> list:
        """Automaattesteri lemmik asi."""
        res_list = []
        for t in self._trains:
            res_seats = (
                str(t.get_number_of_passengers()) + "/" + str(t.get_seats_in_train())
            )  # kinni/kokku seats
            res_list.append(
                {"train_id": t.train_id, "carriages": t.carriages, "seats": res_seats}
            )
        return res_list

    def get_number_of_passengers(self):
        """Automaattesteri lemmik asi."""
        return len(self._passengers)

    def pass_trains(self):
        """Automaattesteri lemmik asi."""
        saved_pass = []  # make second list
        saved_pass.extend(self._passengers)
        """
        Copy data from main to second list, because we will need to work with list and we don't need to change main list before end.
        Changing of main list can cause problems and incorrect output.
        """
        for passenger in self._passengers:
            splitter = passenger.seat.split("-")
            tr_id = splitter[0]
            p = None  # if "if" requirements is false return None into passengers
            for t in self._trains:
                if t.train_id == tr_id:
                    p = t.add_passenger(passenger)
            if p is None:  # can cause problems if in for cycle, so outside of cycle
                saved_pass.remove(passenger)
        self._passengers = saved_pass  # update main with data from second

    @property
    def passengers(self):
        """Automaattesteri lemmik asi."""
        return self._passengers

    @passengers.setter
    def passengers(self, value_list: list):
        """Automaattesteri lemmik asi."""
        self._passengers = value_list

    @property
    def trains(self):
        """Automaattesteri lemmik asi."""
        return self._trains

    @trains.setter
    def trains(self, value_list: list):
        """Automaattesteri lemmik asi."""
        self._trains = value_list
