"""

Problem Description
Given two integer arrays, A and B of size N and M, respectively. Your task is to find all the common elements in both the array.

NOTE:

Each element in the result should appear as many times as it appears in both arrays.
The result can be in any order.


Problem Constraints
1 <= N, M <= 105

1 <= A[i] <= 109



Input Format
First argument is an integer array A of size N.

Second argument is an integer array B of size M.



Output Format
Return an integer array denoting the common elements.



Example Input
Input 1:

 A = [1, 2, 2, 1]
 B = [2, 3, 1, 2]
Input 2:

 A = [2, 1, 4, 10]
 B = [3, 6, 2, 10, 10]


Example Output
Output 1:

 [1, 2, 2]
Output 2:

 [2, 10]


Example Explanation
Explanation 1:

 Elements (1, 2, 2) appears in both the array. Note 2 appears twice in both the array.
Explantion 2:

 Elements (2, 10) appears in both the array.
 """

def solve(A,B):
    # d1={}
    # d2={}
    # result=[]
    # for x in A:
    #     d1[x] = 1 if x not in d1 else d1[x]+1
    # for x in B:
    #     d2[x] = 1 if x not in d2 else d2[x]+1
    # if len(d1)>=len(d2):
    #     a=d1
    #     b=d2
    # else:
    #     a=d2
    #     b=d1
    # for k,v in a.items():
    #     if k in b:
    #         for _ in range(min(v,b[k])):
    #             result.append(k)
    # return result

    n = len(A)
    m = len(B)
    hashmap = {}
    for i in range(n):
        if(hashmap.get(A[i]) == None):
            hashmap[A[i]] = 1
        else:
            hashmap[A[i]] += 1
    
    ans =[] 
    for i in range(m):
        if(hashmap.get(B[i]) != None and hashmap[B[i]] != 0):
            ans.append(B[i])
            hashmap[B[i]] -= 1
        
    return ans

print(solve([1, 2, 2, 1],[2, 3, 1, 2]).sort() == [1, 2, 2].sort())
print(solve([2, 1, 4, 10],[3, 6, 2, 10, 10]).sort()== [2,10].sort())

