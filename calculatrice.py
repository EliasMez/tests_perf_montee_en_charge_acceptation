def additionner(a, b):
    if isinstance(a, list):
        return sum(a) + b
    return a + b

def soustraire(a, b):
    return a - b

def factorial_recursive(n):
    if n < 0:
        raise ValueError('n must be non-negative')
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
