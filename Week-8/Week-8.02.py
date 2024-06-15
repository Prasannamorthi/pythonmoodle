Create a student dictionary  for n students with the student name as key and their test mark assignment mark and lab mark as values. Do the following computations and display the result.

1.Identify the student with the  highest average score

2.Identify the student who as the highest Assignment marks

3.Identify the student with the Lowest lab marks

4.Identify the student with the lowest average score

Note:

If more than one student has the same score display all the student names



Sample input:

4

James 67 89 56

Lalith 89 45 45

Ram 89 89 89

Sita 70 70 70

Sample Output:

Ram

James Ram

Lalith

Lalith








n = int(input())
s = {}
for _ in range(n):
    data = input().split()
    name = data[0]
    tm, am, l = map(int, data[1:]) 
    s[name] = (tm, am, l)
a = {name: sum(marks) / len(marks) for name, marks in s.items()}
h = max(a.values())
hs = sorted([name for name, score in a.items() if score == h])
m = max([marks[1] for marks in s.values()])
ass = sorted([name for name, marks in s.items() if marks[1] == m])
lm = min([marks[2] for marks in s.values()])
ls = sorted([name for name, marks in s.items() if marks[2] == lm])
avgs = min(a.values())
ags = sorted([name for name, score in a.items() if score == avgs])
print("\n".join([
    " ".join(hs),
    " ".join(ass),
    " ".join(ls),
    " ".join(ags)
]))




t = input()

k = int(input())

a = t.split(",")

l = [int(x) for x in a]

count = 0

x = set()



for i in range(len(l)):

    for j in range(i + 1, len(l)):

        if l[i] + l[j] == k:

            s = (l[i], l[j])

            if s not in x and (l[j], l[i]) not in x:

                count += 1

                x.add(s)



print(count)



