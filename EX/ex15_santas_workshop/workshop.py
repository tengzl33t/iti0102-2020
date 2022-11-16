"""Workshop."""
import csv
import simplejson as json
import faster_than_requests as req  # from https://github.com/tengzl33t/faster-than-requests/releases
import pathlib
import re
import base64


class Receiver:
    """Receiver class."""

    def __init__(self, name, country):
        """Sample text."""
        self.name = name
        self.country = country
        self.wishes = []
        self.wishes_total_weight = 0

    def add_wish(self, wish):
        """Add wishes to receiver."""
        self.wishes += wish

    def set_total_weight(self, weight):
        """Set receivers wishes total weight."""
        self.wishes_total_weight = weight


class Order:
    """Order class."""

    def __init__(self, dest_country):
        """Sample text."""
        self.dest_country = dest_country
        self.parcels = []
        self.weight = 0

    def set_parcels(self, parcel):
        """Add parcels to order."""
        self.parcels.append(parcel)

    def set_weight(self, weight):
        """Add weight to order."""
        self.weight += weight

    def get_weight(self):
        """Get orders weight."""
        return round(self.weight, 2)


class Gift:
    """Gift class."""

    def __init__(self, name):
        """Sample text."""
        self.name = name
        self.cost = 0
        self.prod_time = 0
        self.weight = 0

    def get_parameters(self):
        """Get gift parameters (weight, prod. time, etc) from url."""
        name_encoded = req.urlencode(self.name)

        r = req.get2json(f"http://api.game-scheduler.com:8089/gift?name={name_encoded}")
        data_dict = json.loads(r)

        self.cost = data_dict["material_cost"]
        self.prod_time = data_dict["production_time"]
        self.weight = round(data_dict["weight_in_grams"] / 1000, 2)


