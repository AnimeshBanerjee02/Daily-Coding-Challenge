class Solution:
    def countEven(self, num: int) -> int:
        # Define a helper function to compute the digit sum of a number
        def digitSum(n):
            return sum(int(d) for d in str(n))
        
        # Count the number of positive integers less than or equal to num
        # whose digit sums are even
        count = 0
        for i in range(1, num+1):
            if digitSum(i) % 2 == 0:
                count += 1
        
        return count