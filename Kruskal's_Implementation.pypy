def cycle(a, parent):
    while parent[a]:
        a = parent[a]
    return a

def kruskal(n, arr):
    parent = [0] * n
    itr = 1
    cost = 0
    while itr < n:
        min_val = 99999
        a, b, c, d = None, None, None, None
        for i in range(n):
            for j in range(n):
                if arr[i][j] < min_val:
                    min_val = arr[i][j]
                    a, b, c, d = i, j, i, j

        c = cycle(c, parent)
        d = cycle(d, parent)
        if c != d:
            parent[c] = d
            print("{} - {}  {}".format(b, a, min_val))
            cost += min_val
            itr += 1

        arr[a][b] = arr[b][a] = 99999
    print("total cost: {}\n".format(cost))

n = 5
arr = [[0, 4, 2, 0, 0],
       [0, 0, 3, 2, 3],
       [0, 1, 0, 4, 5],
       [0, 0, 0, 0, 0],
       [0, 0, 0, -5, 0]]
       
       

for i in range(n):
    for j in range(n):
        if arr[i][j] == 5:
            break
        if arr[i][j] == 0:
            arr[i][j] = 99999
        

kruskal(n, arr)
