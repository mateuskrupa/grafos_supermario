#Integrantes da equipe:
#Mateus Scherreier Krupa 
#Gustavo Henrique Soares dos Santos
#Tito Claudio de Andrade Silva


import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

fases_conexoes = {
    "1": ["2"],
    "2": ["1", "3"],
    "3": ["2", "4"],
    "4": ["3", "5"],
    "5": ["4", "6"],
    "6": ["6a", "7"],
    "6a": ["6", "6b"],
    "6b": ["6a", "6c"],
    "6c": ["6b", "6d"],
    "6d": ["6c", "7"],
    "7": ["6", "6d", "8"],
    "8": ["7", "9"],
    "9": ["8","10", "18"],
    "10": ["9", "10a", "11"],
    "10a": ["10"],
    "11": ["10","11a","11b","12"],
    "11a": ["11","12"],
    "11b": ["11"],
    "12": ["11a","11","13"],
    "13": ["12","14","15"],
    "14": ["13"],
    "15": ["13","15a","16"],
    "15a": ["15","15b","15c"],
    "15b": ["15a","15c","15d"],
    "15c": ["15a","15b","29b"],
    "15d": ["15b"],
    "16": ["15","17"],
    "17": ["16","18","22","21"],
    "18": ["17","19","9"],
    "19": ["18","20"],
    "20": ["19","42","41","21"],
    "21": ["20","17","23"],
    "22": ["17","23"],
    "23": ["21","22","24"],
    "24": ["23","25"],
    "25": ["24","26","28"],
    "26": ["25","27"],
    "27": ["26"],
    "28": ["25","29"],
    "29": ["28","30","29a"],
    "29a": ["29","29b"],
    "29b": ["29a","29c","29d","29e"],
    "29c": ["29b","29g"],
    "29d": ["29b"],
    "29e": ["29b","29f"],
    "29f": ["29e","29g"],
    "29g": ["29c","29f"],
    "30": ["29","31"],
    "31": ["30","32","34"],
    "32": ["31","33"],
    "33": ["32"],
    "34": ["31","35","38","38a"],
    "35": ["34","36"],
    "36": ["35","37"],
    "37": ["36"],
    "38": ["35","34","38a","39"],
    "38a": ["38","34"],
    "39": ["38","40","39a"],
    "39a": ["39"],
    "40": ["39","41"],
    "41": ["40","42","20"],
    "42": ["41","20","43"],
    "43": ["42","44"],
    "44": ["43","45"],
    "45": ["44","46"],
    "46": ["45"],

    
}

G = nx.DiGraph()

for fase, conexoes in fases_conexoes.items():
    G.add_node(fase)
    for conexao in conexoes:
        G.add_edge(fase, conexao)


def encontrar_caminho_bfs(grafo, origem, destino):
    if origem not in grafo or destino not in grafo:
        return None  

    fila = deque([(origem, [origem])])  # Fila de nós para visitar e caminho percorrido
    visitados = set()

    while fila:
        fase_atual, caminho_atual = fila.popleft()

        if fase_atual == destino:
            return caminho_atual  # Caminho encontrado

        if fase_atual not in visitados:
            visitados.add(fase_atual)
            for vizinho in grafo[fase_atual]:
                if vizinho not in visitados:
                    fila.append((vizinho, caminho_atual + [vizinho]))

    return None  # Caminho não encontrado

#Pergunta o caminho
origem = str(input("Origem: "))
destino = str(input("Destino: "))


caminho = encontrar_caminho_bfs(fases_conexoes, origem, destino)

if caminho:
    print(f"Caminho de {origem} para {destino}:")
    for fase in caminho:
        print(fase)
else:
    print(f"Caminho de {origem} para {destino} não encontrado.")


# Visualizar o grafo
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # Layout do grafo
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_color='black', arrows=True)
plt.title("Mapa de Fases do Super Mario World")
plt.show()