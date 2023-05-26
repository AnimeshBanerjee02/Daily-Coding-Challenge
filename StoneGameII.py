from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {} 
        def dfs(i: int, m: int) -> int:
            if i >= n:
                return 0
            
            if (i, m) in memo:
                return memo[(i, m)]
            
            max_stones = float('-inf')  
            
            for x in range(1, min(2 * m + 1, n - i + 1)):
                max_stones = max(max_stones, sum(piles[i:i+x]) - dfs(i + x, max(m, x)))
            
            memo[(i, m)] = max_stones
            return max_stones
        
        return (sum(piles) + dfs(0, 1)) // 2
