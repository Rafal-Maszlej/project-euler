"""
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_divisible(number, n):
    return 0.5 * ((number - 1) // n) * ((number - 1) // n + 1) * n


def sum_multiples(number):
    return sum_divisible(number, 3) + sum_divisible(number, 5) - sum_divisible(number, 15)


if __name__ == '__main__':
    assert sum_multiples(10) == 23
    assert sum_multiples(1_000) == 233168
    assert sum_multiples(1_000_000) == 233333166668
    assert sum_multiples(1_000_000_000) == 233333333166666688
