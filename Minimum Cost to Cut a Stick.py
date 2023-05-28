from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        cuts = [0] + sorted(cuts) + [n]
        
        
        dp = [[0] * len(cuts) for _ in range(len(cuts))]
        
        
        for length in range(2, len(cuts)):
            for start in range(len(cuts) - length):
                end = start + length
                dp[start][end] = float('inf')
                
                
                for k in range(start + 1, end):
                    dp[start][end] = min(dp[start][end], dp[start][k] + dp[k][end] + cuts[end] - cuts[start])
        
        return dp[0][len(cuts) - 1]
