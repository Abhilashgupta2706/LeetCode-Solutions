my_list1 = [1, 2, 3, 4]
my_list2 = [1, 1, 1, 1, 1]
my_list3 = [3, 1, 2, 10, 1]


class Solution:
    def runningSum(list: list[int]):
        final_list = []
        Solution.logic(list, final_list)
        return final_list

    def logic(my_list, opList):
        if len(my_list) == 1:
            value = my_list[0]
            opList.append(value)
            return value
        else:
            recursion = my_list[-1] + Solution.logic(my_list[:-1], opList)
            opList.append(recursion)
            return recursion


print(Solution.runningSum(my_list1))
print(Solution.runningSum(my_list2))
print(Solution.runningSum(my_list3))
