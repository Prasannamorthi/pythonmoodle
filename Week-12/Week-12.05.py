Given an integer n, print true if it is a power of two. Otherwise, print false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

For example:

Input	Result
1
True
80
False
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Input
n = int(input())

# Check if n is a power of two
result = is_power_of_two(n)

# Output
print(result)


