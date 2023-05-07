class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}
        
        for i in range(len(s)):
            if s[i] in s_dict:
                if s_dict[s[i]] != t[i]:
                    return False
            else:
                s_dict[s[i]] = t[i]
            
            if t[i] in t_dict:
                if t_dict[t[i]] != s[i]:
                    return False
            else:
                t_dict[t[i]] = s[i]
        
        return True
