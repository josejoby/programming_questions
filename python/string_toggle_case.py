"""
Problem Description
You are given a character string A having length N, consisting of only lowercase and uppercase latin letters.

You have to toggle case of each character of string A. For e.g 'A' is changed to 'a', 'e' is changed to 'E', etc.



Problem Constraints
1 <= N <= 10^5

A[i] ∈ ['a'-'z', 'A'-'Z']



Input Format
First and only argument is a character string A.



Output Format
Return a character string.



Example Input
Input 1:

 A = "Hello" 
Input 2:

 A = "tHiSiSaStRiNg" 


Example Output
Output 1:

 hELLO 
Output 2:

 ThIsIsAsTrInG 


Example Explanation
Explanation 1:

 'H' changes to 'h'
 'e' changes to 'E'
 'l' changes to 'L'
 'l' changes to 'L'
 'o' changes to 'O'
Explanation 2:

 "tHiSiSaStRiNg" changes to "ThIsIsAsTrInG".
"""


def solve(A):
    output=[]
    for idx in range(len(A)):
        o = ord(A[idx])
        if ord('a')<=o<=ord('z'):
            output.append(chr(o-32))
        elif ord('A')<=o<=ord('Z'):
            output.append(chr(o+32))
    return "".join(output)

def solve2(A):
    output=""
    for c in A:
        if c>='A' and c<='Z':
            output+=chr(ord(c)+32)
        elif c>='a' and c<='z':
            output+=chr(ord(c)-32)
    return output


print(solve("Hello"),solve("Hello")=="hELLO")
print(solve("tHiSiSaStRiNg"), solve("tHiSiSaStRiNg")=="ThIsIsAsTrInG")

print(solve2("Hello"),solve2("Hello")=="hELLO")
print(solve2("tHiSiSaStRiNg"), solve2("tHiSiSaStRiNg")=="ThIsIsAsTrInG")