nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [1]
nums3 = [5, 4, -1, 7, 8]


class Solution:
    def maxSubArray(nums: list[int]):
        max_sum = nums[0]
        current_sum = 0
        for i in nums:
            current_sum += i
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum


print(Solution.maxSubArray(nums1))
print(Solution.maxSubArray(nums2))
print(Solution.maxSubArray(nums3))
