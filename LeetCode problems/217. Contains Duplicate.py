list1 = [1, 2, 3, 1]
list2 = [1, 2, 3, 4]
list3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]


class Solution:
    def containsDuplicate(nums: list[int]):
        counter = set()

        for num in nums:
            if num not in counter:
                counter.add(num)
            else:
                return True

        return False


print(Solution.containsDuplicate(list1))
print(Solution.containsDuplicate(list2))
print(Solution.containsDuplicate(list3))
