number=int(input())
num_str=str(number)
non_repeated_digits=[]
for digit in num_str:
    if num_str.count(digit)==1:
        non_repeated_digits.append(int(digit))
non_repeated_count =len(non_repeated_digits)
print(non_repeated_count)


