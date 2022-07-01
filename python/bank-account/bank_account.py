import threading

class BankAccount:

    error_messages = [
        'amount must be greater than 0',
        'amount must be less than balance',
        'account not open',
        'account already open'
    ]

    def __init__(self) -> None:
        self.__open = False
        self.__lock = threading.Lock()

    def get_balance(self) -> None:
        if self.__open:
            return self.__balance
        raise ValueError(self.error_messages[2])

    def open(self) -> None:
        if self.__open:
            raise ValueError(self.error_messages[3])
        self.__open = True
        self.__balance = 0

    def deposit(self, amount:int) -> None:
        with self.__lock:
            if not (self.__open):
                raise ValueError(self.error_messages[2])
            if not (amount > 0):
                raise ValueError(self.error_messages[0])
            self.__balance += amount

    def withdraw(self, amount:int) -> None:
        with self.__lock:
            if not (self.__open):
                raise ValueError(self.error_messages[2])
            if not (self.__balance >= amount):
                raise ValueError(self.error_messages[1])
            if not (amount > 0):
                raise ValueError(self.error_messages[0])
            self.__balance -= amount

    def close(self) -> None:
        if not (self.__open):
            raise ValueError(self.error_messages[2])
        self.__open = False
