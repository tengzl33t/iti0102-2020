"""Bank."""
import datetime
import random


class PersonError(Exception):
    """Person error."""

    pass


class TransactionError(Exception):
    """Transaction error."""

    pass


class Person:
    """Person class."""

    def __init__(self, fn: str, ln: str, ag: int):
        """Testeri lemmik asi."""
        self.first_name = fn
        self.last_name = ln
        if ag <= 0:  # If age is 0 or less
            raise PersonError
        self._age = ag
        self.bank_account = None

    @property
    def full_name(self) -> str:
        """Get person's full name. Combination of first and last name."""
        result = self.first_name + " " + self.last_name
        return result

    @property
    def age(self) -> int:
        """Get person's age."""
        return self._age

    @age.setter
    def age(self, value: int):
        """Set person's age. Must be greater than 0."""
        if value <= 0:
            raise PersonError
        self._age = value

    def __repr__(self) -> str:
        """Testeri lemmik asi."""
        return self.full_name


class Bank:
    """Bank class."""

    def __init__(self, nm: str):
        """Testeri lemmik asi."""
        self.name = nm
        self.customers = []
        self.transactions = []

    def add_customer(self, person: Person) -> bool:
        """Testeri lemmik asi."""
        if person not in self.customers:
            person.bank_account = Account(0, person, self)
            self.customers.append(person)
            return True
        else:
            return False

    def remove_customer(self, person: Person) -> bool:
        """Testeri lemmik asi."""
        if person in self.customers:
            person.bank_account = None
            self.customers.remove(person)
            return True
        else:
            return False

    def __repr__(self) -> str:
        """Testeri lemmik asi."""
        return self.name


class Transaction:
    """Transaction class."""

    def __init__(self, amnt: float, dt: datetime.date, sender: 'Account', receiver: 'Account', atm: bool):
        """Testeri lemmik asi."""
        self.amount = amnt
        self.date = dt
        self.sender_account = sender
        self.receiver_account = receiver
        self.is_from_atm = atm

    def __repr__(self) -> str:
        """Testeri lemmik asi."""
        if self.is_from_atm:
            return f"({self.amount} €) ATM"
        else:
            return f"({self.amount} €) {self.sender_account.person.full_name} -> {self.receiver_account.person.full_name}"


class Account:
    """Account class."""

    def __init__(self, blnc: float, prs: Person, bnk: 'Bank'):
        """Testeri lemmik asi."""
        self._balance = blnc
        self.person = prs
        self.bank = bnk
        self.transactions = []
        self.number = "EE" + str(random.randint(100000000000000000, 999999999999999999))

    @property
    def balance(self) -> float:
        """Get account's balance."""
        return self._balance

    def deposit(self, amount: float, is_from_atm: bool = True):
        """Deposit money to account."""
        if amount > 0:
            if is_from_atm:
                t = Transaction(amount, datetime.date.today(), self, self, is_from_atm)
                self.transactions.append(t)
                self.bank.transactions.append(t)
            self._balance += amount
        else:
            raise TransactionError

    def withdraw(self, amount: float, is_from_atm: bool = True):
        """Withdraw money from account."""
        if 0 < amount < self._balance:
            if is_from_atm:
                t = Transaction(-amount, datetime.date.today(), self, self, is_from_atm)
                self.transactions.append(t)
                self.bank.transactions.append(t)
            self._balance -= amount
        else:
            raise TransactionError

    def transfer(self, amount: float, receiver_account: 'Account'):
        """Transfer money from one account to another."""
        com = 5
        another_bank = True if self.bank != receiver_account.bank else False

        if amount > self._balance or (another_bank and amount > (self.balance + com)):
            raise TransactionError

        if self == receiver_account:  # Can't send money to same account
            raise TransactionError

        tr = Transaction(amount, datetime.date.today(), self, receiver_account, False)
        self.withdraw(amount, False)
        receiver_account.deposit(amount, False)

        if another_bank:
            self.withdraw(com, False)
            receiver_account.bank.transactions.append(tr)  # Add transaction to another bank

        self.transactions.append(tr)
        receiver_account.transactions.append(tr)

        self.bank.transactions.append(tr)

    def account_statement(self, from_date: datetime.date, to_date: datetime.date) -> list:
        """All transactions in given period."""
        res_list = []
        for tr in self.transactions:
            if from_date <= tr.date <= to_date:  # if date between
                res_list.append(tr)
        return res_list

    def get_debit_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """Get all debit (deposit/income)."""
        result = 0
        for tr in self.transactions:
            if from_date <= tr.date <= to_date and ((tr.is_from_atm or tr.receiver_account == self) and tr.amount > 0):
                result += tr.amount
        return result

    def get_credit_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """Get all credit (withdraw)."""
        result = 0
        for tr in self.transactions:
            if from_date <= tr.date <= to_date and (
                    (tr.is_from_atm and tr.amount < 0) or (tr.sender_account == self and not tr.is_from_atm)):
                result -= abs(tr.amount)  # remove minus from value
        return result

    def get_net_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """Get all debit/credit in time."""
        result = 0
        result += self.get_debit_turnover(from_date, to_date)
        result += self.get_credit_turnover(from_date, to_date)
        return result

    def __repr__(self) -> str:
        """Testeri lemmik asi."""
        return self.number
