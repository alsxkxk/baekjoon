import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split())

items = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, c = map(int, input().split())

    graph[a].append([b,c])
    graph[b].append([a,c])

distance_list = [[0]]
def solution():

    for i in range(1, n+1):
        distance = [INF] * (n + 1)
        q = []
        distance[i] = 0

        heapq.heappush(q, (0, i))

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0],))

        distance_list.append(distance[:])

solution()

result = []
for i in range(1, n+1):
    temp = 0
    temp+=items[i-1]

    for j in range(1, n+1):
        if distance_list[i][j]!=0 and distance_list[i][j]<=m:
            temp+=items[j-1]

    result.append(temp)
print(max(result))