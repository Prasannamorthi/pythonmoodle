num=int(input())
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(1)
            break
    else:
            print(2)
else:
    print(1)
