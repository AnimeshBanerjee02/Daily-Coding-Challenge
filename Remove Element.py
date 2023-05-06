class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            # Initialize two pointers i and j
            i = 0
            j = 0
            # Loop through the array
            while j < len(nums):
                # If the current element is not equal to val
                if nums[j] != val:
                    # Move the current element to the ith position
                    nums[i] = nums[j]
                    # Increment the ith pointer
                    i += 1
                # Increment the jth pointer
                j += 1

            # Return the number of elements which are not equal to val
            return i
