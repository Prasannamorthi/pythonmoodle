Write a code to check whether product of digits at even places is divisible by sum of digits

at odd place of a positive integer.

Input Format:

Take an input integer from stdin.

Output Format:

Print TRUE or FALSE.

Example Input:

1256

Output:

TRUE

Example Input:

1595

Output:

FALSE

For example:

Test	Result
print(productDigits(1256))
True
print(productDigits(1595))
False



def productDigits(number):
    number_str = str(number)
    product_even_positions = 1
    sum_odd_positions = 0
    
    for i, digit in enumerate(number_str, start=1):
        digit = int(digit)
        if i % 2 == 1:
            sum_odd_positions += digit
        else:
            product_even_positions *= digit

    if sum_odd_positions == 0:
        return False

    return product_even_positions % sum_odd_positions == 0
    

