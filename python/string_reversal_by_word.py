"""
Problem Description
You are given a string A of size N.

Return the string A after reversing the string word by word.

NOTE:

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.


Problem Constraints
1 <= N <= 3 * 10^5



Input Format
The only argument given is string A.



Output Format
Return the string A after reversing the string word by word.



Example Input
Input 1:
A = "the sky is blue"
Input 2:
A = "this is ib"


Example Output
Output 1:
"blue is sky the"
Output 2:
"ib is this"    


Example Explanation
Explanation 1:
We reverse the string word by word so the string becomes "blue is sky the".
Explanation 2:
We reverse the string word by word so the string becomes "ib is this".

"""

def solve(A):
    l=[]
    word=""
    idx=0
    while idx<len(A):
        if A[idx]!=" ":
            word+=A[idx]
        elif word!="":
            l.append(word)
            word=""
        idx+=1
    if word!="": # add any remaining elements
        l.append(word)
    output = ""
    while len(l)>0:
        output+=l.pop()
        if len(l)>0:
            output+=" "
    return output
    

def solve2(A): # faster, pythonic soln
    A=A.strip()
    A=A.split()
    return ' '.join(A[::-1])


print(solve("this is ib")=="ib is this")
print(solve("the sky is blue")=="blue is sky the")
print(solve(" the sky is blue  ")=="blue is sky the")
print(solve(" the  sky is blue  ")=="blue is sky the")

print(solve2("this is ib")=="ib is this")
print(solve2("the sky is blue")=="blue is sky the")
print(solve2(" the sky is blue  ")=="blue is sky the")
print(solve2(" the  sky is blue  ")=="blue is sky the")