In this exercise you will create a program that reads a letter of the alphabet from the user. If the user enters a, e, i, o or u then your program should display a message indicating that the entered letter is a vowel. If the user enters y then your program should display a message indicating that sometimes y is a vowel, and sometimes y is a consonant. Otherwise your program should display a message indicating that the letter is a consonant.

Sample Input 1

i

Sample Output 1

It's a vowel.

Sample Input 2

y

Sample Output 2

Sometimes it's a vowel... Sometimes it's a consonant.

Sample Input3

c

Sample Output 3

It's a consonant.


For example:

Input	Result
y
Sometimes it's a vowel... Sometimes it's a consonant.
c
It's a consonant.


_a=input()
if(_a=='a' or _a=='e' or _a=='i' or _a=='o' or _a=='u'):
    print("It's a vowel.")
elif(_a=='y'):
    print("Sometimes it's a vowel... Sometimes it's a consonant.")
else:
    print("It's a consonant.")

