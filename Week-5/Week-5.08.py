Robert  is having 2 strings consist of uppercase & lowercase english letters. Now he want to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter.


Input
The first line contains T. Then T test cases follow.

Each test case contains a two lines contains a string. The strings' lengths range from 1 to 100 inclusive. It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.

Output
If the first string is less than the second one, print "-1".
If the second string is less than the first one, print "1".
If the strings are equal, print "0".
Note that the letters' case is not taken into consideration when the strings are compared.

Constraints
                      1≤T≤50
                      String length≤100

For example:

Input	Result
3
aaaa
aaaA
abs
Abz
abcdefg
AbCdEfF
0
-1
1

def compare_strings_lexicographically():
    T = int(input())  # Number of test cases
    for _ in range(T):
        string1 = input().lower()
        string2 = input().lower()

        if string1 < string2:
            print("-1")
        elif string1 > string2:
            print("1")
        else:
            print("0")

# Call the function
compare_strings_lexicographically()


