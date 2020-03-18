"""
LIS: Longest Increasing Subsequeunce. Returns the length of the 
longest increasing subsequence

Example:
    arr: [3, 10, 2, 1, 20]
    output: 3

    arr: [50, 3, 10, 7, 40, 80]
    output: 4

Reference: https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
"""

def lis(arr):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    n = len(arr)
    dp = [1 for i in range(n)]

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] <  dp[j] + 1:
                dp[i] = dp[j] + 1

    longest_subsequence_len = None
    for val in dp:
        if longest_subsequence_len is None or longest_subsequence_len <  val:
            longest_subsequence_len = val
    return longest_subsequence_len


if __name__ == "__main__":
    arr= [50, 3, 10, 7, 40, 80]
    expected_output = 4
    output = lis(arr)
    print(f'Array: {arr},\nExpected Output: {expected_output}, Output: {output}')