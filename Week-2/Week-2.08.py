Pretend that you have just opened a new savings account that earns 4 percent interest per year. The interest that you earn is paid at the end of the year, and is added to the balance of the savings account. Write a program that begins by reading the amount of money deposited into the account from the user. Then your program should compute and display the amount in the savings account after 1, 2, and 3 years. Display each amount so that it is rounded to 2 decimal places. Sample Input: 10000 Sample Output: Balance as of end of Year 1: $10400.00. Balance as of end of Year 2: $10816.00. Balance as of end of Year 3: $11248.64.
For example:

Input	Result
10000
Balance as of end of Year 1: $10400.00.
Balance as of end of Year 2: $10816.00.
Balance as of end of Year 3: $11248.64.
Pretend that you have just opened a new savings account that earns 4 percent interest per year. The interest that you earn is paid at the end of the year, and is added to the balance of the savings account. Write a program that begins by reading the amount of money deposited into the account from the user. Then your program should compute and display the amount in the savings account after 1, 2, and 3 years. Display each amount so that it is rounded to 2 decimal places. Sample Input: 10000 Sample Output: Balance as of end of Year 1: $10400.00. Balance as of end of Year 2: $10816.00. Balance as of end of Year 3: $11248.64.
For example:

Input	Result
10000
Balance as of end of Year 1: $10400.00.
Balance as of end of Year 2: $10816.00.
Balance as of end of Year 3: $11248.64.



def calculate_savings_account_balance(principal, interest_rate, years):
    balance = principal
    for year in range(1, years + 1):
        interest = balance * interest_rate / 100
        balance += interest
        balance = round(balance, 2)
    return balance
def main():
    principal = float(input())
    interest_rate = 4
    for years in [1, 2, 3]:
        balance = calculate_savings_account_balance(principal, interest_rate, years)
        print(f"Balance as of end of Year {years}: $""%.2f."%balance)
if __name__ == "__main__":
    main()

else:

    print("False")

