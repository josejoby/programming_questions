"""
Problem Description
Given an array of size N, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exists in the array.



Problem Constraints
1 <= N <= 5*105
1 <= num[i] <= 109


Input Format
Only argument is an integer array.


Output Format
Return an integer.


Example Input
Input 1:
[2, 1, 2]
Input 2:
[1, 1, 1]


Example Output
Input 1:
2
Input 2:
1


Example Explanation
For Input 1:
2 occurs 2 times which is greater than 3/2.
For Input 2:
 1 is the only element in the array, so it is majority
"""


def solve(A):
    """ Boyer-Moore Majority Voting Algorithm """
    candidate=None # majority candidate
    count=0
    for i in range(len(A)):
        if count == 0:
            candidate = A[i]
        if A[i]!=candidate:
            count-=1
        elif A[i]==candidate:
            count+=1
    return candidate


print(solve([2, 1, 2])==2)
print(solve([1,1,1])==1)
print(solve([1,1,2])==1)
