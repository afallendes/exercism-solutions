def is_armstrong_number(number:int):
    return sum([ int(_) ** len(str(number)) for _ in str(number) ]) == number