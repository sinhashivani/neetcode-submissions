class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1]
        memo = {}

        #create a dfs function that goes through each potential combination of days
        # and returns the combination it could create with the cost. it'll find the minimum
        # cost overall

        travel_days = set(days)

        def dfs(src, curr_cost):
            if src > n:
                return curr_cost
            
            #cur vs curr?
            if src not in travel_days:
                return dfs(src + 1, curr_cost)
            if (src in memo) and (curr_cost >= memo[src]):
                return float('inf')
            
            memo[src] = curr_cost
            cost = min(dfs(src + 1, curr_cost + costs[0]), dfs(src + 7, curr_cost + costs[1]), dfs(src + 30, curr_cost + costs[2]))

            return cost
        
        return dfs(days[0], 0)