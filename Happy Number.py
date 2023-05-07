class Solution:
    def isHappy(self, n: int) -> bool:
        c= set()
        while n not in c:
            c.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1
