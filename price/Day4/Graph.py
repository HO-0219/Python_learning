#그래프(Graph)
# 그래프는 정점(Vertex)과 간선(Edge)으로 이루어진 자료구조
# 그래프는 방향성에 따라 방향 그래프(Directed Graph)와 무방향 그래프(Undirected Graph)로 나뉜다.
# 그래프는 두 정점 사이의 관계를 표현할 때 사용한다.
# 그래프는 인접 행렬(Adjacency Matrix)과 인접 리스트(Adjacency List)로 표현할 수 있다.

# 인접 리스트(Adjacency List)
graph ={
    'A' :['B','C'],
    'B' :['A','D'],
    'C' :['A','G','H','I'],
    'D' :['B','E','F'],
    'E' :['D'],
}
print(graph['A'])

#인접 행렬(Adjacency Matrix)
# 정점 4개 (A, B, C, D)
graph_matrix = [
    [0, 1, 1, 0],  # A → B, C
    [1, 0, 0, 1],  # B → A, D
    [1, 0, 0, 1],  # C → A, D
    [0, 1, 1, 0]   # D → B, C
]

# A에서 C로 가는 길이 있는가? (A = 0, C = 2)
print(graph_matrix[0][2])  # 1 (연결됨)

# B에서 C로 가는 길이 있는가? (B = 1, C = 2)
print(graph_matrix[1][2])  # 0 (연결되지 않음)
