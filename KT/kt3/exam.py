"""KT3."""


def only_one_pair(numbers: list) -> bool:
    """See wtf."""
    res_list = []
    for i in numbers:
        res_list.append(numbers.count(i))
    if len(res_list) > 0:
        maxvalue = max(res_list)
        if maxvalue > 1 and maxvalue == 2 and res_list.count(maxvalue) <= 2:
            return True
        else:
            return False
    else:
        return False


class Account:
    """Represent a bank account."""

    def __init__(self, name, balance):
        """See wtf."""
        self._name = name
        self._balance = balance

        pass

    def get_balance(self):
        """See wtf."""
        return self._balance

    def get_name(self):
        """See wtf."""
        return self._name.upper()

    def withdraw(self, amount):
        """See wtf."""
        if amount > 0 and self._balance > 0:
            if amount > self._balance:
                if self._balance != 0:
                    wasmoney = self._balance
                    self._balance = 0
                    return f"Amount withdrawn: {wasmoney}"
            else:
                if self._balance != 0:
                    self._balance -= amount
                    return f"Amount withdrawn: {amount}"
        else:
            if amount == 0:
                return "Amount withdrawn: 0"
            else:
                return None

    def deposit(self, amount):
        """See wtf."""
        if amount > 0:
            self._balance += amount
            return f"Amount deposited: {amount}"
        else:
            return "Amount deposited: 0"
