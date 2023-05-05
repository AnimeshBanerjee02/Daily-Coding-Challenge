class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Calculate the actual number of rotations needed
        k = k % len(nums)
        
        # Reverse the entire array
        nums.reverse()
        
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        
        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])
