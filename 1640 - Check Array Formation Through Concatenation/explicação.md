pecas_por_inicio = {}

for peca in pecas:
    pecas_por_inicio[peca[0]] = peca

# serve pra adicionar num dict
----------------------------------------
indice = 0

while indice < len(arr):

# aumenta o indice enquanto for menor q o array

----------------------------------------

numero = arr[indice]

# o indice vale 0 e o numero vale 91 por exemplo, que era uma das validações

if numero not in pecas_por_inicio:
    return False

# como 91 existe entao achamos a peca [91]

peca = pecas_por_inicio[numero]

# Se não existisse uma peça começando pelo número atual, retornaria False, pois não conseguiriamos continuar formando o array naquela posição

----------------------------------------
trecho_arr = arr[indice:indice + len(peca)]

if trecho_arr != peca:
    return False

# Agora comparamos a peça encontrada com o trecho do array que deveria ocupar.

----------------------------------------

Na primeira volta:
trecho_arr = [91]
peca = [91]
Os dois são iguais. Então continuamos.
# Na segunda volta, indice será 1, e encontraremos a peça [4, 64].
# O trecho do array também será [4, 64], portanto a validação passa novamente.
# Essa comparação é importante porque encontrar uma peça com o primeiro número correto não garante que todos os elementos seguintes estejam na ordem correta.

----------------------------------------

indice += len(peca)
# vai avançando

----------------------------------------

# Quando indice chega a 4, temos indice == len(arr). O while termina e a função retorna True.
return True
# Isso significa que conseguimos percorrer e validar todo o array.

----------------------------------------

## São três conceitos que trabalham juntos:

for: percorre as peças para montar o dicionário.
while: percorre o array original, avançando conforme o tamanho de cada peça.
Dicionário: permite encontrar rapidamente qual peça começa com o número atual.

# A complexidade de tempo é O(n), considerando n como a quantidade de números em arr, pois cada peça é registrada uma vez e o array é percorrido sem voltar às posições anteriores. O segredo não é testar todas as combinações de peças. É aproveitar o primeiro número de cada peça para localizar a peça certa e depois verificar se ela corresponde ao trecho esperado do array.