class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1 and edges == []:
            return True
        elif n == 1:
            return False
        visited = set()
        adj_list = defaultdict(set)
        
        for origin, dest in edges:
            adj_list[origin].add(dest)
            adj_list[dest].add(origin)      

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)

            children = adj_list[node]
            for c in children:
                if c == prev:
                    continue
                if not dfs(c, node):
                    return False
            
            return True

        if not dfs(0, -1):
            return False
        return len(visited) == n

