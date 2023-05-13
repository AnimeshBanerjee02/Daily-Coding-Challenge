
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
   
        dp = [1] + [0] * high
            
        for length in range(1, high+1):
            
            num_good_strings = 0
            if length >= zero:
                num_good_strings += dp[length-zero]
            if length >= one:
                num_good_strings += dp[length-one]
            dp[length] = num_good_strings % (10**9+7)

        
        return sum(dp[low:high+1]) % (10**9+7)
