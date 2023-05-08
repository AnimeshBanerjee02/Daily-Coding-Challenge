class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        for i in range(n):
            j = abs(nums[i]) - 1
            if j < n and nums[j] > 0:
                nums[j] = -nums[j]
        
       
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        
        return n + 1
