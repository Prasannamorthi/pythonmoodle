Write a program to eliminate the common elements in the given 2 arrays and print only the non-repeating

elements and the total number of such non-repeating elements.

Input Format:

The first line contains space-separated values, denoting the size of the two arrays in integer format respectively.

The next two lines contain the space-separated integer arrays to be compared.

Sample Input:

5 4

1 2 8 6 5

2 6 8 10

Sample Output:

1 5 10

3

Sample  Input: 

5 5

1 2 3 4 5

1 2 3 4 5

Sample Output:

NO SUCH ELEMENTS



For example:

Input	Result
5 4
1 2 8 6 5
2 6 8 10
1 5 10
3


def find_non_repeating_elements(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    unique_to_set1 = set1.difference(set2)
    unique_to_set2 = set2.difference(set1)
    non_repeating_elements = unique_to_set1.union(unique_to_set2)
    
    return non_repeating_elements
size1, size2 = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

non_repeating_elements = find_non_repeating_elements(arr1, arr2)
if non_repeating_elements:
    print(' '.join(map(str, sorted(non_repeating_elements))))
    print(len(non_repeating_elements))
else:
    print("NO SUCH ELEMENTS")


  
