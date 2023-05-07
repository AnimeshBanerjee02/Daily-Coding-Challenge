from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.searchLeft(nums, target)
        right = self.searchRight(nums, target)
        return [left, right]
    
    def searchLeft(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left if left < len(nums) and nums[left] == target else -1
    
    def searchRight(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right if right >= 0 and nums[right] == target else -1
