import threading

ACCOUNT_CLOSED_ERROR_MESSAGE = 'Account is closed'
ACCOUNT_OPENED_ERROR_MESSAGE = 'Acoount is opened'
AMOUNT_ERROR_MESSAGE = 'Amount is not valid'

class BankAccount:
    def __init__(self) -> None:
        self._open = False
        self._lock = threading.Lock()

    def get_balance(self) -> None:
        if self._open:
            return self._balance
        raise ValueError(ACCOUNT_CLOSED_ERROR_MESSAGE)

    def open(self) -> None:
        if self._open:
            raise ValueError(ACCOUNT_OPENED_ERROR_MESSAGE)
        self._open = True
        self._balance = 0

    def deposit(self, amount:int) -> None:
        with self._lock:
            if not (self._open):
                raise ValueError(ACCOUNT_CLOSED_ERROR_MESSAGE)
            if not (amount > 0):
                raise ValueError(AMOUNT_ERROR_MESSAGE)
            self._balance += amount

    def withdraw(self, amount:int) -> None:
        with self._lock:
            if not (self._open):
                raise ValueError(ACCOUNT_CLOSED_ERROR_MESSAGE)
            if not (amount > 0 and self._balance >= amount):
                raise ValueError(AMOUNT_ERROR_MESSAGE)
            self._balance -= amount

    def close(self) -> None:
        if not (self._open):
            raise ValueError(ACCOUNT_CLOSED_ERROR_MESSAGE)
        self._open = False
