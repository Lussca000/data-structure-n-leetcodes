from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, numeros: list[int], quantidade: int) -> int:

        def contar_no_maximo(limite: int) -> int:
            if limite < 0:
                return 0

            frequencia = defaultdict(int)
            esquerda = 0
            total = 0

            for direita, numero in enumerate(numeros):
                # Adiciona o número atual à janela
                frequencia[numero] += 1

                # Se houver números distintos demais, diminui a janela
                while len(frequencia) > limite:
                    numero_esquerda = numeros[esquerda]
                    frequencia[numero_esquerda] -= 1

                    # Remove o número do dicionário quando sua frequência chega a zero
                    if frequencia[numero_esquerda] == 0:
                        del frequencia[numero_esquerda]

                    esquerda += 1

                # Conta os subarrays que terminam na posição direita
                total += direita - esquerda + 1

            return total

        # Exatamente K = no máximo K - no máximo K-1
        return (
            contar_no_maximo(quantidade)
            - contar_no_maximo(quantidade - 1)
        )