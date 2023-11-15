# Implementação de uma lista de adjancentes 

def printList(d, f, n):
    print("D:", "[" + ", ".join(map(str, d[:n])) + "]")
    print("F:", "[" + ", ".join(map(str, f[:n])) + "]")

def loadList():
    file = open("grafos/g1.txt", "r")
    list = file.readlines()

    for i in range(len(list)):
        line = list[i].split()  # Split each line of the file

        if i == 0: 
            n = int(line[0])
            list_adjacent = [ [] for _ in range(n) ]
        else: 
            list_adjacent[int(line[0])-1].append(int(line[1])-1)
    
    file.close()
    return list_adjacent, n


def DFS_visit(u):
    global mark
    cor[u] = "Cinza"
    mark += 1
    d[u] = mark

    for v in lista_adj[u]:
        if cor[v] == "Branco":
            DFS_visit(v)
    
    cor[u] = "Preto"
    mark += 1
    f[u] = mark


def DFS():
    for u in v:
        cor[u] = "Branco"

    for u in v:
        if cor[u] == "Branco":
            DFS_visit(u)


[lista_adj, n] = loadList()
v = [3,0,1,2,4,5,6,7]
cor = [0] * n
d = [0] * n
f = [0] * n
mark = 0
DFS()
printList(d, f, n)