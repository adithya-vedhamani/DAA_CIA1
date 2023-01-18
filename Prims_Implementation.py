//Implementation in Prims's Algorithm
n = int(input("Enter the number of nodes:"))
cost = [[float('inf') for j in range(n)] for i in range(n)]
visited = [0 for i in range(n)]
mincost = 0
ne = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        cost[i][j] = int(input())
        if cost[i][j] == 0:
            cost[i][j] = float('inf')

visited[0] = 1

while ne < n:
    min = float('inf')
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if cost[i][j] < min:
                if visited[i - 1] != 0:
                    min = cost[i][j]
                    a = u = i
                    b = v = j
    if visited[u - 1] == 0 or visited[v - 1] == 0:
        print("Edge", ne, ": (", a, ",", b, ")", "Cost :", min)
        mincost += min
        visited[b - 1] = 1
    ne += 1
    cost[a][b] = cost[b][a] = float('inf')

print("\nMinimum cost=", mincost)
