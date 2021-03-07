def slices(series:str, length:int) -> list:
    if length > 0 and length <= len(series):
        return [
            series[slice(i, length + i, 1)]
            for i in range(len(series) - length + 1)
        ]
    raise ValueError('Enter a valid length value.')

