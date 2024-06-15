Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order. You read an list of numbers. You need to arrange the elements in ascending order and print the result. The sorting should be done using bubble sort.

Input Format: The first line reads the number of elements in the array. The second line reads the array elements one by one.


Output Format: The output should be a sorted list.



For example:

Input	Result
6
3 4 8 7 1 2
1 2 3 4 7 8
5 
4 5 2 3 1
1 2 3 4 5


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

n = int(input())
arr = list(map(int, input().split()))
sorted_arr = bubble_sort(arr)
print(" ".join(map(str, sorted_arr)))

print("Last Element:", arr[-1])



