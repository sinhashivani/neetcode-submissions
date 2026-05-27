class Solution: 
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        
        dp = [[] for _ in range(n + 1)]
        dp[1] = ["()"]

        for i in range(2, n + 1):
            new_vals = set()
            for prev_str in dp[i - 1]:
                new_vals.add("()" + prev_str)
                new_vals.add("(" + prev_str + ")")
                new_vals.add(prev_str + "()")
            
            # This basic approach misses cases like "(())()()" for higher n,
            # but for n <= 3 it works. To fix logic for n up to 7:
            for j in range(1, i):
                for left in dp[j]:
                    for right in dp[i - j]:
                        new_vals.add(left + right)
                #new_vals.add(dp[i - 1][j] + "()")

            dp[i] = list(new_vals)

        return dp[-1]


        