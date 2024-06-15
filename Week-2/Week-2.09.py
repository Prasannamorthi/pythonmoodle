Write a python program that takes a integer between 0 and 15 as input and displays the number of '1' s in its binary form.(Hint:use python bitwise operator.

Sample Input

3

Sample Output:

2

Explanation:

The binary representation of 3 is 011, hence there are 2 ones in it. so the output is 2.


For example:

Input	Result
3
2




def count_ones_in_binary(number):
    count = 0
    while number > 0:
        if number & 1:
            count += 1
        number >>= 1
    return count
number = int(input(""))
if 0 <= number <= 15:
    ones = count_ones_in_binary(number)
    print(f"{ones}")
else:
    print(f"Invalid input: {number} is not between 0 and 15.")
