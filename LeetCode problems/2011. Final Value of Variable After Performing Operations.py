operation1 = ["--X", "X++", "X++"]
operation2 = ["++X", "++X", "X++"]
operation3 = ["X++", "++X", "--X", "X--"]


class Solution:
    def finalValueAfterOperations(operations: list[str]):
        x = 0
        for i in range(0, len(operations)):  # O(n)
            if operations[i] in ["X++", "++X"]:
                x += 1
            else:
                x -= 1
        return x


print(Solution.finalValueAfterOperations(operation1))
print(Solution.finalValueAfterOperations(operation2))
print(Solution.finalValueAfterOperations(operation3))
