import numpy as np

def travellingsalesman(c, visited, cost, tsp_g, n):
    adj_vertex = -1
    min_val = float('inf')
    visited[c] = 1
    print((c + 1), end=" ")
    
    for k in range(n):
        if tsp_g[c][k] != 0 and visited[k] == 0:
            if tsp_g[c][k] < min_val:
                min_val = tsp_g[c][k]
                adj_vertex = k
    
    if min_val != float('inf'):
        cost[0] += min_val
        if adj_vertex == -1:
            adj_vertex = 0
        print((adj_vertex + 1), end=" ")
        cost[0] += tsp_g[c][adj_vertex]
        travellingsalesman(adj_vertex, visited, cost, tsp_g, n)
    else:
        cost[0] += tsp_g[c][0]  # return to the start point
        print((1), end=" ")

n = 5
cost = [0]
visited = np.zeros(n, dtype=int)
tsp_g = np.array([[12, 30, 33, 10, 45],
                  [56, 22, 9, 15, 18],
                  [29, 13, 8, 5, 12],
                  [33, 28, 16, 10, 3],
                  [1, 4, 30, 24, 20]])

print("Shortest Path:", end=" ")
travellingsalesman(0, visited, cost, tsp_g, n)
print()
print("Minimum Cost:", end=" ")
print(cost[0])
