g = [[0,4,2,0,0],[0,0,3,2,3],[0,1,0,4,5],[0,0,0,0,0],[0,0,0,-5,0]]
for i in range(5):
    for j in range(5):
        if g[i][j]<0:
            g[i][j] = g[i][j]**2
        elif g[i][j] == 0:
            g[i][j] = 100

order = [0] * 5
dist = [0] * 5
visit = [0] * 5

for i in range(5):
    dist[i] = g[0][i]

for c in range(5):
    min = 100
    for i in range(5):
        if dist[i] < min and not visit[i]:
            min = dist[i]
            node = i
    visit[node] = 1
    for i in range(5):
        if not visit[i]:
            if min + g[node][i] < dist[i]:
                dist[i] = min + g[node][i]

for i in range(1, 5):
    print("Distance from 1 to {} is {}".format(i + 1, dist[i]))
