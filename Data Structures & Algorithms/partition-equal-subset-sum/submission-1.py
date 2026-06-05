class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if sum(nums) % 2 == 1:
            return False
        
        seen = set()
        seen.add(0)

        for i in range(len(nums)):
            new_seen = set(seen)
            for val in seen:
                if nums[i] + val < target:
                    new_seen.add(nums[i] + val)
                if nums[i] + val == target:
                    return True
            seen = new_seen
        
        return False