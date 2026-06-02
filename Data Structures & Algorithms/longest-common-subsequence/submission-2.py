class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if m > i >= 0 and n > j >= 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) 
                
                    if text1[i] == text2[j]:
                        dp[i][j] = dp[i - 1][j - 1] + 1

                
                print(f"{i}, {j}, {text1[i]} {text2[j]} {dp[i][j]}")

        return dp[-2][-2]


        