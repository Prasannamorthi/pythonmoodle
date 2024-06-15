Reverse a string without affecting special characters
 Given a string S, containing special characters and all the alphabets, reverse the string without affecting the positions of the special characters.
Input:
A&B
Output:
B&A
Explanation: As we ignore '&' and
As we ignore '&' and then reverse, so answer is "B&A".


For example:

Input	Result
A&x#
x&A#

s=input()
l=[]
for i in s:
    if(i.isalpha()):
        l.append(i)
l.reverse()
result=''
index=0
for i in s:
    if(i.isalpha()):
        result+=l[index]
        index+=1
    else:
        result+=i
print(result)



