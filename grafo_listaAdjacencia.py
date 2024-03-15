from collections import defaultdict

class Grafo:
  # construtor da classe com atributos numero_vertices, numero_arestas e lista adjacente
  def __init__(self, numeroVertices):
    self.numero_vertices = numeroVertices
    self.numero_arestas = 0
    self.adjacenteLista = defaultdict(list)

  """def __str__(self):
    return self.imprime_lista_adjacencias()"""

 # ponto a
 def adiciona_vertice(self, u_vertice_inicial):
    if u_vertice_inicial not in self.adjacenteLista:
      self.adjacenteLista[u_vertice_inicial] = []
      self.numero_vertices += 1

  # ponto b
  def adiciona_aresta(self, u_vertice_inicial, v_vertice_final, peso):
    if u_vertice_inicial not in self.adjacenteLista:
      self.adjacenteLista[u_vertice_inicial]
    if v_vertice_final not in self.adjacenteLista:
      self.adjacenteLista[v_vertice_final]

    self.adjacenteLista[u_vertice_inicial].append((v_vertice_final, peso))
    self.numero_arestas += 1
    
  
  # ponto c
  def remove_aresta(self, u_vertice_inicial, v_vertice_final):
      if u_vertice_inicial in self.adjacenteLista:
        for i, (destino, peso) in enumerate(self.adjacenteLista[u_vertice_inicial]):
          if destino == v_vertice_final:
            del self.adjacenteLista[u_vertice_inicial][i]
            self.numero_arestas -= 1
            print(f"Aresta de {u_vertice_inicial} para {v_vertice_final} removida com sucesso.")
            return
      print(f"Aresta de {u_vertice_inicial} para {v_vertice_final} não encontrada.")
      
  
  # ponto d
def remove_vertice(self, u_vertice_inicial):
      if u_vertice_inicial not in self.adjacenteLista:
        print(f"Vertice {u_vertice_inicial} não se encontra.")
        return

      removidaAresta = len(self.adjacenteLista[u_vertice_inicial])
      del self.adjacenteLista[u_vertice_inicial]

      for v_vertice_final in list(self.adjacenteLista):
        removidaAresta += sum(1 for destino, _ in self.adjacenteLista[v_vertice_final] if destino == u_vertice_inicial)
        self.adjacenteLista[v_vertice_final] = [(destino, peso) for destino, peso in self.adjacenteLista[v_vertice_final] if destino != u_vertice_inicial]
      
      self.numero_vertices -= 1
      self.numero_arestas -= removidaAresta
      print(f"Vertice {u_vertice_inicial} e suas arestas foram removidas")

  # ponto e
 def tem_aresta(self, u_vertice_inicial, v_vertice_final):
    if u_vertice_inicial in self.adjacenteLista:
      for destino, _ in self.adjacenteLista[u_vertice_inicial]:
        if destino == v_vertice_final:
          return True
    return False

  # ponto f
  def grau_entrada(self, u_vertice_inicial):
    grau_entrada = 0
    for i in self.adjacenteLista:
      for destino, _ in self.adjacenteLista[i]:
        if destino == u_vertice_inicial:
          grau_entrada += 1
    return grau_entrada

  # ponto g
 def grau_saida(self, u_vertice_inicial):
    if u_vertice_inicial in self.adjacenteLista:
      return len(self.adjacenteLista[u_vertice_inicial])
    return 0

  # ponto h
 def grau(self, u_vertice_inicial):
    return self.grau_entrada(u_vertice_inicial) + self.grau_saida(u_vertice_inicial)

  # ponto i
 def get_peso(self, u_vertice_inicial, v_vertice_final):
    if u_vertice_inicial not in self.adjacenteLista:
      print(f"Vertice {u_vertice_inicial} não existente")
      return None
    for destino, peso in self.adjacenteLista[u_vertice_inicial]:
      if destino == v_vertice_final:
        return peso

    print(f"Aresta de {u_vertice_inicial} para {v_vertice_final} não encontrada")
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
