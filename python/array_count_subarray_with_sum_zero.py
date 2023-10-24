"""
Problem Description
Given an array A of N integers.

Find the count of the subarrays in the array which sums to zero. Since the answer can be very large, return the remainder on dividing the result with 109+7


Problem Constraints
1 <= N <= 105
-109 <= A[i] <= 109


Input Format
Single argument which is an integer array A.


Output Format
Return an integer.


Example Input
Input 1:

 A = [1, -1, -2, 2]
Input 2:

 A = [-1, 2, -1]


Example Output
Output 1:

3
Output 2:

1


Example Explanation
Explanation 1:

 The subarrays with zero sum are [1, -1], [-2, 2] and [1, -1, -2, 2].
Explanation 2:

 The subarray with zero sum is [-1, 2, -1].

"""

def solve(A):
    result=0
    # create pf array
    pf=[]
    d={}
    for i in range(len(A)):
        pfv=pf[i-1]+A[i] if i > 0 else A[i]
        pf.append(pfv)
        d[pfv] = 1 if pfv not in d else d[pfv]+1
    for v in pf:
        if v == 0:
            result+=1
    for vcount in d.values():
        if vcount > 1:
            result+=vcount*(vcount-1)//2
    return result
    


print(solve([1, -1, -2, 2])==3)
print(solve([-1, 2, -1])==1)
print(solve([4, 8, 3, 6, -5, -4, 7, -2, 1, -6, 2])==3)