"""
Problem Description
Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array

and at least one occurrence of the minimum value of the array.



Problem Constraints
1 <= |A| <= 2000



Input Format
First and only argument is vector A



Output Format
Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array



Example Input
Input 1:

A = [1, 3, 2]
Input 2:

A = [2, 6, 1, 6, 9]


Example Output
Output 1:

 2
Output 2:

 3


Example Explanation
Explanation 1:

 Take the 1st and 2nd elements as they are the minimum and maximum elements respectievly.
Explanation 2:

 Take the last 3 elements of the array.
"""

def carry_backward(arr):
    min_idx = max_idx = -1
    min_elem = maxx_elem = arr[0]
    for _ in range(len(arr)): # finding min and max elements
        if arr[_]< min_elem:
            min_elem = arr[_]
        elif arr[_] > maxx_elem:
            maxx_elem = arr[_]
    if min_elem == maxx_elem: # edge case
        return 1
    len_smallest = len(arr) # assuming the smallest_subarray is the array itself
    for i in range(len(arr)-1, 0, -1): # finding smallest subarrays
        if arr[i] == min_elem:
            min_idx = i
        elif arr[i] == maxx_elem:
            max_idx = i
        if min_idx > -1 and max_idx > -1:
            len_smallest = min(abs(min_idx - max_idx)+1, len_smallest)
    return len_smallest

def solve(A):
    maxx = A[0]
    minn = A[0]
    for _ in range(len(A)):
        if A[_] > maxx:
            maxx = A[_]
        elif A[_] < minn:
            minn = A[_]
    if minn == maxx: # edge case
        return 1
    min_idx = -1
    max_idx = -1
    l=len(A)
    for _ in range(len(A)-1, -1, -1):
        if A[_] == minn:
            min_idx = _
        elif A[_] == maxx:
            max_idx = _
        if min_idx > -1 and max_idx > -1:
            l = min(l, abs(min_idx-max_idx)+1)
    return l


# print(carry_backward([2,2,6,4,5,1,5,2,6,4,1])) #3
# print(carry_backward([814,761,697,483,981])) #2
print(carry_backward([4,4,4,4,4])) #1