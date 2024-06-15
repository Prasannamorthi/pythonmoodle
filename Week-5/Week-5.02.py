Assume that the given string has enough memory.

 

Don't use any extra space(IN-PLACE)

 

Sample Input 1

 

a2b4c6

 

Sample Output 1

 

aabbbbcccccc


s=input()
result=''
i=0
while(i<len(s)):
    char=s[i]
    i+=1
    num=''
    while(i<len(s) and s[i].isdigit()):
        num+=s[i]
        i+=1
    result=char*int(num)
    print(result,end='')

