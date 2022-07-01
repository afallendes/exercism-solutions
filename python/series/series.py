from operator import le


def slices(series:str, length:int) -> list:
    if len(series) == 0:
        raise ValueError('series cannot be empty') 
    if length == 0:
        raise ValueError('slice length cannot be zero')
    if length < 0:
        raise ValueError('slice length cannot be negative')
    if length > len(series):
        raise ValueError('slice length cannot be greater than series length')
    return [
        series[slice(i, length + i, 1)]
        for i in range(len(series) - length + 1)
    ]

