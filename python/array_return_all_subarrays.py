"""
You are given an array A of N integers.
Return a 2D array consisting of all the subarrays of the array

Note : The order of the subarrays in the resulting 2D array does not matter.


Problem Constraints
1 <= N <= 100
1 <= A[i] <= 105


Input Format
First argument A is an array of integers.


Output Format
Return a 2D array of integers in any order.


Example Input
Input 1:
A = [1, 2, 3]
Input 2:
A = [5, 2, 1, 4]


Example Output
Output 1:
[[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
Output 2:
[[1 ], [1 4 ], [2 ], [2 1 ], [2 1 4 ], [4 ], [5 ], [5 2 ], [5 2 1 ], [5 2 1 4 ] ]
"""

def solve(A):
    result = []
    for i in range(len(A)):
        result.append([A[i]])
        for j in range(i+1, len(A)):
            # print all subarray from i to j
            temp =[]
            for k in range(i, j+1):
                temp.append(A[k])
            result.append(temp)
            j+=1
    return result

print(solve([1, 2, 3])) 
# [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]