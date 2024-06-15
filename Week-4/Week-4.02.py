number = int(input())
num_str = str(number)
length = len(num_str)
total = 0
for i in range(length):
    total += int(num_str[i]) ** (i + 1)
if total==number:
    print("Yes")
else:
    print("No")



