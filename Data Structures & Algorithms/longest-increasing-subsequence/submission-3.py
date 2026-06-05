class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        dp[0] = 1

        for i in range(0, len(nums)):
            longest_valid = 1
            for j in range(0, i):
                #print(f"num1 {nums[i]} num2 {nums[j]} {longest_valid}")
            
                if nums[i] > nums[j]:
                    longest_valid = max(longest_valid, dp[j] + 1)
                    #print(f"num1 {nums[i]} num2 {nums[j]} {longest_valid}")
            
            dp[i] = longest_valid

        return max(dp)
