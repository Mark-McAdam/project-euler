"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000. 
This problem seems similar to fizzbuzz
"""


def get_sum(x):
    """
    If x is divisble by 3 
    or divisible by 5 
    return the sum of divisible numbers 
    """
    sum_this = []

    for value in range(1, x):

        if value % 3 == 0 or value % 5 == 0:

            sum_this.append(value)

            summer = sum(sum_this)

    return summer


if __name__ == "__main__":
    print(get_sum(1000))
