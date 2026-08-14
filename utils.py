def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def factorial(n):
    if n < 0:
        raise ValueError("Negative values are not allowed")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def is_palindrome(s):
    return s == s[::-1]


def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged