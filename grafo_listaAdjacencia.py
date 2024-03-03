from collections import defaultdict

class Grafo:
  #construtor da classe com atributos ordem, tamanho e lista adjacente
  def __init__(self, numeroVertices):
    self.ordem = numeroVertices
    self.tamanho = 0
    self.adjacenteLista = defaultdict(list) 

  """def __str__(self):
    return self.imprime_lista_adjacencias()"""

 # ponto a
  def adiciona_vertice(self, u):
    if u not in self.adjacenteLista:
      self.adjacenteLista[u] = []
      self.ordem += 1

  # ponto b
  def adiciona_aresta(self, u, v, peso):
    if u not in self.adjacenteLista:
      self.adjacenteLista[u]
    if v not in self.adjacenteLista:
      self.adjacenteLista[v]

    self.adjacenteLista[u].append((v, peso))
    self.tamanho += 1
    
  
  # ponto c
  def remove_aresta(self, u, v):
      if u in self.adjacenteLista:
        for i, (destino, peso) in enumerate(self.adjacenteLista[u]):
          if destino == v:
            del self.adjacenteLista[u][i]
            self.tamanho -= 1
            print(f"Aresta de {u} para {v} removida com sucesso.")
            return
      print(f"Aresta de {u} para {v} não encontrada.")
      
  
  # ponto 
  def remove_vertice(self, u):
      if u not in self.adjacenteLista:
        print(f"Vertice {u} não se encontra.")
        return

      removidaAresta = len(self.adjacenteLista[u])
      del self.adjacenteLista[u]

      for v in list(self.adjacenteLista):
        removidaAresta += sum([1 for destino, _ in self.adjacenteLista[v] if destino == u])
        self.adjacenteLista[v] = [(destino, peso) for destino, peso in self.adjacenteLista[v] if destino != u]
      
      self.ordem -= 1
      self.tamanho -= removidaAresta
      print(f"Vertice {u} e suas arestas foram removidas")

  # ponto e
  def tem_aresta(self, u, v):
    if u in self.adjacenteLista:
      for destino, _ in self.adjacenteLista[u]:
        if destino == v:
          return True
    return False

  # ponto f
  def grau_entrada(self, u):
    grau_entrada = 0
    for i in self.adjacenteLista:
      for destino, _ in self.adjacenteLista[i]:
        if destino == u:
          grau_entrada += 1
    return grau_entrada

  # ponto g
  def grau_saida(self, u):
    if u in self.adjacenteLista:
      return len(self.adjacenteLista[u])
    return 0

  # ponto h
  def grau(self, u):
    return self.grau_entrada(u) + self.grau_saida(u)

  # ponto i
  def get_peso(self, u, v):
    if u not in self.adjacenteLista:
      print(f"Vertice {u} não existente")
      return None
    for destino, peso in self.adjacenteLista[u]:
      if destino == v:
        return peso
    
    print(f"Aresta de {u} para {v} não encontrada")
    return None

  # pont j
  def imprime_lista_adjacencias(self):
    impressaoTotal = ""
    for vertice in self.adjacenteLista:
      impressao = f"{vertice}:"
      for destino, peso in self.adjacenteLista[vertice]:
        impressao += f"('{destino}', {peso}) ->"
      impressaoTotal += impressao.strip(", ") + "\n"
      print(impressao)
        
g = Grafo(4)

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
