Square Root

Write a simple python program to find the square root of a given floating point number. The output should be displayed with 3 decimal places.





Sample Input:

8.00

Sample Output:

2.828

For example:

Input	Result

14.00	3.742


import math
a=float(input())
if math.sqrt(a)%2==0:
    print(math.sqrt(a),end='')
    print("00")
else:
    print(round(math.sqrt(a),3))

