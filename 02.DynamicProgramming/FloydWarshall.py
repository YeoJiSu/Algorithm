def floydWarshall():
    inf = float("inf")
    example = [
        [0, 5, inf, 8],
        [7, 0, 9, inf],
        [2, inf, 0, 4],
        [inf, inf, 3, 0]
    ]
    num = len(example)
    # 시간복잡도: O(n^3)
    for i in range(num):
        for j in range(num):
            for k in range(num):
                road = example[i][k]+example[k][j]
                example[i][j] = min(example[i][j],road)
    return(example)

print(floydWarshall())