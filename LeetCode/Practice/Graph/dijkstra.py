# https://neetcode.io/problems/dijkstra
# Use case: Edges are weighted and directed. Want shortest/cheapest path.
# Intuition
# - *Unvisited* set, as opposed to visited in DFS/BFS
# - This is because of Dijkstra key property: cur_node will always have the minimum distance already
#   - Intuitively, any other path will have to go through other unvisited nodes which have greater weights
# - Need to store path weights (and sometimes the previous node in the path)

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        neighbours = {i : [] for i in range(n)} # node -> neighbours
        visited = set()           # Didn't end up needing visited set
        unvisited = set(range(n)) 
        paths = [float('inf')] * n # node -> weight
        res = {}

        for u, v, w in edges:
            neighbours[u].append((v, w))
        
        paths[src] = 0
        
        while unvisited:
            cur_node = None
            min_weight = float('inf')
            for node in unvisited:
                if paths[node] < min_weight:
                    cur_node = node
                    cur_weight = paths[cur_node]
            if cur_node is None:
                break

            unvisited.remove(cur_node)
            visited.add(cur_node)
            for neighbour, weight in neighbours[cur_node]:
                new_path_weight = cur_weight + weight
                if new_path_weight < paths[neighbour]:
                    paths[neighbour] = new_path_weight
        
        for i in range(n):
            res[i] = -1 if paths[i] == float('inf') else paths[i]
        
        return res