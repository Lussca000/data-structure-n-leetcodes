class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letra_s = {}
        letra_t = {}

        for i in range(len(s)):
            if s[i] not in letra_s:
                letra_s[s[i]] = t[i]
            else:
                if letra_s[s[i]] != t[i]:
                    return False

            if t[i] not in letra_t:
                letra_t[t[i]] = s[i]
            else:
                if letra_t[t[i]] != s[i]:
                    return False
        return True