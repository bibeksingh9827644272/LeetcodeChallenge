class Solution:
    def maxSubArray(self, nums):
        best = nums[0]
        curr = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            curr = curr + x if curr > 0 else x
            if curr > best:
                best = curr

        return best