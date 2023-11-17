# Implementação de uma lista de adjacentes 

def printList(d, f, n):
    print("D:", "[" + ", ".join(map(str, d[:n])) + "]")
    print("F:", "[" + ", ".join(map(str, f[:n])) + "]")
    
    # Saída mais organizada do vetores de tempo D e F
    # JOIN concatena cada iteração da lista usando MAP com , e um espaço

#Função para carregar os vértices de maior grau de saída pro menor.
def listaDosMaioresGraus():
    file = open("grafos/g2.txt", "r")
    list = file.readlines()
    
    #Irá ler a primeira coluna do arquivo txt do grafo escolhido.
    for i in range(len(list)):
        line = list[i].split()
        if i == 0:
            n = int(line[0])
            saidas = [0] * n #Crio um vetor de grau de saída de acordo com o N de vértices.
        else:
            saidas[int(line[0])-1] += 1 #Cada vez que o número aparecer, quer dizer que seu grau de saída é aumentado.
    file.close()

    maioresgraus = [] #Crio uma lista vazia para armazenas os vértices do maior grau pro menor.
    for i in range(len(saidas)):
        maioresgraus.append(saidas.index(max(saidas))) #Vai adicionando na lista o índice(vértice) de maior grau até então.
        saidas[saidas.index(max(saidas))] = -1 #E no local do vértice de maior grau de saída é substituido por -1, para simbolizar que o vértice já foi removido da lista.
    return maioresgraus #E retorna a lista com os vértices do maior grau de saída pro menor.
    

#Função para carregar a lista de adjacentes
def loadList():
    file = open("grafos/g2.txt", "r") #Abro o arquivo txt em modo de leitura
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


def DFS_visit(u):
    global tiposDasArestas
    global mark 
    cor[u] = "Cinza" #Marco o vértice branco como cinza

    mark += 1
    d[u] = mark #E marco o tempo em que ele se tornou

    for v in lista_adj[u]: #Percorro a lista de vértices adjacentes de U até que não encontre ninguém mais branco.
        if cor[v] == "Branco":
            tiposDasArestas.append(f"{u+1} {v+1}: Árvore")
            DFS_visit(v)
        elif cor[v] == "Cinza":
            tiposDasArestas.append(f"{u+1} {v+1}: Retorno")
        elif cor[v] == "Preto" and d[u] < f[v]:
            tiposDasArestas.append(f"{u+1} {v+1}: Avanço")
        else:
            tiposDasArestas.append(f"{u+1} {v+1}: Cruzamento")
        
    cor[u] = "Preto" #Após todos seus vizinhos terem sido testados, marca o vértice como preto.
    mark += 1
    f[u] = mark #E marca o tempo que ele se torno preto.


def DFS():
    for u in v: #Inicializo todos os vértices como brancos
        cor[u] = "Branco"

    for u in v: #Dou inicio ao algoritmo, caso ele seja branco, significa que não visitamos ainda.
        if cor[u] == "Branco":
            DFS_visit(u)

def exibirTiposDasArestas():
    global tiposDasArestas
    print(f"Resultado do DFS a partir do vértice {v[0]+1}!")
    for i in tiposDasArestas:
        print(i)


tiposDasArestas = [] #Lista que irá armazenar a nomenclatura das arestas.
[lista_adj, n] = loadList() #Carrego a lista de adjacência e o tamanho de vertices.
v = listaDosMaioresGraus() #Ordem de vértices de maior pro menor grau de saída que o algoritmo irá ser executado.

#Vetores iniciais e a variável de marcação inicializados.
cor = [0] * n 
d = [0] * n
f = [0] * n
mark = 0

#Chamo o algoritmo DFS pro Grafo e printo em seguida os vetores e a nomenclatura.
DFS()
printList(d, f, n)
exibirTiposDasArestas()