# Implementação de uma lista de adjacentes 

def printList(d, f, n):
    print("D:", "[" + ", ".join(map(str, d[:n])) + "]")
    print("F:", "[" + ", ".join(map(str, f[:n])) + "]")
    
    # Saída mais organizada do vetores de tempo D e F
    # JOIN concatena cada iteração da lista usando MAP com , e um espaço


#Função para carregar a lista de adjacentes
def loadList():
    file = open("grafos/g1.txt", "r") #Abro o arquivo txt em modo de leitura
    list = file.readlines() #Leio cada linha

    for i in range(len(list)):
        line = list[i].split()  # Dou um split em cada linha para separar as informações do grafo

        if i == 0: #Como a primeira linha do arquivo contém a qtd de vértices e arestas, no primeiro loop leio esses dados
            n = int(line[0]) #Seto o tamanho da lista de acordo com o tamanho de vértices do grafo.
            list_adjacent = [ [] for _ in range(n) ] #Crio uma lista vazia de acordo com o N.
        
        else:#Se não estiver no inicio, quer dizer que estará lendo as arestas existentes. 
            list_adjacent[int(line[0])-1].append(int(line[1])-1) #Armazeno na posição de cada vértice, os seus vertices adjacentes.
    
    file.close()
    return list_adjacent, n

arestasArvore = []
arestasRetorno = []
arestasAvanco = []
arestasCruzamento = []

def DFS_visit(u):
    global arestasArvore,arestasAvanco,arestasCruzamento,arestasRetorno
    global mark 
    cor[u] = "Cinza" #Marco o vértice branco como cinza

    mark += 1
    d[u] = mark #E marco o tempo em que ele se tornou

    for v in lista_adj[u]: #Percorro a lista de vértices adjacentes de U até que não encontre ninguém mais branco.
        if cor[v] == "Branco":
            arestasArvore.append(f"{u+1} {v+1}: Árvore")
            DFS_visit(v)
        elif cor[v] == "Cinza":
            arestasRetorno.append(f"{u+1} {v+1}: Retorno")
        elif cor[v] == "Preto" and d[u] < f[v]:
            arestasAvanco.append(f"{u+1} {v+1}: Avanço")
        else:
            arestasCruzamento.append(f"{u+1} {v+1}: Cruzamento")
        
    cor[u] = "Preto" #Após todos seus vizinhos terem sido testados, marca o vértice como preto.
    mark += 1
    f[u] = mark #E marca o tempo que ele se torno preto.


def DFS():
    for u in v: #Inicializo todos os vértices como brancos
        cor[u] = "Branco"

    for u in v: #Dou inicio ao algoritmo, caso ele seja branco, significa que não visitamos ainda.
        if cor[u] == "Branco":
            DFS_visit(u)

def nomenclaturaArestas():
    print(f"Resultado do DFS a partir do vértice {v[0]+1}!")
    for i in arestasArvore:
        print(i)
    for i in arestasAvanco:
        print(i)
    for i in arestasRetorno:
        print(i)
    for i in arestasCruzamento:
        print(i)



[lista_adj, n] = loadList() #Carrego a lista de adjacência e o tamanho de vertices.

v = [1,0,2,3,4,5,6,7] #Ordem de vértices que o algoritmo irá ser executado.

#Vetores iniciais e a variável de marcação inicializados.
cor = [0] * n 
d = [0] * n
f = [0] * n
mark = 0

#Chamo o algoritmo DFS pro Grafo e printo em seguida os vetores e a nomenclatura.
DFS()
printList(d, f, n)
nomenclaturaArestas()