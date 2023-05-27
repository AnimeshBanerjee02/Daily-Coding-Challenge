class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * (n + 1)  

        dp[n] = 0  

        for i in range(n - 1, -1, -1):
            max_score_diff = float('-inf')

            
            for j in range(1, 4):
                if i + j <= n:
                    curr_score_diff = sum(stoneValue[i:i + j]) - dp[i + j]
                    max_score_diff = max(max_score_diff, curr_score_diff)

            dp[i] = max_score_diff

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
