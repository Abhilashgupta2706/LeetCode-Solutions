sentences1 = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
sentences2 = ["please wait", "continue to fight", "continue to win"]
sentences3 = ["w jrpihe zsyqn l dxchifbxlasaehj", "nmmfrwyl jscqyxk a xfibiooix xolyqfdspkliyejsnksfewbjom",
              "xnleojowaxwpyogyrayfgyuzhgtdzrsyococuqexggigtberizdzlyrdsfvryiynhg",
              "krpwiazoulcixkkeyogizvicdkbrsiiuhizhkxdpssynfzuigvcbovm",
              "rgmz rgztiup wqnvbucfqcyjivvoeedyxvjsmtqwpqpxmzdupfyfeewxegrlbjtsjkusyektigr",
              "o lgsbechr lqcgfiat pkqdutzrq iveyv iqzgvyddyoqqmqerbmkxlbtmdtkinlk",
              "hrvh efqvjilibdqxjlpmanmogiossjyxepotezo", "qstd zui nbbohtuk", "qsdrerdzjvhxjqchvuewevyzlkyydpeeblpc"]


class Solution:
    def mostWordsFound(sentences: list[str]):
        count = 0
        counts = []
        for i in range(0, len(sentences)):  # O(N)
            for j in sentences[i].split():  # O(N)
                count += 1
            counts.append(count)
            count = 0

        max_value = counts[0]
        for total in counts:  # O(N)
            if total > max_value:
                max_value = total
        return max_value
        #  TC: O(N)


print(Solution.mostWordsFound(sentences1))
print(Solution.mostWordsFound(sentences2))
print(Solution.mostWordsFound(sentences3))
