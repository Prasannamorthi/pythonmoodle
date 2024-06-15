complete function to implement coin change making problem i.e. finding the minimum

number of coins of certain denominations that add up to given amount of money.

The only available coins are of values 1, 2, 3, 4

Input Format:

Integer input from stdin.

Output Format:

return the minimum number of coins required to meet the given target.

Example Input:

16

Output:

4

Explanation:

We need only 4 coins of value 4 each

Example Input:

25

Output:

7

Explanation:

We need 6 coins of 4 value, and 1 coin of 1 value

def coinChange(n):
    coins = [1, 2, 3, 4]
    min_coins = [float('inf')] * (n + 1)
    min_coins[0] = 0
    for amount in range(1, n + 1):
        for coin in coins:
            if amount - coin >= 0:
               min_coins[amount] = min(min_coins[amount], min_coins[amount - coin] + 1)
    return min_coins[n]
 



