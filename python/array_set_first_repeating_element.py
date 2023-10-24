"""
Problem Description
Given an integer array A of size N, find the first repeating element in it.

We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.

If there is no repeating element, return -1.



Problem Constraints
1 <= N <= 105

1 <= A[i] <= 109



Input Format
The first and only argument is an integer array A of size N.



Output Format
Return an integer denoting the first repeating element.



Example Input
Input 1:

 A = [10, 5, 3, 4, 3, 5, 6]
Input 2:

 A = [6, 10, 5, 4, 9, 120]


Example Output
Output 1:

 5
Output 2:

 -1


Example Explanation
Explanation 1:

 5 is the first element that repeats
Explanation 2:

 There is no repeating element, output -1

"""

def solve(A):
    first_occ={}
    seen=set()
    duplicated=set()
    for i in range(len(A)):
        elem = A[i]
        if elem in seen:
            duplicated.add(elem)
        else:
            seen.add(elem)
            first_occ[elem] = i
    min_occ=len(A)
    for elem in duplicated:
        if first_occ[elem] < min_occ:
            min_occ=first_occ[elem]
    return -1 if min_occ==len(A) else A[min_occ]
        

print(solve([10, 5, 3, 4, 3, 5, 6])==5)
print(solve([6, 10, 5, 4, 9, 120])==-1)