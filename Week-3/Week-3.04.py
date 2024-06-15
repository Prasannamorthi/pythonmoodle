Write a program that returns the second last digit of the given number. Second last digit is being referred 10the digit in the tens place in the given number.

For example, if the given number is 197, the second last digit is 9.

Note1 - The second last digit should be returned as a positive number. i.e. if the given number is -197, the second last digit is 9.

Note2 - If the given number is a single digit number, then the second last digit does not exist. In such cases, the program should return -1. i.e. if the given number is 5, the second last digit should be returned as -1



For example:

Input	Result
197
9
5
-1



a=int(input())

if(a<0):
    a=a*-1
if(a<10):
    print("-1")
else:
    a=a//10
    a=a%10

    print(a)
