Give a dictionary with value lists, sort the keys by summation of values in value list.

 Input : test_dict = {‘Gfg’ : [6, 7, 4], ‘best’ : [7, 6, 5]}

Output : {‘Gfg’: 17, ‘best’: 18}

Explanation : Sorted by sum, and replaced.

 Input : test_dict = {‘Gfg’ : [8,8], ‘best’ : [5,5]}

Output : {‘best’: 10, ‘Gfg’: 16}

Explanation : Sorted by sum, and replaced.

 Sample Input:

2

Gfg 6 7 4

Best 7 6 5

Sample Output

Gfg 17

Best 18

 



For example:

Input	Result
2
Gfg 6 7 4
Best 7 6 5
Gfg 17
Best 18




test_dict = {}
n = int(input())
for _ in range(n):
    key, *values = input().split()
    test_dict[key] = list(map(int, values))

sorted_keys = [key for key, _ in sorted(test_dict.items(), key=lambda item: sum(item[1]))]
result_dict = {key: sum(test_dict[key]) for key in sorted_keys}

for key, value in result_dict.items():
    print(key, value)

