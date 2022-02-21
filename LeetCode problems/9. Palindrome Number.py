num1 = 121
num2 = -121
num3 = 10


class Solution:
    def isPalindrome(x: int):
        def reverseNum(num):
            rev = 0
            while num != 0:
                reminder = num % 10
                rev = rev * 10 + reminder
                num //= 10
            return rev

        if x < 0:
            return False

        if x == reverseNum(x):
            return True
        else:
            return False


print(Solution.isPalindrome(num1))
print(Solution.isPalindrome(num2))
print(Solution.isPalindrome(num3))
