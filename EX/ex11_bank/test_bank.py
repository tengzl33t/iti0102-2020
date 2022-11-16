"""Test for bank.py."""
import datetime
from bank import Person, Bank


def test_full_name():
    """For the tester."""
    person = Person("Vladimir", "Lenin", 100)
    result = "Vladimir Lenin"
    assert result == str(person)
    assert result == person.full_name


def test_age():
    """For the tester."""
    person = Person("Vladimir", "Lenin", 100)
    result = 100
    assert result == person.age


def test_add_customer():
    """For the tester."""
    person = Person("Vladimir", "Lenin", 100)
    bank = Bank("Soviet Bank")
    bank.add_customer(person)
    assert len(person.bank_account.number) == 20


def test_remove_customer():
    """For the tester."""
    person = Person("Vladimir", "Lenin", 100)
    bank = Bank("Soviet Bank")
    bank.add_customer(person)
    bank.remove_customer(person)
    assert person.bank_account is None


def test_balance():
    """For the tester."""
    person = Person("Vladimir", "Lenin", 100)
    bank = Bank("Soviet Bank")
    bank.add_customer(person)
    a = person.bank_account
    assert a.balance == 0


def test_deposit():
    """For the tester."""
    person = Person("Vladimir", "Lenin", 100)
    bank = Bank("Soviet Bank")
    bank.add_customer(person)
    a = person.bank_account
    a.deposit(100)
    assert a.balance == 100


def test_withdraw():
    """For the tester."""
    person = Person("Vladimir", "Lenin", 100)
    bank = Bank("Soviet Bank")
    bank.add_customer(person)
    a = person.bank_account
    a.deposit(100)
    a.withdraw(10)
    assert a.balance == 90


def test_transfer():
    """For the tester."""
    bank = Bank("Soviet Bank")

    person = Person("Vladimir", "Lenin", 100)
    bank.add_customer(person)
    a = person.bank_account
    a.deposit(100)

    person1 = Person("Lev", "Trockiy", 89)
    bank.add_customer(person1)
    a1 = person1.bank_account

    a.transfer(10, a1)

    tr = a.transactions
    tr1 = a1.transactions

    assert a.balance == 90
    assert a1.balance == 10
    assert tr[0].amount == 100
    assert tr1[0].amount == 10
    assert str(tr) == "[(100 €) ATM, (10 €) Vladimir Lenin -> Lev Trockiy]"


def test_account_statement():
    """For the tester."""
    d = datetime.date.today()

    person = Person("Vladimir", "Lenin", 100)
    bank = Bank("Soviet Bank")
    bank.add_customer(person)
    a = person.bank_account
    a.deposit(500)
    a.withdraw(100)

    person1 = Person("Lev", "Trockiy", 89)
    bank.add_customer(person1)
    a1 = person1.bank_account

    a.transfer(10, a1)

    result = "[(500 €) ATM, (-100 €) ATM, (10 €) Vladimir Lenin -> Lev Trockiy]"
    result1 = "(500 €) ATM"

    assert str(a.account_statement(d, d)) == result
    assert str(a.account_statement(d, d)[0]) == result1


def test_get_debit_turnover():
    """For the tester."""
    d = datetime.date.today()

    person = Person("Vladimir", "Lenin", 100)
    bank = Bank("Soviet Bank")
    bank.add_customer(person)
    a = person.bank_account
    a.deposit(500)
    a.withdraw(100)

    person1 = Person("Lev", "Trockiy", 89)
    bank.add_customer(person1)
    a1 = person1.bank_account
    a1.deposit(50)
    a.transfer(10, a1)
    a1.transfer(22, a)

    assert a.get_debit_turnover(d, d) == 522
    assert a1.get_debit_turnover(d, d) == 60


def test_get_credit_turnover():
    """For the tester."""
    d = datetime.date.today()

    person = Person("Vladimir", "Lenin", 100)
    bank = Bank("Soviet Bank")
    bank.add_customer(person)
    a = person.bank_account
    a.deposit(500)
    a.withdraw(100)

    person1 = Person("Lev", "Trockiy", 89)
    bank.add_customer(person1)
    a1 = person1.bank_account
    a1.deposit(50)
    a.transfer(10, a1)
    a1.transfer(22, a)

    assert a.get_credit_turnover(d, d) == -110
    assert a1.get_credit_turnover(d, d) == -22


def test_get_net_turnover():
    """For the tester."""
    d = datetime.date.today()

    person = Person("Vladimir", "Lenin", 100)
    bank = Bank("Soviet Bank")
    bank.add_customer(person)
    a = person.bank_account
    a.deposit(500)
    a.withdraw(100)

    person1 = Person("Lev", "Trockiy", 89)
    bank.add_customer(person1)
    a1 = person1.bank_account
    a1.deposit(50)
    a.transfer(10, a1)
    a1.transfer(22, a)

    assert a.get_net_turnover(d, d) == 412
    assert a1.get_net_turnover(d, d) == 38
