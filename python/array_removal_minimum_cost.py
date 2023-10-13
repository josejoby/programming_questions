"""
Problem Description
Given an integer array A of size N. You can remove any element from the array in one operation.
The cost of this operation is the sum of all elements in the array present before this operation.

Find the minimum cost to remove all elements from the array.

Problem Constraints
0 <= N <= 1000
1 <= A[i] <= 103

Input Format
First and only argument is an integer array A.

Output Format
Return an integer denoting the total cost of removing all elements from the array.


A = [2, 1] op = 4
A = [5] op = 5

"""

def solve(A):
    A.sort(reverse=True)
    cost=0
    arrsum = 0
    for _ in range(len(A)):
        arrsum +=A[_]
    for _ in range(len(A)):
        cost+=arrsum
        arrsum-=A[_]
    return cost


print(solve([2, 1]))
print(solve([5]))
print(solve([5,4,3,2,1])) # 35
print(solve([])) # 0
print(solve([-1,-2, -10, 5, 1])) # -54

