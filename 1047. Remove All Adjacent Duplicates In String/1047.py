class Solution:
    def removeDuplicates(self, s: str) -> str:
        pilha = []

        for letra in s:
            if pilha and pilha[-1] == letra:
                pilha.pop()
            else:
                pilha.append(letra)

        return "".join(pilha)