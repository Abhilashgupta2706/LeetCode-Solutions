accounts1 = [[1, 2, 3], [3, 2, 1]]
accounts2 = [[1, 5], [7, 3], [3, 5]]
accounts3 = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]


class Solution:
    def buildArray(accounts):
        temp = []

        for i in accounts:
            total = 0
            for j in i:
                total += j
            temp.append(total)

        # Now checking the maximum value in temp
        max_value = temp[0]
        for i in temp:
            if i > max_value:
                max_value = i

        return max_value


print(Solution.buildArray(accounts1))
print(Solution.buildArray(accounts2))
print(Solution.buildArray(accounts3))
