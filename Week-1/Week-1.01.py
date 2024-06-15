Write a program to convert strings to an integer and float and display its type.

Sample Input:

10

10.9

Sample Output:

10,<class 'int'>

10.9,<class 'float'>



For example:

Input	Result
10
10.9
10,<class 'int'>
10.9,<class 'float'>


a=input("")
b=input("")
c=int(a)
d=float(b)
print(c,end=',')
print(type(c))
print(round(d,1),end=',')
print(type(d))
