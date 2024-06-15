Given an list, find peak element in it. A peak element is an element that is greater than its neighbors.

An element a[i] is a peak element if

A[i-1] <= A[i] >=a[i+1] for middle elements. [0<i<n-1]

A[i-1] <= A[i] for last element [i=n-1]

A[i]>=A[i+1] for first element [i=0]

Input Format

The first line contains a single integer n , the length of A .
The second line contains n space-separated integers,A[i].

Output Format

Print peak numbers separated by space.

Sample Input

5

8 9 10 2 6

Sample Output

10 6


def find_and_print_peak_elements(n, arr):
    if n == 1:
        print(arr[0])
    else:
        if arr[0] >= arr[1]:
            print(arr[0], end=" ")
        for i in range(1, n - 1):
            if arr[i - 1] <= arr[i] >= arr[i + 1]:
                print(arr[i], end=" ")
        if arr[n - 1] >= arr[n - 2]:
            print(arr[n - 1], end=" ")
n = int(input())
arr = list(map(int, input().split()))
find_and_print_peak_elements(n, arr)


