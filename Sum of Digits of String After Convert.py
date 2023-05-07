class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Replace each character with its corresponding alphabet position
        num_str = ''.join(str(ord(ch) - 96) for ch in s)
        
        # Repeat the transform operation k times
        for i in range(k):
            # Transform the integer by replacing it with the sum of its digits
            num = sum(int(ch) for ch in num_str)
            num_str = str(num)
        
        return int(num_str)