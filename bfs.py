'''
Given a directed graph. The task is to do Breadth First Traversal of this graph starting from 0.
Note: One can move from node u to node v only if there's an edge from u to v. Find the BFS traversal of the graph starting from the 0th vertex, from left to right according to the input graph. Also, you should only take nodes directly or indirectly connected from Node 0 in consideration.

'''

from typing import List
from queue import Queue

class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        
        q = Queue()
        visited_arr  = [False]*V
        q.put(0)
        visited_arr[0] = True
        
        bfs_traversal = []
        
        while q.queue:
            
            vertex = q.get()
            bfs_traversal += [vertex]
            
            if len(adj[vertex]) > 0:
                for neighbour in adj[vertex]:
                    if not visited_arr[neighbour]:
                        q.put(neighbour)
                        visited_arr[neighbour] = True
                    
        return bfs_traversal
