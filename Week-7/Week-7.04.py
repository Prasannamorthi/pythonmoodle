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



def findRepeatedDnaSequences(s):
    if len(s) < 10:
        return []

    sequences = {}
    result = []

    for i in range(len(s) - 9):
        substring = s[i:i+10]
        if substring in sequences:
            sequences[substring] += 1
        else:
            sequences[substring] = 1

    for sequence, count in sequences.items():
        if count > 1:
            result.append(sequence)
    for i in result:
        print(i)

s1=input()

findRepeatedDnaSequences(s1)


         
