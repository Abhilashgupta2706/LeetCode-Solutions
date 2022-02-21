num1 = [2, 0, 2, 1, 1, 0]
num2 = [2, 0, 1]


class Solution:
    def sortColors(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place insteaAd.
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums


print(Solution.sortColors(num1))
print(Solution.sortColors(num2))
