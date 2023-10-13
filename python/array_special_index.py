
"""
index 'i' is a special index if sum of all elements to the right of i = sum of all elements to the left of i

[-3, 2, 4, -1] special index=> 1. (-3+2) == (-1)
[-7,1,5,2,-4,3,0] special index=>3 (-7+1+5)==(-4+3+0)


"""
def special_index(A): # didnt handle edge cases if any
    pf = [A[0]]
    n=len(A)
    lastidx = n-1
    for i in range(1, n):
        pf.append(pf[i-1]+A[i])
    for idx in range(1, lastidx): # iterating only till second last element.
        leftsum = pf[idx-1]
        rightsum=pf[lastidx]-pf[idx]
        if leftsum == rightsum:
            return idx
    return -1


def count_of_special_indices(A):
    l=len(A)
    cnt = 0
    pf=[None]*l
    pf[0] = A[0]
    for _ in range(1, l):
        pf[_] = pf[_-1]+A[_]
    for _ in range(l):
        leftsum=0
        rightsum=0
        if _ == 0:
            rightsum=pf[l-1]
        elif _+1 == l:
            leftsum=pf[_-1]
        else:
            leftsum = pf[_-1]
            rightsum = pf[l-1]-pf[_]
        if leftsum == rightsum:
            cnt+=1
    return cnt




# print(special_index([-3,2,4,1])) # -1
# print(special_index([-3,2,4,-1])) # 2
# print(special_index([-7,1,5,2,-4,3,0])) # 3

print(count_of_special_indices([2,1,6,4])) #1
print(count_of_special_indices([1,1,1])) #3
