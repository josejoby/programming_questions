"""
Problem Constraints
1 <= A.size() <= 1000
1 <= A[i].size() <= 1000
1 <= A[i][j] <= 1000

Input Format
First argument is a 2D matrix of integers.

Output Format
You have to return the Transpose of this 2D matrix.
"""

def solve(A):
    result = [0]*len(A)
    for _ in range(len(result)):
        result[_] = []
    for j in range(len(A[0])):
        for i in range(len(A)):
            result[j].append(A[i][j])
    return result

def solve1(A):
    result = []
    for j in range(len(A[0])):
        temp = []
        for i in range(len(A)):
            temp.append(A[i][j])
        result.append(temp)
    return result

# print(solve([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))
print(solve([[1, 2],[1, 2],[1, 2]]))