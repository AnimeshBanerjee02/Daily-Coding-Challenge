class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        
        word = ''.join([' ' if not c.isdigit() else c for c in word])
        gers
        nums = [int(n) for n in word.split()]
        
        return len(set(nums))
