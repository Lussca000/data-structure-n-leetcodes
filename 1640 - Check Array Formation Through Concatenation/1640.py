class Solution:
    def canFormArray(self, arr: list[int], pecas: list[list[int]]) -> bool:
        pecas_por_inicio = {}
        # 1. Guarda cada peça no dicionário
        for peca in pecas:
            pecas_por_inicio[peca[0]] = peca
        indice = 0

        # 2. Percorre o array original
        while indice < len(arr):
            numero = arr[indice]
            # 3. Verifica se existe uma peça que começa com esse número
            if numero not in pecas_por_inicio:
                return False
            peca = pecas_por_inicio[numero]

            # 4. Confere se a peça corresponde ao trecho do array
            trecho_arr = arr[indice:indice + len(peca)]
            if trecho_arr != peca:
                return False
            # 5. Avança pela quantidade de elementos da peça
            indice += len(peca)

        return True