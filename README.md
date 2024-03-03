# RESOLUÇÃO DE PROBLEMAS COM GRAFOS

## Getting Started

Em Python, crie uma classe “Grafo” que permita a criação de um grafo G direcionado,
rotulado e ponderado utilizando a representação de LISTA DE ADJACÊNCIAS (ADJACENCY LIST).
Diferentemente da matriz de adjacências, em que é preciso criar um grafo inicial com uma
quantidade pré-definida de vértices, o grafo utilizando lista de adjacências deve ser
criado inicialmente vazio e os vértices são adicionados incrementalmente.

### Prerequisites

Pré requisto, saber a linguagem de programação Python e Grafos

* You need this
* And you need this
* Oh, and don't forget this

### Explanation

u == vertice inicial 
v == vertice final
peso == valor associado a aresta que conectqa u ao v
self = permite que os metodos aceese e modifique os atributos de Grafo
1. **Importação e Classe:**
   - Importamos `defaultdict` da biblioteca `collections`. Isso nos ajuda a criar dicionários que têm um valor padrão se a chave ainda não existir.
   - Definimos uma classe chamada `Grafo`.

2. **Construtor (`__init__`):**
   - Quando criamos um novo `Grafo`, especificamos o número de vértices (`numeroVertices`). Inicializamos a `ordem` do grafo com esse número, `tamanho` (número de arestas) como 0, e `adjacenteLista`, que é um `defaultdict` contendo listas, para armazenar as arestas.

3. **Adicionando Vértices (`adiciona_vertice`):**
   - Se um vértice `u` não estiver presente em `adjacenteLista`, nós o adicionamos com uma lista vazia como valor. Isso significa que o vértice `u` ainda não tem arestas conectadas. A `ordem` do grafo é aumentada em 1.

4. **Adicionando Arestas (`adiciona_aresta`):**
   - Para adicionar uma aresta, verificamos se `u` e `v` existem. Se não existirem, eles são adicionados. Depois, adicionamos uma tupla `(v, peso)` à lista de `u` em `adjacenteLista`, indicando uma aresta de `u` para `v` com certo `peso`. O `tamanho` do grafo é aumentado em 1.

5. **Removendo Arestas (`remove_aresta`):**
   - Para remover uma aresta de `u` para `v`, procuramos por `v` na lista de `u` e a removemos se encontrada. O `tamanho` do grafo é diminuído em 1.

6. **Removendo Vértices (`remove_vertice`):**
   - Para remover um vértice `u`, removemos `u` e sua lista de `adjacenteLista`. Então, iteramos sobre todos os vértices restantes para remover qualquer aresta que aponte para `u`. A `ordem` do grafo é diminuída em 1, e o `tamanho` é ajustado para refletir as arestas removidas.

7. **Verificando Arestas (`tem_aresta`):**
   - Verificamos se existe uma aresta de `u` para `v` procurando por `v` na lista de `u`. Se encontrada, retornamos `True`; caso contrário, `False`.

8. **Grau de Entrada (`grau_entrada`):**
   - Calculamos o grau de entrada de `u` contando quantas vezes `u` aparece como destino nas listas de todos os vértices.

9. **Grau de Saída (`grau_saida`):**
   - O grau de saída de `u` é simplesmente o tamanho da lista de `u` em `adjacenteLista`.

10. **Grau Total (`grau`):**
    - O grau total de `u` é a soma do grau de entrada e do grau de saída.

11. **Peso da Aresta (`get_peso`):**
    - Para encontrar o peso de uma aresta de `u` para `v`, procuramos por `v` na lista de `u` e retornamos o peso associado se a aresta for encontrada.

12. **Imprimindo Lista de Adjacências (`imprime_lista_adjacencias`):**
    - Iteramos sobre cada vértice e suas arestas em `adjacenteLista`, formatando e imprimindo a lista de adjacências de cada vértice.

13. **Uso da Classe:**
    - Criamos uma instância da classe `Grafo`, adicionamos vértices e arestas usando os métodos definidos, e então chamamos `imprime_lista_adjacencias` para ver a lista de adjacências do grafo.

O código segue a lógica descrita acima para manipular grafos, permitindo adicionar e remover vértices e arestas, além de consultar informações sobre o grafo, como a existência de arestas e os graus dos vértices.

## Usage

Nos demais titulos deixarei o texto original desse modelo de README

```
$ First example
$ Second example
$ And keep this in mind
```

## Deployment

Additional notes on how to deploy this on a live or release system. Explaining the most important branches, what pipelines they trigger and how to update the database (if anything special).

### Server

* Live:
* Release:
* Development:

### Branches

* Master:
* Feature:
* Bugfix:
* etc...

## Additional Documentation and Acknowledgments

* Project folder on server:
* Confluence link:
* Asana board:
* etc...
