import re

class PhoneNumber:
    """ This class stores and normalizes user-entered NANP phone numbers. """

    def __init__(self, number:str) -> None:
        self.normalize(self.clean(number))
    
    def clean(self, number:str) -> str:
        """ Cleans input from any non-numeric character. """ 
        return re.sub(r'\D', '', number)
    
    def normalize(self, number:str) -> None:
        """ Normalizes phone number if entered number is a valid US number. """

        if len(number) == 0: # after cleaning out all non-numeric chars
            raise ValueError("letters not permitted")

        if len(number) < 10:
            raise ValueError("incorrect number of digits")

        if len(number) > 11:
            raise ValueError("more than 11 digits")

        if len(number) == 11 and number[0] != 1:
            raise ValueError("11 digits must start with 1")

        # if a phone number has punctuation in place of some digits.
        # raise ValueError("punctuations not permitted")

        # if a phone number has letters in place of some digits.
        # raise ValueError("letters not permitted")
        
        p = re.compile(r'^1?(?P<number>(?P<area_code>[2-9]{1}\d{2})(?P<exchange_code>[2-9]{1}\d{2})(?P<subscriber_number>\d{4}))')
        m = p.match(number)



        if m['exchange_code'][0] == 0:
            raise ValueError("exchange code cannot start with zero")

        if m['exchange_code'][0] == 1:
            raise ValueError("exchange code cannot start with one")

        if m['area_code'][0] == 0:
            raise ValueError("area code cannot start with zero")

        if m['area_code'][0] == 1:
            raise ValueError("area code cannot start with one")

        if m:
            self.number = m['number']
            self.area_code = m['area_code']
            self.exchange_code = m['exchange_code']
            self.subscriber_number = m['subscriber_number']
            return None
    
    def pretty(self) -> str:
        """ Prints stylized phone number. """
        return f'({self.area_code})-{self.exchange_code}-{self.subscriber_number}'

    def __str__(self):
        return self.pretty()

