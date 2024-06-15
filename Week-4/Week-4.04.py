number=int(input())
num_str = str(number)
unique_digits = set()
for digit in num_str:
    unique_digits.add(digit)
unique_digit_count = len(unique_digits)
print(unique_digit_count)
