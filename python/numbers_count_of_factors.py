"""
Problem Description
Given an integer A, you need to find the count of it's factors.

Factor of a number is the number which divides it perfectly leaving no remainder.

Example : 1, 2, 3, 6 are factors of 6


Problem Constraints
1 <= A <= 109


Input Format
First and only argument is an integer A.


Output Format
Return the count of factors of A.


Example Input
Input 1:
5
Input 2:
10


Example Output
Output 1:
2
Output 2:
4


Example Explanation
Explanation 1:
Factors of 5 are 1 and 5.
Explanation 2:
Factors of 10 are 1, 2, 5 and 10.


"""

from perf_measurer import log_time
import math

@log_time
def solve(A):
    if A == 1:
        return 1
    x=1
    count=0
    while x<=A/x:
        if A%x == 0:
            count = count+1 if x == A/x else count+2
        x+=1
    return count

@log_time
def solve1(A): # better soln when inp size increases
    count = 0
    root = (int)(math.sqrt(A))
    for i in range(1 , root + 1):
        if A % i == 0:
            if i * i == A:
                count += 1
            else:
                count += 2
    return count

# inp =[1, 2, 10, 11, 49]
inp = [1000000000]
for x in inp:
    # print(f"{x}: {solve(x)}")
    solve1(x)

for x in inp:
    # print(f"{x}: {solve(x)}")
    solve(x)
