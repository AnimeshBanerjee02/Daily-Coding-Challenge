class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        p_dict = {}
        w_dict = {}
        
        for i in range(len(pattern)):
            if pattern[i] in p_dict:
                if p_dict[pattern[i]] != words[i]:
                    return False
            else:
                p_dict[pattern[i]] = words[i]
            
            if words[i] in w_dict:
                if w_dict[words[i]] != pattern[i]:
                    return False
            else:
                w_dict[words[i]] = pattern[i]
        
        return True
