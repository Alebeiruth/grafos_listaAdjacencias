from collections import defaultdict

"""Alexandre, Diferentemente da matriz de adjacências, na lista de adjacências
não é preciso passar a quantidade de vértices para a instanciação do grafo.
Sugiro que remova do construtor da classe o parâmetro "numeroVertices".
Assim, é possível criar um grafo vazio G=Grafo() e ir adicionando vértices
e arestas de maneira incremental e sem a limitação da quantidade de
vértices inicial. No seu código atual, ao fazer G=Grafo(5) e não adicionar
nenhum vértice, o grafo terá ordem 5, o que está incorreto já que ele não
possui nenhum vértice. Também sugiro que você reveja o seu
método imprime_lista_adjacencias, pois a sua impressão está replicando a lista.
No exemplo apresentado no vídeo, somente as 3 últimas linhas deveriam ter sido
apresentadas."""

# u = vertice inicial/origem
# v = vertice final/destino

# criacao constructor da classe Grafos
class Grafo:
  def __init__(self):
    self.adjacente_list = defaultdict(list)

  """def __str__(self):
    return self.imprime_lista_adjacencias()"""

 # ponto a
 # funcao adciona vertice, faz o teste da existencia do mesmo,
 # cria a vertice
  def adiciona_vertice(self, u):
    if u not in self.adjacente_list:
      self.adjacente_list[u] = []

  # ponto b
  def adiciona_aresta(self, u, v, peso):
    # verifica a existencias de ambos vertices
    self.adiciona_vertice(u)
    self.adiciona_vertice(v)

    # adciona aresta e pondera a mesma
    self.adjacente_list[u].append((v, peso))

  # ponto c
  # remocao da aresta do vertice U para vertice V
  def remove_aresta(self, u, v):
    for i in range(len(self.adjacente_list[u])):
      if self.adjacente_list[u][i][0] == v:
        del self.adjacente_list[u][i]
        break

  # ponto d
  # retira todas as arestas que se direcionam para o vertice U
  def remove_vertice(self, u):
    for vertice, arestas in self.adjacente_list.items():
      arestas_verificadas = []
      for destino, peso in arestas:
        if destino != u:
          arestas_verificadas.append((destino, peso))
      self.adjacente_list[vertice] = arestas_verificadas

      if u in self.adjacente_list:
        del self.adjacente_list[u]

  # ponto e
  # faz a verificacao de arestas entre vertice U para vertice V
  def tem_aresta(self, u, v):
    for destino, _ in self.adjacente_list[u]:
      if destino == v:
        return True
    return False

  # ponto f
  def grau_entrada(self, u):
    count = 0
    # percorre todos vertices
    for vertice in self.adjacente_list:
      # percorre cada aresta do vertice
      for destino, _ in self.adjacente_list[vertice]:
        if destino == u:
          count += 1
    return count

  # ponto g
  def grau_saida(self, u):
    # grau de saida de U e o tamanho da lsita de adjancencias / GRAFO
    return len(self.adjacente_list[u])

  # ponto h
  def grau(self, u):
    grau_saida = len(self.adjacente_list[u])
    
    # contador do grau de entrada
    grau_ent = 0
    for vertice in self.adjacente_list:
      for destino, _ in self.adjacente_list[vertice]:
        if destino == u:
          grau_ent += 1
    # grau total e encontrado na somatoria dos graus de saida e entrada
    return grau_ent + grau_saida

  # ponto i
  def get_peso(self, u, v):
    # percorre toda lista do vertice U
    for destino, peso in self.adjacente_list[u]:
      # verifica se o destino da aresta e igual ao vertice V
      if destino == v:
        return peso
        # retorna o peso da aresta e caso nao encotre retorna None (excecao)
    return None
    

  # pont j
  def imprime_lista_adjacencias(self):
    # percorre cada vertice
    for vertice, arestas in self.adjacente_list.items():
      # informa a linha de impressao e nome do vertice
      line = f"{vertice}"
      # percorre cada aresta do vertice atual
      for destino, peso in arestas:
        # adciona a representacao da aresta a linha
        line += f"('{destino}', {peso}) -> "
      
      line = line.rstrip(" -> ") # remove o ultimo " -> "
      print(line)

g = Grafo()

"""g.adjacenteLista["Pedro"].append(("Maria",3))
g.adjacenteLista['Maria'].append(('Clara', 2))
g.adjacenteLista['Clara'].append(('Maria', 5))"""

g.adiciona_vertice("Pedro")
g.adiciona_vertice("Maria")
g.adiciona_vertice("Clara")

g.adiciona_aresta("Pedro", "Maria", 3)
g.adiciona_aresta("Maria", "Clara", 2)
g.adiciona_aresta("Clara", "Maria", 5)

g.imprime_lista_adjacencias()
