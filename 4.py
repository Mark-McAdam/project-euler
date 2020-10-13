"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""


def Is_Palindrome(num):
    if str(num) == str(num)[::-1]:
        return str(num) == str(num)[::-1]


def Largest_Palindrome(min=99, max=999):
    palindrome = 0
    for x in range(max, min, -1):
        for y in range(max, min, -1):
            product = x * y
            if Is_Palindrome(product) and product > palindrome:
                palindrome = product
    return palindrome


print(str(Largest_Palindrome(99, 999)))
