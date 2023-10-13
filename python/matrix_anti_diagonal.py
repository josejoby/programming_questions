"""
Problem Description
Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.


Problem Constraints
1<= N <= 1000
1<= A[i][j] <= 1e9


Input Format
Only argument is a 2D array A of size N * N.


Output Format
Return a 2D integer array of size (2 * N-1) * N, representing the anti-diagonals of input array A.
The vacant spaces in the grid should be assigned to 0.


Example Input
Input 1:
1 2 3
4 5 6
7 8 9
Input 2:

1 2
3 4


Example Output
Output 1:
1 0 0
2 4 0
3 5 7
6 8 0
9 0 0
Output 2:

1 0
2 3
4 0


Example Explanation
For input 1:
The first anti diagonal of the matrix is [1 ], the rest spaces shoud be filled with 0 making the row as [1, 0, 0].
The second anti diagonal of the matrix is [2, 4 ], the rest spaces shoud be filled with 0 making the row as [2, 4, 0].
The third anti diagonal of the matrix is [3, 5, 7 ], the rest spaces shoud be filled with 0 making the row as [3, 5, 7].
The fourth anti diagonal of the matrix is [6, 8 ], the rest spaces shoud be filled with 0 making the row as [6, 8, 0].
The fifth anti diagonal of the matrix is [9 ], the rest spaces shoud be filled with 0 making the row as [9, 0, 0].
For input 2:

The first anti diagonal of the matrix is [1 ], the rest spaces shoud be filled with 0 making the row as [1, 0, 0].
The second anti diagonal of the matrix is [2, 4 ], the rest spaces shoud be filled with 0 making the row as [2, 4, 0].
The third anti diagonal of the matrix is [3, 0, 0 ], the rest spaces shoud be filled with 0 making the row as [3, 0, 0].
"""
def print_diagonal_pos(A):
    n=len(A) # row count
    m= len(A[0]) # colmn count
    for top in range(m+2):
        i=0
        j=top
        while i < n and j > -1:
            if j < m:
                print(f"({i}, {j})", end=" ")
            i+=1
            j-=1
        print(end="\n")


def brute_soln(A):
    output = []
    n=len(A)
    m=len(A[0])
    for top in range(m+n):
        temp = []
        i=0
        j=top
        while i<n and j>-1:
            if j<m:
                temp.append(A[i][j])
            i+=1
            j-=1
        while 0<len(temp)<m: # adding placeholder values
                temp.append(0)
        if len(temp)>0:
            output.append(temp)
    return output

                

def optimal_soln1(A):
    """
    optimal soln for N*N matrix
    total_diagonal_count = len(A)+len(A[0]) -1 = 2*N-1
    """
    N = len(A)
    total_diagonal_count = 2*N-1
    # creating the output matrix
    result = [0] * total_diagonal_count
    for _ in range(total_diagonal_count):
        result[_] = []
    for i in range(N):
        for j in range(N):
            result[i+j].append(A[i][j])
    for diagonal in range(total_diagonal_count):
        while len(result[diagonal]) < N:
            result[diagonal].append(0)
    return result


    


# print(print_diagonal_pos([[1,2], [3,4]]))
# print(print_diagonal_pos([[1,2,3],[4,5,6],[7,8,9]]))


print(brute_soln([[1,2], [3,4]]))
print(brute_soln([[1,2,3],[4,5,6],[7,8,9]]))
print(brute_soln([[2,3,6,7],[2,3,4,5]]))
print(brute_soln([[3,7,7,1],[8,4,15,1],[13,5,8,5],[11,6,8,7]]))

print(optimal_soln1([[1,2], [3,4]]))
print(optimal_soln1([[1,2,3],[4,5,6],[7,8,9]]))
# print(optimal_soln1([[2,3,6,7],[2,3,4,5]])) # this will fail
print(optimal_soln1([[3,7,7,1],[8,4,15,1],[13,5,8,5],[11,6,8,7]]))