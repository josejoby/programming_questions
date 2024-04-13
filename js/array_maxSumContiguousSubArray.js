/* 
Problem Description
Find the maximum sum of contiguous non-empty subarray within an array A of length N.



Problem Constraints
1 <= N <= 1e6
-1000 <= A[i] <= 1000



Input Format
The first and the only argument contains an integer array, A.



Output Format
Return an integer representing the maximum possible sum of the contiguous subarray.



Example Input
Input 1:

 A = [1, 2, 3, 4, -10] 
Input 2:

 A = [-2,  1, -3, 4, -1, 2, 1, -5, 4 ] 

Example Output
Output 1:

 10 
Output 2:

 6 
*/

function sumOfSubArrayLenK(A, K) {
    // assume K < A.length

    let s = 0;
    let e = 0;

    let windowSum = 0;
    while (e < K) {
        windowSum = windowSum + A[e]
        e++;
    }
    console.log("windowusm ", windowSum);
    let maxSum = windowSum;
    while (e < A.length) {
        windowSum = windowSum - A[s] + A[e]
        maxSum = Math.max(maxSum, windowSum)
        s++;
        e++
    }
    return maxSum;
}

// TLE
function maxSumSubArraySlidingWindow(A){
    if (A.length == 1) {
        return A[0]
    }

    let K=1;
    let maxSubArrSum=-Infinity
    while (K < A.length) {
        maxSubArrSum = Math.max(maxSubArrSum, sumOfSubArrayLenK(A, K));
        K++;
    }
    return maxSubArrSum;
}


console.log(solve(-500));
// console.log(solve([1, 2, 3, 4, -10]));
// console.log(solve([-2,  1, -3, 4, -1, 2, 1, -5, 4 ] ));
