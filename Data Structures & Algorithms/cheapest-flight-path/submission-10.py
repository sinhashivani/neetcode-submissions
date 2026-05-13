class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        q = deque()
        grid = {}
         

        for origin, dest, price in flights:
            if origin not in grid:
                grid[origin] = []
            grid[origin].append((dest, price))
            if origin == src:
                q.append((dest, price))
        
        memo = {}
        
        def dfs(curr_node, curr_price, depth):
            min_price = float('inf')
            if (curr_node, depth) in memo and curr_price >= memo[(curr_node, depth)]:
                return memo[(curr_node, depth)]
        
            if curr_node == dst and depth <= k + 1:
                #print("A")
                #print(f"curr node {curr_node}")
                memo[(curr_node, depth)] = curr_price
                return curr_price
            if depth == (k + 1) and curr_node != dst:
                #print("B")
                #print(f"curr node {curr_node}")
                memo[(curr_node, depth)] = curr_price
                return float('inf')
            if curr_node in grid:
                for node, price in grid[curr_node]:
                    min_price = min(min_price, dfs(node, curr_price + price, depth + 1))
                    #print(f"min_price {min_price} node {node} curr_price {curr_price} depth {depth + 1}")
            else:
                return float('inf')
            
            memo[(curr_node, depth)] = min_price
            return min_price

        res = dfs(src, 0, 0)
        if res == float('inf'):
            return -1
        return res

                
            

        
        