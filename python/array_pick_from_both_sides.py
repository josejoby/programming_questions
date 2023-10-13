"""
https://www.scaler.com/academy/mentee-dashboard/class/126180/homework/problems/9900?navref=cl_tt_nv
You are given an integer array A of size N.

You have to perform B operations. In one operation, you can remove either the leftmost or the rightmost element of the array A.

Find and return the maximum possible sum of the B elements that were removed after the B operations.

NOTE: Suppose B = 3, and array A contains 10 elements, then you can:

Remove 3 elements from front and 0 elements from the back, OR
Remove 2 elements from front and 1 element from the back, OR
Remove 1 element from front and 2 elements from the back, OR
Remove 0 elements from front and 3 elements from the back.


1 <= N <= 10**5

1 <= B <= N

-10**3 <= A[i] <= 10**3

Input Format
    First argument is an integer array A.
    Second argument is an integer B
Output Format
    Return an integer denoting the maximum possible sum of elements you removed.

Input 1:
 A = [5, -2, 3 , 1, 2]
 B = 3
 op = 8  Remove element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8
Input 2:
 A = [ 2, 3, -1, 4, 2, 1 ]
 B = 4
op = 9  Remove the first element and the last 3 elements. So we get 2 + 4 + 2 + 1 = 9
"""

def solve(A, B):
    pass
# print(solve([5, -2, 3 , 1, 2], 3)) # 8
# print(solve([ 2, 3, -1, 4, 2, 1 ], 4)) # 9

print(solve([-533,-666,-500,169,724,478,358,-38,-536,705,-855,281,-173,961,-509,-5,942,-173,436,-609,-396,902,-847,-708,-618,421,-284,718,895,447,726,-229,538,869,912,667,-701,35,894,-297,811,322,-667,673,-336,141,711,-747,-132,547,644,-338,-243,-963,-141,-277,741,529,-222,-684,35], 1)) #35