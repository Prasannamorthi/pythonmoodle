Find if a String2 is substring of String1. If it is, return the index of the first occurrence. else return -1.

Sample Input 1 

thistest123string

123

Sample Output 1 

8

 
a=input()
b=input()
if(a.find(b)==-1):
    print(-1)
else:
    print(a.find(b))

