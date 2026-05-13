class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_a = 0

        while left < right:
            cur = (right - left) * min(heights[left], heights[right])
            if cur > max_a:
                max_a = cur
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return max_a
        