# 49. Group anagramas leetcode

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramas = {}
        for palavra in strs:
            palavra_sortida = ''.join(sorted(palavra))
            if palavra_sortida not in anagramas:
                anagramas[palavra_sortida] = []
            anagramas[palavra_sortida].append(palavra)
        return list(anagramas.values())