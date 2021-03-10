import re

class PhoneNumber:
    """ This class stores and normalizes user-entered NANP phone numbers. """

    def __init__(self, number:str) -> None:
        self.normalize(self.clean(number))
    
    def clean(self, number:str) -> str:
        """ Cleans input from any non-numeric character. """ 
        return re.sub(r'\D', '', number)
    
    def normalize(self, number:str) -> None:
        """ Normalizes if entered number is a valid US number. """
        if len(number) == 10 or (len(number) == 11 and number[0] == '1'):
            p = re.compile(r'^1?(?P<number>(?P<area_code>[2-9]{1}\d{2})(?P<exchange_code>[2-9]{1}\d{2})(?P<subscriber_number>\d{4}))')
            m = p.match(number)
            if m:
                self.number = m['number']
                self.area_code = m['area_code']
                self.exchange_code = m['exchange_code']
                self.subscriber_number = m['subscriber_number']
                return None
        raise ValueError('Enter a valid NANP phone number.')
    
    def pretty(self) -> str:
        """ Prints stylized phone number. """
        return f'({self.area_code})-{self.exchange_code}-{self.subscriber_number}'

    def __str__(self):
        return self.pretty()

