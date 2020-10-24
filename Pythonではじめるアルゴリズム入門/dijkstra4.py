# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 02:38:24 2020

@author: ckn32
"""

import heapq

def dijkstra(edges, num_v, goal):
    dist = [float('inf')] * num_v
    dist[0] = 0
    q = []
    heapq.heappush(q, [0, [0]])
    
    while len(q) > 0:
        # ヒープから取り出し
        _, u = heapq.heappop(q)
        last = u[-1]
        if last == goal:
            return u
        for i in edges[last]:
            if dist[i[0]] > dist[last] + i[1]:
                # 頂点までのコストが更新できれば更新してヒープに登録
                dist[i[0]] = dist[last] + i[1]
                heapq.heappush(q, [dist[last] + i[1], u + [i[0]]])

    return []

# 辺のリスト（終点のコストのリスト）
edges = [
    [[1, 4], [2, 3]],           # 頂点Aからの辺のコスト
    [[2, 1], [3, 1], [4, 5]],   # 頂点Bからの辺のコスト
    [[5, 2]],                   # 頂点Cからの辺のコスト
    [[4, 3]],                   # 頂点Dからの辺のコスト
    [[6, 2]],                   # 頂点Eからの辺のコスト
    [[4, 1], [6, 4]],           # 頂点Fからの辺のコスト
    []                          # 頂点Gからの辺のコスト
]
print(dijkstra(edges, 7, 6))