my_list1 = [0, 2, 1, 5, 3, 4]
my_list2 = [5, 0, 1, 2, 3, 4]


class Solution:
    def buildArray(nums: list[int]):
        ans = []
        for i in range(0, len(nums)):
            value = nums[nums[i]]
            ans.append(value)
        return ans


print(Solution.buildArray(my_list1))
print(Solution.buildArray(my_list2))
