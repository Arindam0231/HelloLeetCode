class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        from collections import defaultdict

        graph = defaultdict(list)
        for fro, to in connections:
            graph[fro].append((to, 1))   # original direction — needs reversal
            graph[to].append((fro, 0))   # reverse direction — already correct
        nodes = [0]
        visited = set([0])
        reversed_nodes = 0
        while(nodes):
            n=nodes.pop()
            for neigbor,cost in graph[n]:
                if neigbor not in visited:
                    visited.add(neigbor)
                    reversed_nodes+=cost
                    nodes.append(neigbor)
        return reversed_nodes
        # n = [0]
        # visited = set([0])     
        # reversed_nodes = 0
        # while(n):
        #     node = n.pop()
        #     level = []
        #     for fro,to in connections:
        #         if to == node and fro not in visited:
        #             level.append(fro)
        #             visited.add(fro)
        #         if fro == node and to not in visited:
        #             reversed_nodes+=1
        #             level.append(to)
        #             visited.add(to)
        #     n.extend(level)

        # return reversed_nodes
