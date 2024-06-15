Write a program to calculate and print the Electricity bill where the unit consumed by the user is given from test case. It prints the total amount the customer has to pay. The charge are as follows: 

Unit                                                     Charge / Unit

Upto 199                                             @1.20

200 and above but less than 400        @1.50

400 and above but less than 600        @1.80

600 and above                                    @2.00

If bill exceeds Rs.400 then a surcharge of 15% will be charged and the minimum bill should be of Rs.100/- 

Sample Test Cases

Test Case 1 

Input

50 

Output

100.00 

Test Case 2

Input 

300

Output 

517.50



For example:

Input	Result
100.00
120.00





a=float(input())
if(a<=199):
    x=a*1.20
elif(a>=200 and a<400):
    x=a*1.50
elif(a>=400 and a<600):
    x=a*1.80
elif(a>=600):
    x=a*2.00
if(x<100):
    print("100.00")
elif(x>400):
    print(f"{(x*0.15)+x:.2f}")
else:
    print(f"{x:.2f}")
