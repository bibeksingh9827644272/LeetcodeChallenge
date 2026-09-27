class Solution:
    def maxSubArray(self, nums):
        current = best = nums[0]

        for x in nums[1:]:
            current += x

            if current < x:
                current = x

            if current > best:
                best = current

        return best