class Workshop:
    """Workshop class."""

    def __init__(self, wish_file, naughty_file, nice_file):
        """Sample text."""
        self.wish_file = wish_file
        self.naughty_file = naughty_file
        self.nice_file = nice_file

    def read_file(self, filename):
        """Read workshop input files."""
        res_list = []
        with open(filename, encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                res_list.append(line)
        return res_list

    # def get_bad(self):
    #     """IDK does i need it."""
    #     res_dict = {}
    #     for line in self.read_file(self.naughty_file):
    #         res_dict[line[0]] = line[1].strip()
    #     return res_dict

    def get_nice(self):
        """Sample text."""
        res_list = []
        for line in self.read_file(self.nice_file):
            re = Receiver(line[0], line[1].strip())
            res_list.append(re)
        return res_list

    def get_wishes(self):
        """Sample text."""
        res_dict = {}
        for line in self.read_file(self.wish_file):
            wishes = [Gift(i.strip()) for i in line[1:]]
            for w in wishes:
                w.get_parameters()  # So slow...
            res_dict[line[0]] = wishes
        return res_dict

    def union(self):
        """Union nice and it's wishes."""
        nice = self.get_nice()
        wishes = self.get_wishes()
        for n in nice:
            for k, v in wishes.items():
                if k == n.name:
                    n.add_wish(v)
            n.set_total_weight(round(sum([v.weight for v in n.wishes]), 2))
        return nice

    def country_sort(self):
        """Sort parcels by country and return dict."""
        un = self.union()
        country_sort_dict = {}
        for i in un:
            if i.country in country_sort_dict:
                country_sort_dict[i.country].append(i)
            else:
                country_sort_dict.setdefault(i.country, []).append(i)  # if key not found insert key with list
        return country_sort_dict

    def delivery(self):
        """Make delivery orders."""
        c_sort = self.country_sort()
        order_list = []
        for k, v in c_sort.items():
            o = Order(k)
            for i in v:
                # if not last element and has free space in order.
                if o.get_weight() + i.wishes_total_weight <= 50.0000 and i != v[-1]:
                    o.set_weight(i.wishes_total_weight)
                    o.set_parcels(i)
                # if last element and has free space in order.
                elif o.get_weight() + i.wishes_total_weight <= 50.0000 and i == v[-1]:
                    o.set_weight(i.wishes_total_weight)
                    o.set_parcels(i)
                    order_list.append(o)
                # if not last and don't have free space -> append previous order and make new
                elif i != v[-1]:
                    order_list.append(o)
                    o = Order(k)
                    o.set_weight(i.wishes_total_weight)
                    o.set_parcels(i)
                # if not last and don't have free space -> append previous order, make new and append it
                elif i == v[-1]:
                    order_list.append(o)
                    o = Order(k)
                    o.set_weight(i.wishes_total_weight)
                    o.set_parcels(i)
                    order_list.append(o)
        return order_list

    def write_orders_to_file(self):
        """Write orders to files."""
        orders = self.delivery()

        for i in orders:

            # Get max lengths of names and wishes
            names_max = max([len(v.name) for v in i.parcels])

            wishes_max_list = []
            for p in i.parcels:
                w = len(', '.join([v.name for v in p.wishes]))
                wishes_max_list.append(w)

            wishes_max = max(wishes_max_list)

            # Create directory with parents
            pathlib.Path(f"orders/{i.dest_country}").mkdir(parents=True, exist_ok=True)

            write_file = f"orders/{i.dest_country}/order{orders.index(i)}.txt"

            h_dict = {"Name": names_max, "Gifts": wishes_max, "Total Weight(kg)": 18}  # header data

            h = '{:{align}{width}}'.format("DELIVERY ORDER", align='^', width=66) + "\n\n"
            h += " " * 58 + "_v\n"
            h += " " * 53 + "__* (__)\n"
            h += " " * 13 + "ff     ff     ff     ff" + " " * 16 + r"{\/ (_(__).-." + "\n"
            h += r"      ff    <_\__, <_\__, <_\__, <_\__,      __,~~.(`>|-(___)/ ,_)" + "\n"
            h += r'    o<_\__,  (_ ff ~(_ ff ~(_ ff ~(_ ff~~~~~@ )\/_;-"``     |' + "\n"
            h += r'      (___)~~//<_\__, <_\__, <_\__, <_\__,    | \__________/|' + "\n"
            h += r'      // >>     (___)~~(___)~~(___)~~(___)~~~~\\_/_______\_//' + "\n"
            h += r"                // >>  // >>  // >>  // >>     `'---------'` " + "\n"
            h += "FROM: NORTH POLE CHRISTMAS CHEER INCORPORATED\n"
            h += f"TO: {i.dest_country}\n"
            h += f"TOTAL WEIGHT: {i.get_weight()}\n\n"

            h += "//" + "=" * (h_dict["Name"] + 2) + "[]" + "=" * (h_dict["Gifts"] + 2) + "[]" \
                 + "=" * 18 + r"\\" + "\n"

            for k, v in h_dict.items():
                if k == "Total Weight(kg)":
                    h += "||" + '{:{align}{width}}'.format(k, align='^', width=v) + "||\n"
                else:
                    h += "||" + ' {:{align}{width}} '.format(k, align='^', width=v)

            h += "|]" + "=" * (h_dict["Name"] + 2) + "[]" + "=" * (h_dict["Gifts"] + 2) + "[]" + "=" * 18 + "[|"

            with open(write_file, "w+") as file:
                file.write(h)
                for p in i.parcels:
                    data = "\n"
                    data += "||" + ' {:{align}{width}} '.format(p.name, align='<', width=h_dict["Name"])
                    data += "||" + ' {:{align}{width}} '.format(", ".join([v.name for v in p.wishes]),
                                                                align='<', width=h_dict["Gifts"])
                    data += "||" + ' {:{align}{width}} '.format(p.wishes_total_weight, align='>', width=16) + "||"
                    file.write(data)

                file.write("\n")
                file.write(r"\\" + "=" * (h_dict["Name"] + 2) + "[]" + "=" * (h_dict["Gifts"] + 2)
                           + "[]" + "=" * 18 + "//")

    def post(self, test):
        """Postal services."""
        if not test:
            r = req.get2json("http://api.game-scheduler.com:8089/letter")
            data_dict = json.loads(r)
            letter = str(data_dict["letter"])
        else:
            letter = test

        check1_words = ["Dear", "Santa", "Hello", "Hi", "Thanks", "Thank you", "Sincerely", "thankful", "Greetings"]
        check1 = any([bool(re.search(w, letter)) for w in check1_words])

        if check1 is True:  # First check for normal letter.
            return letter
        elif check1 is False and "\n" not in letter:  # if base64
            return base64.b64decode(letter).decode("UTF-8")
        elif check1 is False and "\n" in letter:
            letters = ""
            for i in letter:
                if i.isalpha():
                    letters += chr((ord(i) - 4 - 97) % 26 + 97)
                else:
                    letters += i
            return letters

    def get_post_parameters(self, test):
        """Get wishes from post messages."""
        post_msg = self.post(test)
        # print(post_msg)
        check_list = ["for", "wishlist:", "want"]

        # check if message contains wishes
        if any([bool(re.search(w, post_msg)) for w in check_list]) is False:
            return "No gifts found"

        wishes_start = 0
        wishes_end = 0

        words = [i for i in post_msg.split()]

        # find wishes
        for i, l in enumerate(post_msg.split()):
            if l in check_list:
                wishes_start = i + 1
            # find end of wishes list
            if l[-1] == ".":
                wishes_end = i + 1

        # make str from list by join
        # delete dot from last element
        # make list from string by split
        res = ' '.join([str(i) for i in words[wishes_start:wishes_end]]).strip(".").split(", ")
        return res

#intellij to git test line
