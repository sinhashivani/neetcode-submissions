class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [] 

        for px, py in points:
            dist = px ** 2 + py ** 2

            heapq.heappush(min_heap, (-dist, [px, py]))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [point for _, point in min_heap]

