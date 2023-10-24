"""
Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1's that can be achieved.


Input Format

The only argument given is string A.
Output Format

Return the length of the longest consecutive 1's that can be achieved.
Constraints

1 <= length of string <= 1000000
A contains only characters 0 and 1.
For Example

Input 1:
    A = "111000"
Output 1:
    3

Input 2:
    A = "111011101"
Output 2:
    7
"""

def solve(A):
    leftarr = [0]*len(A)
    rightarr = [0]*len(A)
    count_of_ones = 0

    # get the total count of ones
    for x in A:
        if x =='1':
            count_of_ones+=1
    if count_of_ones == len(A):
        return count_of_ones
    # compute the left cumulative sum arr
    for i in range(len(A)):
        if i==0 and A[i]=='1':
            leftarr[i] = 1
        elif A[i]=='1':
            leftarr[i] = leftarr[i-1]+1
        elif A[i] == '0':
            leftarr[i] = 0
    # compute the right cumulative sum arr
    for i in range(len(A)-1, -1, -1):
        if i==len(A)-1 and A[i]=='1':
            rightarr[i] = 1
        elif A[i]=='1':
            rightarr[i] = rightarr[i+1]+1
        elif A[i] == '0':
            rightarr[i] = 0
    
    # find the longest consecutive substring
    result = 0
    for i in range(len(A)):
        if A[i] == '0': #check if the character is '0'
            # handle edge cases - ends of the string
            if i == 0:
                s = rightarr[i+1]
            elif i == len(A)-1:
                s = leftarr[i-1]
            else:
                s = leftarr[i-1]+rightarr[i+1]
            if s == count_of_ones: # there are no other 1s in the substring and all '1's are near to A[i]. Swapping will happen only with the neighbouring '1's
                result = max(result, s)
            else: # there are 1s which are not near A[i]. We can swap that 1 with A[i] which will increase the number of 1s in the string by 1
                result = max(result, s+1)
    return result
    

        
    





print(solve("111000")==3)
print(solve("111011101")==7)
print(solve("111")==3)
print(solve("000")==0)
print(solve("01")==1)