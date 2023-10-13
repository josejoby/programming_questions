"""
Problem Description
You have given a string A having Uppercase English letters.

You have to find how many times subsequence "AG" is there in the given string.

NOTE: Return the answer modulo 109 + 7 as the answer can be very large.



Problem Constraints
1 <= length(A) <= 105



Input Format
First and only argument is a string A.



Output Format
Return an integer denoting the answer.



Example Input
Input 1:

 A = "ABCGAG"
Input 2:

 A = "GAB"


Example Output
Output 1:

 3
Output 2:

 0


Example Explanation
Explanation 1:

 Subsequence "AG" is 3 times in given string 
Explanation 2:

 There is no subsequence "AG" in the given string.
 """
# approach 1
def carry_backward(s):
    g_count = 0
    ag_count = 0
    for i in range(len(s)-1, -1, -1):
        if s[i]=='g':
            g_count+=1
        elif s[i] == 'a':
            ag_count = ag_count + g_count
    return ag_count

# approach 2
def carry_forward(s):
    """
    i
    0   a=1 ag=0
    3   a=1 ag=1 - found g
    4   a=2 ag=1
    5   a=2 ag=ag+a_count - found g
    """
    ag_count = 0
    a_count = 0
    for i in range(len(s)):
        if s[i] == 'a':
            a_count +=1
        elif s[i] == 'g':
            ag_count=ag_count+a_count
    return ag_count

print(carry_backward(['a','b','e','g','a','g']))
print(carry_forward(['a','b','e','g','a','g']))

print(carry_backward(['a', 'd', 'g','a','g','a','g','f','g']))
print(carry_forward(['a', 'd', 'g','a','g','a','g','f','g']))
