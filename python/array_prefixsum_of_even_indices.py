


def prefix_array_of_even_indices(A):
    p=[A[0]] # 0 is considered as even index for this problem
    for i in range(1, len(A)):
        if i&1: # if i is odd, add previous prefix value
            p.append(p[i-1])
        else: # if i is even, compute new prefix value.
            p.append(p[i-1] + A[i])
    return p

print(prefix_array_of_even_indices([2,4,3,1,5])) # [2,2,5,5,10]