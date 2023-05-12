from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)
        dp[n-1] = questions[n-1][0]
        
        for i in range(n-2, -1, -1):
            points, brainpower = questions[i]
            dp[i] = points + dp[i + brainpower + 1] if i + brainpower + 1 < n else points
            dp[i] = max(dp[i], dp[i+1])
        
        return dp[0]
