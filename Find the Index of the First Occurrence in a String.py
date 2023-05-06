class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if the needle is an empty string
        if not needle:
            return 0
        # Loop through the haystack string
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring of haystack starting at index i and of length len(needle) is equal to needle
            if haystack[i:i+len(needle)] == needle:
                # If it is, return the index i
                return i

        # If the needle was not found in the haystack, return -1
        return -1
