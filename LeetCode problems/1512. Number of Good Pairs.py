num1 = [1, 2, 3, 1, 1, 3]
num2 = [1, 1, 1, 1]
num3 = [1, 2, 3]


class Solution:
    def numIdenticalPairs(nums: list[int]):
        count = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count
        #  O(N)


print(Solution.numIdenticalPairs(num1))
print(Solution.numIdenticalPairs(num2))
print(Solution.numIdenticalPairs(num3))
