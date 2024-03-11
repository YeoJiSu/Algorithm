"""
example
노드 개수: 7
간선 개수: 9
29 1 2
75 1 5
35 2 3
34 2 6
7 3 4
23 4 6
13 4 7
53 5 6
25 6 7
"""
# 노드의 개수와 간선(Union 연산)의 개수 입력 받기 
v, e = map(int, input().split()) 
parent = [0] * (v+1) # 부모 테이블 초기화 하기

# 모든 간선을 담을 리스트
edges = []

# 최종 비용을 담을 변수
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기 
for _ in range(e):
    cost, a, b = map(int, input().split())
    edges.append((cost,a,b))

def parent_item(parent, a):
    if parent[a] == a:
        return parent[a]
    else:
        parent[a] = parent_item(parent, parent[a])
    return parent[a]
    
def union_parent(parent, a, b):
    a = parent_item(parent, a)
    b = parent_item(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 1. 간선 데이터 비용에 따라 오름차순 정렬
edges.sort()

# 2. 간선을 하나씩 확인하여 현재 간선이 cycle 발생시키는지 확인 
for edge in edges:
    cost, a, b = edge
    if parent_item(parent, a) != parent_item(parent, b):
        union_parent(parent, a, b)
        print(parent)
        result+=cost

print(result)
print(parent)
    

"""
[0,1,2,3,4,5,6,7]
 7 3 4 [0 1 2 3 3 5 6 7]
13 4 7 [0 1 2 3 3 5 6 3]
23 4 6 [0 1 2 3 3 5 3 3]
25 6 7 X
29 1 2 [0 1 1 3 3 5 3 3]
34 2 6 [0 1 1 1 3 5 3 3]
35 2 3 X
53 5 6 [0 1 1 1 3 1 1 3] # 6번째도 1로 바뀜.
75 1 5 X
"""