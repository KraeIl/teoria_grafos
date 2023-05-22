import grafo

file = open("grafo4.txt", "r")
texto = file.readlines()
file.close()

vert_txt = texto[1:]
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 
         'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "1", "2",
         "3", "4", "5", "6", "7", "8", "9", "0"]

grafo = grafo.Grafo()
num_arestas = 0

for i in range(len(vert_txt)):
  vert1_txt = ""
  vert2_txt = ""
  leu_vertices = False
  contagem = 0
  
  for j in range(len(vert_txt[i])):
    
    if not leu_vertices:
      if vert_txt[i][j] in chars:
        if contagem == 0:
          vert1_txt = vert1_txt + vert_txt[i][j]
          
          if j == (len(vert_txt[i])-1):
            grafo.add_vertice(vert1_txt)
            leu_vertices = True  
        
        elif contagem == 1:
          vert2_txt = vert2_txt + vert_txt[i][j]

          if j == (len(vert_txt[i])-1):
            grafo.add_vertice(vert2_txt)
            leu_vertices = True    
      
      else:
        if contagem == 0:
          if vert_txt[i][j] != "":
            grafo.add_vertice(vert1_txt)
            contagem = contagem + 1
          else:
            leu_vertices = True
          
        elif contagem == 1:
          grafo.add_vertice(vert2_txt)
          leu_vertices = True
    
    if leu_vertices:
      if vert1_txt != "" and vert2_txt != "":
        num_arestas += 1
        arestas = [vert1_txt, vert2_txt]
        grafo.add_aresta(arestas)
      break
    
vertices = grafo.todos_vertices()

print(f"Número de vértices: {len(vertices)}")

print(f"Número de arestas: {num_arestas}")

print("")
print(grafo)

grau_max, grau_min = grafo.getGrauMin_Max()
print(f"Grau máximo: {grau_max}\nGrau mínimo: {grau_min}")

matriz_adj = grafo.matriz_adj()

print("\nMatriz de Adjacência:")
for linha in matriz_adj:
  print(linha)

_, busca = grafo.busca_largura(vertices[0])
print(f"\nBusca em largura a partir do primeiro vértice lido ({vertices[0]}): ", busca)
print(f"\n{grafo.get_ComponentesCon()}")