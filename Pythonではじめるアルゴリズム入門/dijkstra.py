# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 19:02:28 2020

@author: ckn32
"""

def dijkstra(edges, num_v):
    dist = [float('inf')] * num_v
    dist[0] = 0
    q = [i for i in range(num_v)]
    
    while len(q) > 0:
        # 最もコストが小さい頂点を探す
        r = q[0]
        for i in q:
            if dist[i] < dist[r]:
                r = i
                
        # 最もコストが小さい頂点を取り出す
        u = q.pop(q.index(r))
        for i in edges[u]:
            if dist[i[0]] > dist[u] + i[1]:
                # 頂点までのコストが更新できれば更新
                dist[i[0]] = dist[u] + i[1]
                
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