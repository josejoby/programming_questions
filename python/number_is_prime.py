"""
Problem Description
Given a number A. Return 1 if A is prime and return 0 if not. 

Note : 
The value of A can cross the range of Integer.


Problem Constraints
1 <= A <= 109


Input Format
The first argument is a single integer A.


Output Format
Return 1 if A is prime else return 0.


Example Input
Input 1:
A = 5
Input 2:

A = 10


Example Output
Output 1:
1
Output 2:

0


Example Explanation
Explanation 1:
5 is a prime number.
Explanation 2:

10 is not a prime number.
"""

import math

def solve(A):
    if A < 2:
            return 0
    for i in range(2, (int)(math.sqrt(A)+1)):
        if A%i == 0:
            return 0
    return 1


inp = [0, 1, 2, 3, 5, 6, 9, 10, 11]
for _ in inp:
     print(f"{_} -> {solve(_)}")
