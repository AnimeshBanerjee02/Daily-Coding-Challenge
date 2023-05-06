class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        start = 0
        longest = 0
        for i in range(len(s)):
            if s[i] in last_seen and last_seen[s[i]] >= start:
                start = last_seen[s[i]] + 1
            last_seen[s[i]] = i
            longest = max(longest, i - start + 1)
    
        return longest
