class Solution:
    def uniqueocorrencias(self, arr: list[int]) -> bool:
        contador = {}
        for num in arr:
            contador[num] = contador.get(num, 0) + 1
        ocorrencias = set(contador.values())
        return len(ocorrencias) == len(contador)