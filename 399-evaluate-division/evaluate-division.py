class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(graph, src, dst,visited, cost_overall):
            print(src, dst, cost_overall)
            if cost_overall == -1:
                return -1
            if src==dst:
                return cost_overall
            if src not in graph:
                return -1
            
            for to, cost in graph[src]:
                if to not in visited:
                    visited.add(to)
                    t = dfs(graph, to,dst, visited,cost*cost_overall) 
                    if t!=-1:
                        return t
                    visited.remove(to)
            return -1
        from collections import defaultdict
        nodes = set()
        head =set()
        graph = defaultdict(list)
        for i in range(len(equations)):
            fro, to = equations[i]
            nodes.add(fro)
            nodes.add(to)
            head.add(fro)
            graph[fro].append((to, values[i])) 
            graph[to].append((fro, 1/values[i])) 
        result = []
        for fro, to in queries:
            if fro not in graph or to not in nodes:
                result.append(-1)
                continue
            if fro == to:
                result.append(1)
                continue
            cost = dfs(graph, fro,to,set([fro]),1)
            result.append(cost)

        return result

        