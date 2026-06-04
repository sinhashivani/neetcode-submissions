class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_sum = sum(piles)
        l, r = 1, max_sum

        min_rate = float('inf')

        while l <= r:
            mid = (l + r) // 2
            #print(f"{l} {r} {mid}")
            count = 0
            for p in piles:
                count += math.ceil(p / mid)
            
            if count <= h:
                r = mid - 1
                min_rate = min(min_rate, mid)

            elif count > h:
                l = mid + 1
            #print(f"{count} count")
            
        return min_rate
