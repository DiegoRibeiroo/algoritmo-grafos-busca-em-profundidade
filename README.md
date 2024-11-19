Essa é uma implementação do algoritmo DFS (Busca em profundidade) em um grafo, carregando a lista de adjacência a partir de um arquivo. Ele ordena os vértices pelo grau de saída, executa o DFS para classificar as arestas (árvore, retorno, avanço e cruzamento)
e registra os tempos de descoberta e finalização de cada vértice. Por fim, exibe os resultados da DFS, incluindo os tipos das arestas.

A primeira linha do arquivo .txt contém dois números e se refere a quantidade de vértices e arestas respectivamente do grafo. Nas demais, se refere as arestas existentes do grafo, onde o primeiro número e o último número da linha se refere ao vértice inicial
e o vértice final daquela aresta, respectivamente.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This is an implementation of the Depth-First Search (DFS) algorithm on a graph, loading the adjacency list from a file. It orders the vertices by their out-degree, performs DFS to classify edges (tree, back, forward, and cross), 
and records the discovery and finish times of each vertex. Finally, it displays the DFS results, including the edge classifications.

The first line of the `.txt` file contains two numbers representing the number of vertices and edges in the graph, respectively.
The following lines list the graph's edges, where the first and last numbers of each line correspond to the starting and ending vertices of that edge, respectively.
