

def brute_force(A):
    """
    tc: O(n^3), sc: O(1)
    """
    pass

def prefix_sum(A):
    """
    tc: O(n^2), sc: O(n)
    """
    pass

def carry_forward(A):
    """
    tc: O(n^2), sc: O(1)
    """
    totalsum=0
    for s in range(len(A)):
        currsum = 0 # store the sum of subarray starting from [s,e]
        for e in range(s, len(A)):
            currsum += A[e] # sum_of_subarray[s,e] = sum_of_subarray[s,e-1] + A[e]
            totalsum +=currsum # add sum_of_subarray[s,e] to totalsum
    return totalsum


def contribution_technique(A):
    """
    """
    pass


print(brute_force([1,2,3])) #20
print(prefix_sum([1,2,3])) #20
print(carry_forward([1,2,3])) #20