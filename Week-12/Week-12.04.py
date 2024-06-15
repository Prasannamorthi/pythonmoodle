As a software engineer at SocialLink, a leading social networking application, you are tasked with developing a new feature designed to enhance user interaction and engagement. The company aims to introduce a system where users can form connections based on shared interests and activities. One of the feature's components involves analyzing pairs of users based on the activities they've participated in, specifically looking at the numerical difference in the number of activities each user has participated in.

Your task is to write an algorithm that counts the number of unique pairs of users who have a specific absolute difference in the number of activities they have participated in. This algorithm will serve as the backbone for a larger feature that recommends user connections based on shared participation patterns.

Problem Statement

Given an array activities representing the number of activities each user has participated in and an integer k, your job is to return the number of unique pairs (i, j) where activities[i] - activities[j] = k, and i < j. The absolute difference between the activities should be exactly k.

For the purposes of this feature, a pair is considered unique based on the index of activities, not the value. That is, if there are two users with the same number of activities, they are considered distinct entities.

Input Format

The first line contains an integer, n, the size of the array nums.

The second line contains n space-separated integers, nums[i].

The third line contains an integer, k.


Output Format

Return a single integer representing the number of unique pairs (i, j) 

where | nums[i] - nums[j] | = k and i < j.


Constraints:

1 ≤ n ≤ 105

-104 ≤ nums[i] ≤ 104

0 ≤ k ≤ 104



For example:

Input	Result
5
1 3 1 5 4
0
1
4
1 2 2 1
1
4

def count_pairs(activities, k):
    activity_count = {}  # Dictionary to count occurrences of each activity count
    unique_pairs = 0  # Initialize count of unique pairs

    # Count occurrences of each activity count
    for activity in activities:
        activity_count[activity] = activity_count.get(activity, 0) + 1

    # Count unique pairs with absolute difference k
    for activity in activity_count:
        # If k is 0, count all pairs of the same activity
        if k == 0:
            unique_pairs += activity_count[activity] * (activity_count[activity] - 1) // 2
        # If k is not 0, check if activity + k exists and count pairs
        elif activity + k in activity_count:
            unique_pairs += activity_count[activity] * activity_count[activity + k]

    return unique_pairs

if __name__ == "__main__":
    # Input
    n = int(input())
    activities = list(map(int, input().split()))
    k = int(input())

    # Output
    result = count_pairs(activities, k)
    print(result)






