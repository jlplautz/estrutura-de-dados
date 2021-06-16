# Como fazer ordenação em Python do jeito certo!

## Definição:
  - qual o problema da ordenação
  - quais as propriedades matemáticas importantes
  - Propriedade Transitiva
    a < b e B < c => a < c
    1 < 2 e 2 < 3 => 1 < 3
    < menor => implica
    
  - Algoritmo de ordenação estavel - quando ocorre um empate o algortimo mantem a ordenação original
  -  decorator @total_ordering
    - tendo dois métodos implementados __gt__ e __eq__ o decorator @total_ordering resolve os demais.

## Contrato
  - que precisa ser definido para poder ordenar uma coleção de objetos.
  - Diferença sort ou Sorted
    - Sorted - adjetivo  -> sorted(numeros) -> é uma função -> gera uma nova lista 
    - SORT   - Verbo     -> numeros.sort    -> é um metodo  -> ordena a mesma lista 
      - o resultado da ordenação com método SORT é NONE, pois o método sort altera o próprio objeto
      - SORT não vai gastar mais memoria O(1) para memoria
    - quando usamos o SORT ou o SORTED
      - SORT   -> quando não tem problema perder a ordem original da lista (não vai gastar memoria)
      - Sorted -> quando não queremos perder a ordem da lista  (faz copia da lista - gasta mais memoria )
    - shuffle() -> embaralhar os elementos da lista
    
## Análise
  - de complexidade em tempo e espaço
  - mencionar quais são as análises dos principais algoritmos

## Importante
  - O custo 
    - os algortimo ordenação os bons tem custo O n logn
                             os ruins tem custo o n2
    - função e metodo
      - SORTED função biltin do python
      - Metodo SORT da list
        
    - saber o contrato para poder usar o algoritmo generico de ordenação
    - Ordenação de tuplas com > ou = com multiplos critérios de ordenação

## Qual o algoritmo de ordenação no Python 
  - link -> http://pythonclub.com.br/algoritmos-ordenacao.html
  - Timsort é um algoritmo de ordenação híbrido derivado do merge sort e do insertion sort, 
    projetado para ter boa performance em vários tipos de dados do mundo real. 
    Foi inventado por **Tim Peters** em 2002 para ser usado na linguagem de programação Python, 
    e tem sido o algoritmo de ordenação padrão de Python desde a versão 2.3
    

## Desafio insertion sort

  - Interar sobre os elementos procurando o indice do elemento com o menor valor minimo (min),
    quando localizado fazer o swuap do indice do menor valor para o indice 0
  - Remover min e colocar como ultimo elemento da lista ordenada
