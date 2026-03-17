class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = {}
        weight = {}  # weight[x] = x / parent[x]

        def find(x):
            if parent[x] != x:
                root = find(parent[x])
                weight[x] *= weight[parent[x]]
                parent[x] = root
            return parent[x]

        def union(a, b, val):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            # ra/rb = val * weight[b] / weight[a]
            weight[ra] = val * weight[b] / weight[a]
            parent[ra] = rb

        for (a, b), val in zip(equations, values):
            if a not in parent:
                parent[a] = a
                weight[a] = 1.0
            if b not in parent:
                parent[b] = b
                weight[b] = 1.0
            union(a, b, val)

        result = []
        for a, b in queries:
            if a not in parent or b not in parent:
                result.append(-1.0)
            elif find(a) != find(b):
                result.append(-1.0)
            else:
                result.append(weight[a] / weight[b])
        return result

        