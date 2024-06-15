Background:

Raghu owns a shoe shop with a varying inventory of shoe sizes. The shop caters to multiple customers who have specific size requirements and are willing to pay a designated amount for their desired shoe size. Raghu needs an efficient system to manage his inventory and calculate the total revenue generated from sales based on customer demands.



Problem Statement:

Develop a Python program that manages shoe inventory and processes sales transactions to determine the total revenue generated. The program should handle inputs of shoe sizes available in the shop, track the number of each size, and match these with customer purchase requests. Each transaction should only proceed if the desired shoe size is in stock, and the inventory should update accordingly after each sale.



Input Format:

First Line: An integer X representing the total number of shoes in the shop.

Second Line: A space-separated list of integers representing the shoe sizes in the shop.

Third Line: An integer N representing the number of customer requests.

Next N Lines: Each line contains a pair of space-separated values:

The first value is an integer representing the shoe size a customer desires.

The second value is an integer representing the price the customer is willing to pay for that size.



Output Format:

Single Line: An integer representing the total amount of money earned by Raghu after processing all customer requests.



Constraints:

1≤X≤1000 — Raghu's shop can hold between 1 and 1000 shoes.

Shoe sizes will be positive integers typically ranging between 1 and 30.

1≤N≤1000 — There can be up to 1000 customer requests in a single batch.

The price offered by customers will be a positive integer, typically ranging from $5 to $100 per shoe.



For example:

Input	Result
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
200
5
5 5 5 5 5
5
5 10
5 10
5 10
5 10
5 10
50

def calculate_total_revenue():
    import sys
    input = sys.stdin.read
    data = input().split()
   
    X = int(data[0])
    shoe_sizes = list(map(int, data[1:X+1]))
   
    # Dictionary to keep track of shoe size inventory
    inventory = {}
    for size in shoe_sizes:
        if size in inventory:
            inventory[size] += 1
        else:
            inventory[size] = 1
   
    N = int(data[X+1])
    requests = data[X+2:]
   
    total_revenue = 0
   
    for i in range(N):
        size = int(requests[2 * i])
        price = int(requests[2 * i + 1])
       
        if size in inventory and inventory[size] > 0:
            total_revenue += price
            inventory[size] -= 1
   
    print(total_revenue)

# Assuming this function is called with the standard input properly set up
calculate_total_revenue()


