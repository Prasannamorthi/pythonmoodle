A sentence is a string of single-space separated words where each word consists only of lowercase letters.A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Example 2:



Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]

 Constraints:

1 <= s1.length, s2.length <= 200

s1 and s2 consist of lowercase English letters and spaces.

s1 and s2 do not have leading or trailing spaces.

All the words in s1 and s2 are separated by a single space.

Note:

Use dictionary to solve the problem


For example:

Input	Result
this apple is sweet
this apple is sour
sweet sour

s1 = input()
s2 = input()
words = (s1 + " " + s2).split()
c = {}
for word in words:
    if word in c:
        c[word] += 1
    else:
        c[word] = 1
u = [word for word, count in c.items() if count == 1]
o = " ".join(u)
print(o)

