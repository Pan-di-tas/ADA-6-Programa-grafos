import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
estados = ['Estado1', 'Estado2', 'Estado3', 'Estado4', 'Estado5', 'Estado6', 'Estado7']
for estado in estados:
    G.add_node(estado)

conexiones = [
    ('Estado1', 'Estado2', 10),
    ('Estado2', 'Estado3', 15),
    ('Estado3', 'Estado4', 20),
    ('Estado4', 'Estado5', 25),
    ('Estado5', 'Estado6', 30),
    ('Estado6', 'Estado7', 35),
    ('Estado7', 'Estado1', 40)  # Añadir más conexiones si es necesario
]
for origen, destino, costo in conexiones:
    G.add_edge(origen, destino, weight=costo)

def recorrido_sin_repetir(grafo):
    recorrido = list(nx.dfs_edges(grafo, source='Estado1'))
    return recorrido

def recorrido_con_repeticion(grafo):
    try:
        ciclo = list(nx.find_cycle(grafo, orientation='ignore'))
        return ciclo
    except nx.NetworkXNoCycle:
        print("No se encontró un ciclo en el grafo.")
        return []

def dibujar_grafo(grafo):
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10)
    labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    plt.show()

def mostrar_relaciones(grafo):
    for origen, destino, datos in grafo.edges(data=True):
        print(f'{origen} <-> {destino}, Costo: {datos["weight"]}')

def calcular_costo_total(grafo, recorrido):
    costo_total = sum(grafo[u][v]['weight'] for u, v, *_ in recorrido) 
    return costo_total


# Ejecución del código
print("Recorrido sin repetir estados:")
recorrido_sin_repetir_res = recorrido_sin_repetir(G)
print(recorrido_sin_repetir_res)

print("\nRecorrido con repetición permitida:")
recorrido_con_repeticion_res = recorrido_con_repeticion(G)
print(recorrido_con_repeticion_res)

print("\nCosto total del recorrido sin repetición:")
print(calcular_costo_total(G, recorrido_sin_repetir_res))

print("\nCosto total del recorrido con repetición:")
print(calcular_costo_total(G, recorrido_con_repeticion_res))

print("\nRelaciones entre estados y sus costos:")
mostrar_relaciones(G)

dibujar_grafo(G)
