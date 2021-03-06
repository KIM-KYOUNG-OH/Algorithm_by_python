from collections import deque


def dfs(v):
    print(v, end=' ')
    dfs_visited[v] = True
    for i in range(1, n+1):
        if graph[v][i] == 1 and not dfs_visited[i]:
            dfs(i)


def bfs(v):
    queue = deque([v])
    bfs_visited[v] = True
    while queue:
        a = queue.popleft()
        print(a, end=' ')
        for i in range(1, n+1):
            if graph[a][i] == 1 and not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i] = True


n,m,v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

dfs(v)
print()
bfs(v)