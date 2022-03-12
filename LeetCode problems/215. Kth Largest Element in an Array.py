nums1, k1 = [3, 2, 1, 5, 6, 4], 2
nums2, k2 = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4


class Solution:
    def findKthLargest(nums: list[int], k: int):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        print(nums)
        max_num = nums[-k]
        return max_num


print(Solution.findKthLargest(nums1, k1))
print(Solution.findKthLargest(nums2, k2))
