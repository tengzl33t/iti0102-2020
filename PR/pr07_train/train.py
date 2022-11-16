"""Train."""


class Train:
    """See, mida tester tahab."""

    def __init__(self, passengers: list, carriages: int, seats_in_carriage: int):
        """See, mida tester tahab."""
        self._passengers = []
        for passenger in passengers:
            pass
        self.carriages = carriages
        self.seats_in_carriage = seats_in_carriage
        self.passengers = passengers

    @property
    def passengers(self) -> list:
        """See, mida tester tahab."""
        return self._passengers

    @property
    def carriages(self) -> int:
        """See, mida tester tahab."""
        return self._carriages

    @property
    def seats_in_carriage(self) -> int:
        """See, mida tester tahab."""
        return self._seats_in_carriage

    def get_seats_in_train(self) -> int:
        """See, mida tester tahab."""
        return self.seats_in_carriage * self.carriages

    def get_number_of_passengers(self) -> int:
        """See, mida tester tahab."""
        result = 0
        for passenger in self.passengers:
            result += 1

        return result

    def get_passengers_in_carriages(self) -> dict:
        """See, mida tester tahab."""
        res_dict = {}
        counter = 1
        while counter <= self.carriages:
            res_dict[str(counter)] = []
            counter += 1

        for passenger in self.passengers:
            in_dict = passenger.__dict__()
            in_dict.update({"seat": passenger.seat_num})
            res_dict[passenger.carr_num].append(in_dict)
        return res_dict

    @passengers.setter
    def passengers(self, value_list: list):
        """See, mida tester tahab."""
        for passenger in value_list:
            if (
                (int(passenger.carr_num) <= self.carriages)
                and (int(passenger.carr_num) > 0)
                and (int(passenger.seat_num) <= self.seats_in_carriage)
                and (int(passenger.seat_num) > 0)
            ):
                self._passengers.append(passenger)
        pass

    @carriages.setter
    def carriages(self, value: int):
        """See, mida tester tahab."""
        self._carriages = value
        pass

    @seats_in_carriage.setter
    def seats_in_carriage(self, value: int):
        """See, mida tester tahab."""
        self._seats_in_carriage = value
        pass


class Passenger:
    """See, mida tester tahab."""

    def __init__(self, passenger_id: str, seat: str):
        """See, mida tester tahab."""
        self.passenger_id = passenger_id
        self.seat = seat
        self.carr_num = str(self.seat.split("-")[0])
        self.seat_num = str(self.seat.split("-")[1])

    def __dict__(self):
        """See, mida tester tahab."""
        res_list = {}
        res_list["id"] = self.passenger_id
        res_list["seat"] = self.seat
        return res_list
