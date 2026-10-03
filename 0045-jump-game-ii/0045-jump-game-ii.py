class Solution:
    def jump(self, nums):
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            # Farthest position we can reach
            farthest = max(farthest, i + nums[i])

            # Current jump has reached its limit
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps