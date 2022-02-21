num1, n1 = [2, 5, 1, 3, 4, 7], 3
num2, n2 = [1, 2, 3, 4, 4, 3, 2, 1], 4
num3, n3 = [1, 1, 2, 2], 2


class Solution:
    def shuffle(nums: list[int], n: int):
        temp = []
        for i in range(n):
            temp.append(nums[i])
            temp.append(nums[i + n])
        return temp
        # O(N)


print(Solution.shuffle(num1, n1))
print(Solution.shuffle(num2, n2))
print(Solution.shuffle(num3, n3))
