"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue = deque([node])
        cloned_graph = {node: Node(node.val)}

        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in cloned_graph:
                    cloned_graph[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                cloned_graph[current].neighbors.append(cloned_graph[neighbor])
        return cloned_graph[node]
                    
            
        