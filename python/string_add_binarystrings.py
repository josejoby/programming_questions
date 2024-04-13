"""
Problem Description
Given two binary strings A and B. Return their sum (also a binary string).


Problem Constraints
1 <= length of A <= 105

1 <= length of B <= 105

A and B are binary strings



Input Format
The two argument A and B are binary strings.



Output Format
Return a binary string denoting the sum of A and B



Example Input
Input 1:
A = "100"
B = "11"
Input 2:
A = "110"
B = "10"


Example Output
Output 1:
"111"
Output 2:
"1000"


Example Explanation
For Input 1:
The sum of 100 and 11 is 111.
For Input 2:
 
The sum of 110 and 10 is 1000.

"""


def solve(A, B):
    s = ""
    l = max(len(A), len(B))
    A = A[::-1]
    B = B[::-1]
    carry = "0"
    for i in range(l):
        a = A[i] if i < len(A) else "0"
        b = B[i] if i < len(B) else "0"
        if a == "1" and b == "1":
            if carry == "1":
                t = "1"
                carry = "1"
            else:
                t = "0"
                carry = "1"
        elif (a == "0" and b == "1") or (b == "0" and a =="1" ):
            if carry == "1":
                t = "0"
                carry = "1"
            else:
                t = "1"
                carry = "0"
        else:
            if carry == "1":
                t = "1"
                carry = "0"
            elif carry == "0":
                t = "0"
                carry = "0"
        
        s += t
    if carry == "1":
        s+="1"
    s=s[::-1]
    return s


def get(x):
    if x == 0:
        return "0"
    if x == 1:
        return "1"
        
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        n = -len(A)
        m = -len(B)
        nm = min(n, m)
        carry = 0
        ans = ""
        # we add bits from the rightmost bit to the leftmost bit
        for i in range(-1, nm - 1, -1):
            if i >= n and i >= m:
                v = ord(A[i]) + ord(B[i]) - 2 * ord('0') + carry
                carry = v // 2
                v -= 2 * carry
                ans += get(v)
            elif i >= n:
                v = ord(A[i]) - ord('0') + carry
                carry = v // 2
                v -= 2 * carry
                ans += get(v)
            else:
                v = ord(B[i]) - ord('0') + carry
                carry = v // 2
                v -= 2 * carry
                ans += get(v)
        if carry == 1:
            ans += get(carry)
        return ans[::-1]


print(solve("100", "11") == "111")
print(solve("110", "10") == "1000")
print(solve("1010110111001101101000", "1000011011000000111100110") == "1001110001111010101001110")