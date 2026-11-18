class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        palavras = s.split()
        if len(pattern) != len(palavras):
            return False

        char_da_palavra = {}
        palavra_do_char = {}

        for char, palavras in zip(pattern, palavras):
            if char in char_da_palavra:
                if char_da_palavra[char] != palavras:
                    return False
            else:
                char_da_palavra[char] = palavras

            if palavras in palavra_do_char:
                if palavra_do_char[palavras] != char:
                    return False
            else:
                palavra_do_char[palavras] = char

        return True