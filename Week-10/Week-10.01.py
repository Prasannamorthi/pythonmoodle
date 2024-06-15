Write a Python program for binary search.

For example:

Input	Result
1,2,3,5,8
6
False
3,5,9,45,42
42
True



arr = list(map(int, input().split(',')))
key = int(input())
fg=0
for i in range(len(arr)):
    if arr[i] == key:
        fg+=1
if(fg):
    print("True")
else:
    print("False")


