class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}

        for i, n in enumerate(nums):
            val = target - n
            if val in my_map:
                return [my_map[val], i]
            my_map[n] = i


        