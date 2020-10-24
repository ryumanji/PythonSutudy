# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 01:57:43 2020

@author: ckn32
"""

def min_heapify(data, i):
    left = 2 * i + 1
    right = 2 * i + 2
    min = i
    if left < len(data) and data[i][0] > data[left][0]:
        min = left
    if right < len(data) and data[i][0] > data[right][0]:
        min = right
    if min != i:
        data[i], data[min] = data[min], data[i]
        min_heapify(data, min)

def dijkstra(edges, num_v):
    dist = [float('inf')] * num_v
    dist[0] = 0
    q = [[0, 0]]
    
    while len(q) > 0:
        # キューから最初の要素を取り出し
        q[0], q[-1] = q[-1], q[0]
        _, u = q.pop()
        # キューを再構成
        min_heapify(q, 0)
        # 各辺に対してコストを調べる
        for i in edges[u]:
            if dist[i[0]] > dist[u] + i[1]:
                dist[i[0]] = dist[u] + i[1]
                q.append([dist[u] + i[1], i[0]])
                j = len(q) - 1
                while (j > 0) and (q[(j - 1) // 2] > q[j]):
                    q[(j - 1) // 2], q[j] = q[j], q[(j - 1) // 2]
                    j = (j - 1) // 2

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