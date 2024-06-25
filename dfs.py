'''
You are given a connected undirected graph. Perform a Depth First Traversal of the graph.
Note: Use the recursive approach to find the DFS traversal of the graph starting from the 0th vertex from left to right according to the graph.
'''

class Solution:
   def dfsOfGraph(self, V, adj):
        
        visited_arr = [False]*V
        ans = []
        
        def dfs(adj , node , visited_arr , ans):
            visited_arr[node] = True
            ans.append(node)
            
            for neighbour in adj[node]:
                if not visited_arr[neighbour]:
                    
                    dfs(adj , neighbour , visited_arr , ans)
                    
        dfs(adj , 0 , visited_arr , ans)
        
        return ans
