class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        palavra_s = {}
        palavra_t = {}
        for char in s:
            palavra_s[char] = palavra_s.get(char, 0) + 1
        for char in t:
            palavra_t[char] = palavra_t.get(char, 0) + 1
            
        return palavra_s == palavra_t