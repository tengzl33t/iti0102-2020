"""Secret Garden."""
import base64


class Decoder:
    """Decoder class."""

    def __init__(self, file: str, key: str):
        """UwU."""
        self.file = file
        self.key = key

        pass

    def read_code_from_file(self) -> list:
        """UwU."""
        file_list = []
        with open(self.file, encoding="utf-8") as file:
            for line in file:
                file_list.append(line.strip())

        return file_list

    @staticmethod
    def decode_from_base64(data: str) -> str:
        """UwU."""
        result = base64.b64decode(data).decode("UTF-8")

        return result

    def calculate_cipher_step(self) -> int:
        """UwU."""
        result = 0
        for i in self.key:
            result += ord(i)
        return result

    def decode(self) -> list:
        """UwU."""
        res_list = []

        for i in self.read_code_from_file():
            dec_letters = ""

            for x in self.decode_from_base64(i):
                dec_letters += chr((ord(x) - self.calculate_cipher_step()) % 255)

            res_list.append(dec_letters)

        return res_list


class SecretGarden:
    """UwU."""

    def __init__(self, file: str, key: str):
        """UwU."""
        self.file = file
        self.key = key
        pass

    def decode_messages(self) -> list:
        """UwU."""
        return Decoder(self.file, self.key).decode()

    def find_secret_locations(self) -> list:
        """UwU."""
        res_list = []
        for i in self.decode_messages():
            splitted = i.split("\n")

            coord = splitted[0].split(";")
            direction = splitted[2]

            EW = int(coord[0])
            NS = int(coord[1])

            for x in direction:
                if x == "E":
                    EW += 1
                elif x == "W":
                    EW -= 1
                elif x == "N":
                    NS += 1
                elif x == "S":
                    NS -= 1
            res_list.append((EW, NS))

        return res_list
