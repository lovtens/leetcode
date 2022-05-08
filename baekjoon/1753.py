"""
https://www.acmicpc.net/problem/1753
다익스트라
"""
import sys
import math
import heapq
INF = math.inf

def solution():
    # 정점의 개수 / 간선의 개수
    v, e = map(int, sys.stdin.readline().split())
    # 시작점
    k = int(sys.stdin.readline())
    adj = dict()
    for i in range(e):
        uu, vv, ww = map(int, sys.stdin.readline().split())
        if uu not in adj:
            adj[uu] = dict()
        if vv in adj[uu]:
            adj[uu][vv] = min(adj[uu][vv], ww)
        else:
            adj[uu][vv] = ww
        # 만약 단방향이 아니라면 똑같이 uu, vv만 바꿔서 똑같이

    distance = [INF] * v
    distance[k-1] = 0
    visit = [False] * v
    q = []
    heapq.heappush(q, [0, k])
    while q:
        _, cur_node = heapq.heappop(q)
        cur_w = distance[cur_node-1]
        # print('cur_node', cur_node)
        visit[cur_node-1] = True
        # cur의 인접 노드
        # print('adj', adj[cur_node-1])
        if cur_node not in adj:
            # 간선이 없어서 key 자체가 없는 경우 예외 처리
            continue
        for next_node, next_w in adj[cur_node].items():
            if visit[next_node-1]:
                continue
            # print('next_node', next_node)
            if distance[next_node-1] > cur_w + next_w:
                distance[next_node-1] = cur_w + next_w
                heapq.heappush(q, [distance[next_node-1], next_node])
        # print('distance', distance)
    for x in distance:
        if x == INF:
            print("INF")
        else:
            print(x)

solution()