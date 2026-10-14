## A função calcula 2 coisas

contar_no_maximo(2) > subarrays com 2 distintos
contar_no_maximo(1) > subarrays com 1 distinto

frequencia[numero] += 1 ----- controla a frequencia 
while len(frequencia) > limite: ----- ajusat a janela
total += direita - esquerda + 1 ----- conta os subarrays

soma a quantidade de subarrays válidos que terminam na posição atual, sem precisar criar cada subarray individualmente.
A complexidade é O(n) em tempo, pq cada elemento entra e sai da janela no máximo uma vez em cada execução da função auxiliar.
A ideia central é: primeiro aprendemos a contar subarrays com no máximo uma quantidade de números distintos; depois fazemos uma subtração para encontrar aqueles com a quantidade exata.