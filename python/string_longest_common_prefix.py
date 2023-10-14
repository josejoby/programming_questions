"""
Problem Description
Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array.

The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".



Problem Constraints
0 <= sum of length of all strings <= 1000000



Input Format
The only argument given is an array of strings A.



Output Format
Return the longest common prefix of all strings in A.



Example Input
Input 1:

A = ["abcdefgh", "aefghijk", "abcefgh"]
Input 2:

A = ["abab", "ab", "abcd"];


Example Output
Output 1:

"a"
Output 2:

"ab"


Example Explanation
Explanation 1:

Longest common prefix of all the strings is "a".
Explanation 2:

Longest common prefix of all the strings is "ab".
"""

def longestCommonPrefix(A):
    A.sort()
    lcp=""
    for ch in A[0]:
        s=lcp+ch
        for i in range(1, len(A)):
            if A[i][0:len(s)] != s:
                return lcp                
        lcp=s
    return lcp
    
def longestCommonPrefix2(A):
        n = len(A)
        if n < 1:
            return ""
        prefix = A[0]
        prefixLen = len(prefix)
        for i in range(1, n):
            j = 0
            # finds the longest common prefix between A[i] and current prefix
            while j < min(prefixLen, len(A[i])):
                if prefix[j] != A[i][j]:
                    break
                j += 1
            if j < prefixLen:
                prefix = prefix[:j]
                prefixLen = j
        return prefix



print(longestCommonPrefix(["abcdefgh", "aefghijk", "abcefgh"])=="a")
print(longestCommonPrefix(["abab", "ab", "abcd"])=="ab")