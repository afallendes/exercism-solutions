import threading

ACCOUNT_CLOSED_ERROR_MESSAGE = 'Account is closed'
ACCOUNT_OPENED_ERROR_MESSAGE = 'Acoount is opened'
AMOUNT_ERROR_MESSAGE = 'Amount is not valid'

class BankAccount:
    def __init__(self) -> None:
        self.__open = False
        self.__lock = threading.Lock()

    def get_balance(self) -> None:
        if self.__open:
            return self.__balance
        raise ValueError(ACCOUNT_CLOSED_ERROR_MESSAGE)

    def open(self) -> None:
        if self.__open:
            raise ValueError(ACCOUNT_OPENED_ERROR_MESSAGE)
        self.__open = True
        self.__balance = 0

    def deposit(self, amount:int) -> None:
        with self.__lock:
            if not (self.__open):
                raise ValueError(ACCOUNT_CLOSED_ERROR_MESSAGE)
            if not (amount > 0):
                raise ValueError(AMOUNT_ERROR_MESSAGE)
            self.__balance += amount

    def withdraw(self, amount:int) -> None:
        with self.__lock:
            if not (self.__open):
                raise ValueError(ACCOUNT_CLOSED_ERROR_MESSAGE)
            if not (amount > 0 and self.__balance >= amount):
                raise ValueError(AMOUNT_ERROR_MESSAGE)
            self.__balance -= amount

    def close(self) -> None:
        if not (self.__open):
            raise ValueError(ACCOUNT_CLOSED_ERROR_MESSAGE)
        self.__open = False
