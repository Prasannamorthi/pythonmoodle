Three numbers form a Pythagorean triple if the sum of squares of two numbers is equal to the square of the third.

For example, 3, 5 and 4 form a Pythagorean triple, since 3*3 + 4*4 = 25 = 5*5

You are given three integers, a, b, and c. They need not be given in increasing order. If they form a Pythagorean triple, then print "yes", otherwise, print "no". Please note that the output message is in small letters.

Sample Input

3

5

4

Sample Output

yes

Sample Test Cases

Test Case 1     

Input

3

5

4

Output

yes

Test Case 2     

Input

5

8

2

Output

noThree numbers form a Pythagorean triple if the sum of squares of two numbers is equal to the square of the third.

For example, 3, 5 and 4 form a Pythagorean triple, since 3*3 + 4*4 = 25 = 5*5

You are given three integers, a, b, and c. They need not be given in increasing order. If they form a Pythagorean triple, then print "yes", otherwise, print "no". Please note that the output message is in small letters.

Sample Input

3

5

4

Sample Output

yes

Sample Test Cases

Test Case 1     

Input

3

5

4

Output

yes

Test Case 2     

Input

5

8

2

Output

no




a=int(input())
b=int(input())
c=int(input())
x=a*a
y=b*b
z=c*c
if(x+y==z or x+z==y or z+y==x):
    print("yes")
else:
    print("no")a=int(input())
b=int(input())
c=int(input())
x=a*a
y=b*b
z=c*c
if(x+y==z or x+z==y or z+y==x):
    print("yes")
else:
    print("no")

