String should contain only the words are not palindrome.

 

Sample Input 1

 

Malayalam is my mother tongue

 

Sample Output 1

 

is my mother tongue


a=input()
a=a.lower()
b=a.split()
l1=[]
for i in b:
    s=i[::-1]
    if(s==i):
        continue
    else:
        l1.append(i)
for i in l1:
    print(i,end=' ')

 

    zipped_list = zip_lists(list1, list2)

    print(zipped_list)

