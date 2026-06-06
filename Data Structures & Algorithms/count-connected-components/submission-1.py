class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        nodes = set()
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            nodes.add(u)
            nodes.add(v)
        
        components = 0
        visited = set()

        def dfs(node):
            cur = node
            for val in adj_list[cur]:
                if val in visited:
                    continue
                visited.add(val)
                dfs(val)
        
        for node in nodes:
            if node in visited:
                continue
            dfs(node)
            components += 1

        return components + (n - len(visited))