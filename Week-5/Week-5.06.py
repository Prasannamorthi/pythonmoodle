Write a python to read a sentence and print its longest word and its length


For example:

Input	Result
This is a sample text to test
sample
6


a=input()
b=a.split()
l=max(b,key=len)
print(l)
print(len(l))

