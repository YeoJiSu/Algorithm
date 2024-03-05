inf = float("inf")

path = [
    [0, 2, 5, 1, inf, inf],
    [2, 0, 3, 2, inf, inf],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, inf],
    [inf, inf, 1, 1, 0, 2],
    [inf, inf, 5, inf, 2, 0],
]

visit = [False]*6
shortest_path = []

# 가장 최소 거리를 가지는 정점을 반환
# 아래 방법은 선형 탐색이고, 다른 효율적인 탐색 방법을 사용하는 것이 좋다.
def getSmallIndex():
    val = inf
    idx = 0
    for i in range(len(visit)):
        if shortest_path[i] < val and visit[i] == False:
            val = shortest_path[i]
            idx = i
    return idx

def dijkstra(start):
    global shortest_path  # shortest_path를 전역 변수로 사용하겠다고 선언
    global visit
    
    shortest_path = path[start]
    visit[start] = True
    for i in range(len(visit)-2): # O(V) 처음 시작노드와 마지막 노드에 대해서는 반복문을 순회할 필요가 없다!
        current = getSmallIndex() # O(V)
        visit[current] = True  # 방문한 정점으로 표시
        for j in range(len(visit)): # O(V)
            if visit[j]==False: # 아직 방문한 곳이 아니라면, 
                if (shortest_path[current] + path[current][j] < shortest_path[j]):
                    shortest_path[j] = shortest_path[current] + path[current][j]
                    
dijkstra(0)
print(shortest_path)

# 시간 복잡도: O(V^2)