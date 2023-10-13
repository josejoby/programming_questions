"""
Problem Description
Given an integer array A of size N and an integer B, you have to return the same array after rotating it B times towards the right.


Problem Constraints
1 <= N <= 105
1 <= A[i] <=109
1 <= B <= 109


Input Format
The first argument given is the integer array A.
The second argument given is the integer B.


Output Format
Return the array A after rotating it B times to the right


Example Input
Input 1:

A = [1, 2, 3, 4]
B = 2
Input 2:

A = [2, 5, 6]
B = 1


Example Output
Output 1:

[3, 4, 1, 2]
Output 2:

[6, 2, 5]


Example Explanation
Explanation 1:

Rotate towards the right 2 times - [1, 2, 3, 4] => [4, 1, 2, 3] => [3, 4, 1, 2]
Explanation 2:

Rotate towards the right 1 time - [2, 5, 6] => [6, 2, 5]
"""

def reverse(A, left, right):
        while left<right:
            A[left] = A[left]+A[right]
            A[right]= A[left]-A[right]
            A[left]= A[left]-A[right]
            left+=1
            right-=1
        return A

def solve(A, B):
    k = B%len(A)
    l=len(A)-1
    # reversing array
    A = reverse(A, 0, l) 
    #reverse(A,0,k-1)
    A = reverse(A, 0, k-1) 
    #reverse(A,k,len(A)-1)
    A = reverse(A, k, l)
    return A