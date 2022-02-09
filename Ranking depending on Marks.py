# l1 = list(input())
lst = [4, 6, 7, 8, 9, 9, 9, 10, 10, 15]
print("Before reversing:", lst)
lst = lst[::-1]
print("After reversing:", lst)
count = 1
result = []

print("------------------------------------------------------------------------------------------------")

print(count, end=" ")
for i in range(1, len(lst) - 1):
    if lst[i] != lst[i - 1]:
        count += 1
    print(count, end=" ")

print(count + 1, end=" ")

print("\n------------------------------------------------------------------------------------------------")

# def ReverseList(lst):
#     lst.reverse()
#     return lst[::-1]
#
#
# print(ReverseList(l1))
