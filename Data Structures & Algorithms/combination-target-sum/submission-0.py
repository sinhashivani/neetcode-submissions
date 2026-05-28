class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(cur_index: int, cur_sum: int, cur_stack: List[int]):

            if cur_sum == target:
                res.append(list(cur_stack))
                return
            if cur_index >= len(nums) or cur_sum > target:
                return
            

            
            cur_stack.append(nums[cur_index])
            dfs(cur_index, cur_sum + nums[cur_index], cur_stack)

            cur_stack.pop()
            dfs(cur_index + 1, cur_sum, cur_stack)

        
        dfs(0, 0, [])

        return res