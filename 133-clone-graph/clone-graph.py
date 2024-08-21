"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        print(node.val)
        cloned_graph={}
        stack=[node]
        cloned_graph[node]=Node(node.val)
        while stack:
            curr=stack.pop()
            for neighbour in curr.neighbors:
                if neighbour not in cloned_graph:
                    cloned_graph[neighbour]=Node(neighbour.val)
                    stack.append(neighbour)
                cloned_graph[curr].neighbors.append(cloned_graph[neighbour])
        return cloned_graph[node]

        