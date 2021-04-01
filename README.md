# estrutura-de-dados
Repositório de curso de estruturas de dados com Python da [Python Pro](www.python.pro.br)

Link para playlist com todas vídeo aulas:
  https://www.youtube.com/watch?v=UvvFaNV68Xs&list=PLA05yVJtRWYS4mhKqJo_1bZqcetSGjDgU

Link do repositório original: 
 https://github.com/pythonprobr/estrutura-de-dados

Link do repositório antigo, de 2016, quando o curso foi ministrado na Fatec:
  https://github.com/renzon/estrutura-de-dados


**Contagem de Operação Primitivas -> tempo constante**

- focar sempore nos piores casos

- **função constante** : f(n) = c  -> c=5, c=28, c=2**10
  - independente do valor do X o valor Y sera sempre o mesmo
  - o melhor algoritmo
    
- **função logarithm** aquela que é inversa a exponencial
  - x = logb 1 == 0
  - log n == log2 n  -> esta explicito que log n deve ser considerado log de n na base 2
  - função chamada sub-linear porque é melhor que a função linear.
  - quando dobramos o valor de entrada vamos somar ao tempo de execução (valor de C) 
    somente somar mais um valor c
    
- **função linear**  -> f(n) = n 
  - o tempo de execução demora um tempo proporcional ao tamanho de entrada
  - duplicando o tempo de entrada duplica o tempo de execusão
  - Algoritmo que caiem com função linear:
    - calcular o max  
    - procurar um elemento em uma lista
    - calcular a mediana ou media
    
- **função N-log-N**  -> f(n) == nlog n
   - esta função é um pouco pior que a linear, ams ainda é uma solução boa
   - Algoritmo que caiem com função linear:
     - os bons algartimo de ordenação
     - 
    
- **função Quadratica**  -> f(n) == n ao quadrado
  - pior que a sub-line -> n ao quadrado
  - algortimo de ordenação ruim (bolb-sort, insert sort)
    
- **loop alinhados e função quadratica**- algoritmos quadraticos
    
- **função cubica** -> f(n) == n ao cubo
  - o que levamo sem consideração é o elemento que esta com o maoir espoente
    
- **função somatoria** -> que da n quadratico

- **função exponencial** -> f(n) == b elevado a n
  - a pior função
  - quando somamos 1 no elemento de entrada dobramos o tempo de execução
  - soma geometrica é um algoritmo exponencial
  - algoritmo caixeiro viajante
  - gerar todas as permutançoes de uma coleção
  - torre de hanoi
  - fibonatti qdo mal implementado é exponencial

- **Analysis Asymptotic**
  - qdo comparamos um algoritmo com outro, fazemos analise asymptotica
  - quando comparamos um algorimo  que ś soma de um função constante com um algortimo de 
    função logaritima, não interessa o algoritmo é logaritma

- **Notação Big-Oh**
  - é um analise desta funçoes onde normalmente vamos ter uma soma entre elas
  - a notação Big_oh é aquela que voce tem um valor de n e uma constante tal qual esta função
    é c de g(n) sempre será maior que f(n) para um determinado valor.
  - se temos um função 8n + 5 -> função constante e função linear. entao a pior 
