class Grafo(object):
    
    def __init__(self):
        self._grafo_dict = {}
            
    def arestas(self, vertice):
        return self._grafo_dict[vertice]
       
    def todos_vertices(self):
        return list(self._grafo_dict.keys())
    
    def todas_arestas(self):
        msg = ""
        for vert in self._grafo_dict:
            msg += "Vértice: " + str(vert) + " arestas: " + str(self._grafo_dict[vert]) + "\n"
            
        return msg
    
    def add_vertice(self, vertice):
        if vertice not in self._grafo_dict:
            self._grafo_dict[vertice] = []
            
    def add_aresta(self, aresta):
        vertice1, vertice2 = list(aresta)
        
        if vertice1 != "" and vertice2 != "" :
            for x, y in [(vertice1, vertice2), (vertice2, vertice1)]:
                if x in self._grafo_dict:
                    if y not in self._grafo_dict[x]:
                        if y != "":
                            self._grafo_dict[x].append(y)
                else:
                    if y != "":
                        self._grafo_dict[x] = [y]
        
    def addAresta(self, arestas):
        self.arestas.append(arestas) 
    
    def getGrauMin_Max(self):
        max = 0
        min = 0
        
        i = 0
        for vert in self._grafo_dict:
            if i == 0:
                max = len(self._grafo_dict[vert])
                min = len(self._grafo_dict[vert])
            
            if len(self._grafo_dict[vert]) > max:
                max = len(self._grafo_dict[vert])
            
            if len(self._grafo_dict[vert]) < min:
                min = len(self._grafo_dict[vert])
            
            i = i + 1
        
        return (max, min)
           
    def __str__(self):      
        return self.todas_arestas()
    
    def matriz_adj(self):
        matriz_adj = [[0 for _ in range(len(self._grafo_dict))] for _ in range(len(self._grafo_dict))]
        
        i = 0
        for vert1 in self._grafo_dict.keys():
            j = 0
            for vert2 in self._grafo_dict.keys():
                if vert1 in self._grafo_dict[vert2]:
                    matriz_adj[i][j] = 1

                if j < (len(self._grafo_dict)-1):
                    j = j + 1
            
            if i < (len(self._grafo_dict)-1):
                i = i + 1
        
        self.matriz_adj = matriz_adj
        return matriz_adj
    
    def busca_largura(self, vertice_fonte):
        visitados, fila = list(), [vertice_fonte]
        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                visitados.append(vertice)
                arestas = self._grafo_dict[vertice]
                extender = [i for i in arestas if i not in visitados]
                fila.extend(extender)
                
        msg = ""
        for i in range(len(visitados)):
            if len(visitados) == 1:
                
                msg += str(visitados[0]) + " -> " + str(visitados[0])
                break
            
            if i == 0:
                msg += str(visitados[i]) + " -> "
                        
            elif i == (len(visitados)-1):
                msg += str(visitados[i])
                
            else:
                msg += str(visitados[i]) + " -> "
                
        return visitados, msg
    
    def get_ComponentesCon(self):
        vertices = self.todos_vertices()
        visitar = vertices.copy()
        vertices.sort()
        
        msg = ""
        i = 0
        componentes = []
        while visitar:
            
            componente, _ = self.busca_largura(visitar.pop(0))
            componente.sort()
            if vertices == componente:
                msg += "O grafo é totalmente conexo, portando não existe componentes conexos neste grafo"
                break
            
            else:
                if i == 0:
                    i = 1
                    msg += "O grafo não é totalmente conexo, portanto existem componentes conexos neste grafo, que são os seguintes:\n"
                
                if componente not in componentes:
                    if componente[0] != "":
                        componentes.append(componente)
                    else:
                        vert = componente[1]
                        componentes.append(list(vert))
                        componente.clear()
                        componente.append(vert)
                        print(componente)
            
            visitar = [item for item in visitar if item not in componente]
            
        #print(componentes)
        for i in componentes:     
            msg += str(i) + "\n"   
            
        return msg
    
    def __iter__(self):
        self.__iter__obj = iter(self._grafo_dict)
        return self.__iter__obj
    
    def __next__(self):
        return next(self.__iter__obj)
    