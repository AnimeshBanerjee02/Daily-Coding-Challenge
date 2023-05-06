class Solution:
    def reverse(self, x: int) -> int:
        # Initialize the result variable
        result = 0
        # Determine if the number is negative
        negative = x < 0

        # Convert the number to a positive integer
        x = abs(x)

        # Reverse the digits of the number
        while x > 0:
            # Add the next digit to the result
            result = result * 10 + x % 10
            # Remove the last digit from the number
            x //= 10

        # If the original number was negative, make the result negative
        if negative:
            result = -result

        # Check if the result is within the 32-bit integer range
        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result
