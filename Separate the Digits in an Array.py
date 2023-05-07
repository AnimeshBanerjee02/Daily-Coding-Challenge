class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        # Convert integers to strings and concatenate
        num_str = ''.join(map(str, nums))
        # Split into individual characters and convert back to integers
        separated_digits = list(map(int, num_str))
        return separated_digits
