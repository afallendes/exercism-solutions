def classify(number:int) -> str:
    if number > 0:
        s = sum(factors(number))
        if s > number:
            return 'abundant'
        if s < number:
            return 'deficient'
        return 'perfect'
    raise ValueError('Enter a valid natural number.')

def factors(number:int) -> list[int]:
    # poorly optimized algo
    return [
        i
        for i in range(1, number // 2 + 1)
        if number % i == 0
    ]
