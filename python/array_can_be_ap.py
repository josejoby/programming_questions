

def solve(A):
    A.sort()
    for i in range(1, len(A)-1):
        if A[i]-A[i-1] != A[i+1]-A[i]:
            return 0
    return 1

print(solve([3,5,1]))
print(solve([2, 4, 1]))
            