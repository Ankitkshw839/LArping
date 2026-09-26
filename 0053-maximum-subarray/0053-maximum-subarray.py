class Solution(object):
    def maxSubArray(self, nums):

        current_sum = nums[0]
        total_sum = nums[0]

        for i in range(1, len(nums)):
            if current_sum + nums[i] >= nums[i]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]

            if total_sum < current_sum:
                total_sum = current_sum

        return total_sum


        