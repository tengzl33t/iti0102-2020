"""Sample text."""


def encode(message: str, key: int) -> str:
    """Sample text."""
    result = ""
    for letter in range(len(message)):  # võtame kõik tähed.
        char = message[letter]
        number = (ord(char) + key - 97) % 26 + 97  # teeme tähe asemel number ascii/unicode tabeliga, number saame edasi muutma "key"ga.
        if char.isalpha() is True:  # vaatame kas täht on täht, mitte number, space või teine asi.
            chr_number = chr(number)  # kui JAH sis teeme unicode/ascii numbrist täht.
        else:
            chr_number = char  # kui EI siis anname tagasi ilma muutuseta.
        result += chr_number  # sumeerime kõik tähed, numbrid jne
    return result  # anname välja funktsiooni tulemust


print(encode("i like turtles", 6))
print(encode("hmm... wh4t, oh what?!?‽", 4))
print(encode("rendime saarele sauna", 100))
