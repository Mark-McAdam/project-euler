"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""


def Largest_Prime_Factor(n):
    """
    uses math and a little logic to figure out the largest prime factor of an input number
    Increment through the numbers until we have largest prime factor alone
    """
    prime_factor = 1
    i = 2

    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1
    if prime_factor < n:
        prime_factor = n

    return prime_factor


print(Largest_Prime_Factor(600851475143))

print(13195 / 3)
print(13195 / 5)
print(13195 / 10)
