class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        if (len(s) != len(t)):
            return False # not an anagram by default
        
        for i in range(len(s)):
            dict_s[s[i]] = dict_s.get(s[i], 0) + 1
            dict_t[t[i]] = dict_t.get(t[i], 0) + 1
    
        for char in s:
            if dict_s.get(char) != dict_t.get(char):
                return False
        
        return True

        
        