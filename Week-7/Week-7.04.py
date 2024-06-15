The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 



For example:

Input	Result
AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT
AAAAACCCCC
CCCCCAAAAA


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


         
