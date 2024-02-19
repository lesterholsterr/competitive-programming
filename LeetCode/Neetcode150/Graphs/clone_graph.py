# Overall: I'm so proud of myself
# The use of a dictionary came naturally (need a way to store nodes and access them based on val)
# Recursive step was a bit tricky. The recursive call needs to be placed after the node creation
# but before the neighbour assignment.
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

# Initial solution - it's great!!
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodes = {}

        def cloneNode(node):
            if node.val not in nodes:
                nodes[node.val] = Node(node.val)

            for n in node.neighbors:
                if n.val not in nodes:
                    cloneNode(n)
                nodes[node.val].neighbors.append(nodes[n.val])

        cloneNode(node)
        return nodes[node.val]
