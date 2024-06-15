Given a tuple and a positive integer k, the task is to find the count of distinct pairs in the tuple whose sum is equal to K.

Examples:

Input: t = (5, 6, 5, 7, 7, 8 ), K = 13 
Output: 2 
Explanation: 
Pairs with sum K( = 13) are  {(5, 8), (6, 7), (6, 7)}. 
Therefore, distinct pairs with sum K( = 13) are { (5, 8), (6, 7) }. 
Therefore, the required output is 2.



For example:

Input	Result
1,2,1,2,5
3
1
1,2
0
0


def find_pairs_with_sum(numbers, target_sum):
    # Convert the tuple to a list to enable mutability
    numbers_list = list(numbers)
    
    # Create a set to store the pairs
    pairs = set()
    
    # Create a set to store the visited numbers
    visited = set()
    
    for number in numbers_list:
        complement = target_sum - number
        if complement in visited:
            # To ensure pairs are stored in a consistent order (e.g., (small, large))
            pair = tuple(sorted((number, complement)))
            pairs.add(pair)
        visited.add(number)
    
    return pairs

# Taking input from the user
numbers_input = input("")
target_sum = int(input(""))

# Convert the input string to a tuple of integers
numbers = tuple(map(int, numbers_input.split(',')))

# Find pairs
pairs = find_pairs_with_sum(numbers, target_sum)

print(f"{len(pairs)}")

         
