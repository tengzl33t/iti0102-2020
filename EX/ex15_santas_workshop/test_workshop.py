"""Workshop tests."""
from workshop import Receiver, Workshop, Gift, Order

w = Workshop("ex15_wish_list.csv", "ex15_naughty_list.csv", "ex15_nice_list.csv")


def test_receiver_class():
    rec = Receiver("nigger", "africa")
    rec.set_total_weight(100.5445)
    w0 = ["rifle"]
    w1 = ["stolen tv"]
    w_test = ["rifle", "stolen tv"]
    rec.add_wish(w0)
    rec.add_wish(w1)
    assert rec.name == "nigger"
    assert rec.country == "africa"
    assert rec.wishes_total_weight == 100.5445
    assert rec.wishes == w_test


def test_order_class():
    o = Order("amerika")
    p = "test_parcel"
    p1 = "test_parcel2"
    p_test = [p, p1]
    o.set_parcels(p)
    o.set_parcels(p1)
    o.set_weight(191.554443)
    assert o.dest_country == "amerika"
    assert o.get_weight() == 191.55
    assert o.parcels == p_test


def test_gift_class():
    g = Gift("Swimming flippers")
    g.get_parameters()
    assert g.cost == 25
    assert g.prod_time == 3
    assert g.weight == 1


def test_workshop_read_file():
    result_list = w.read_file(w.nice_file)
    assert len(result_list) == 291
    assert result_list[0][0] == "Libby"
    assert result_list[0][1] == " United Kingdom"


def test_workshop_get_nice():
    result_list = w.get_nice()
    res = result_list[0]
    assert res.name == "Libby"


def test_workshop_get_wishes():
    result_dict = w.get_wishes()
    assert len(result_dict["Libby"]) == 3


def test_workshop_union():
    union_result = w.union()
    assert len(union_result[0].wishes) == 3


def test_workshop_country_sort():
    sort_result_dict = w.country_sort()
    assert len(sort_result_dict["United Kingdom"]) == 29
    assert len(sort_result_dict["Germany"]) == 21


def test_workshop_delivery():
    order_list = w.delivery()
    assert order_list[0].dest_country == "United Kingdom"
    assert order_list[0].get_weight() == 48.34

    assert order_list[1].dest_country == "United Kingdom"
    assert order_list[1].get_weight() == 30.62

    assert order_list[2].dest_country == "Germany"
    assert order_list[2].get_weight() == 35.93


def test_workshop_write_to_file():
    w.write_orders_to_file()
    read_file = "orders/United Kingdom/order0.txt"
    line_list = []
    with open(read_file, "r") as file:
        for line in file:
            line_list.append(line)

    assert line_list[0] == "                          DELIVERY ORDER                          " + "\n"
    assert line_list[10] == "FROM: NORTH POLE CHRISTMAS CHEER INCORPORATED" + "\n"
    assert line_list[11] == "TO: United Kingdom" + "\n"
    assert line_list[15] == "||  Name   ||                                       Gifts               " \
                            "                        || Total Weight(kg) ||" + "\n"
    assert line_list[17] == r"|| Libby   || Zebra Jumpy, Princess dress, Lego death star               " \
                            "                       ||             3.62 ||" + "\n"
    assert line_list[-1] == r"\\=========[]============================================================" \
                            "=======================[]==================//"


def test_post():
    test = "Greetings to the North Pole!\n\nI have been very nice to my family and friends, and even some people who have not been very nice to me, like our neighbor who yells at me when I play with the waterhose.\n\nThe following is my wishlist: Baby Yoda plushie, Anime krut o, Maxxamad.\n\nThanks, Santa,\nCasper, Puerto Rico"
    assert w.post(test) == test


def test_post_parameters():
    test = "Greetings to the North Pole!\n\nI have been very nice to my family and friends, and even some people who have not been very nice to me, like our neighbor who yells at me when I play with the waterhose.\n\nThe following is my wishlist: Baby Yoda plushie, Anime krut o, Maxxamad.\n\nThanks, Santa,\nCasper, Puerto Rico"
    assert w.get_post_parameters(test) == ['Baby Yoda plushie', 'Anime krut o', 'Maxxamad']
