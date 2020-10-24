# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 02:12:42 2020

@author: ckn32
"""

import heapq

def dijkstra(edges, num_v):
    dist = [float('inf')] * num_v
    dist[0] = 0
    q = []
    heapq.heappush(q, [0, 0])
    
    while len(q) > 0:
        # ヒープから取り出し
        _, u = heapq.heappop(q)
        for i in edges[u]:
            if dist[i[0]] > dist[u] + i[1]:
                # 頂点までのコストが更新できれば更新してヒープに登録
                dist[i[0]] = dist[u] + i[1]
                heapq.heappush(q, [dist[u] + i[1], i[0]])

    return dist

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
print(dijkstra(edges, 7))