number=int(input())
if number < 10:
    print("yes")
else:
    for factor in range(2, 10):
        if number % factor == 0 and 1 <= number // factor <=9:
          print("Yes")
          break
    else:
         print("No")
