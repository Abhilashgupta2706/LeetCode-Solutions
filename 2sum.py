# def twoSum(ls, target):
#     indexList = []
#     for i in range(0, len(ls)-1):
#         for j in range(i+1, len(ls)):
#             if(ls[i]+ls[j] == target):
#                 indexList.append(i)
#                 indexList.append(j)
#     return indexList


# ls = [3, 2, 4]
# target = 6

# print(twoSum(ls, target))


class Logic:
    def search(nums, item):
        for i in range(0, len(nums)):
            return i


class Solution:
    def twoSum(nums, target):
        ls = nums
        ls.sort()
        ns = []
        i = 0
        j = len(ls)-1
        while(i < j):
            if(ls[i]+ls[j] > target):
                j -= 1
            elif(ls[i]+ls[j] == target):
                ns.append(i)
                ns.append(j)
                i += 1
                j -= 1
            else:
                i += 1

        l = Logic()
        f = l.search(nums, ls[ns[0]])
        s = l.search(nums, ls[ns[1]])

        ns[0] = f
        ns[1] = s

        print(ns)


nums = [3, 2, 4]
target = 6

sol = Solution()
sol.twoSum(nums, target)

# TypeError: twoSum() takes 2 positional arguments but 3 were given
