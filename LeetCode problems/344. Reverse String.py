def reverseString(str: list[str]) -> None:
    start, end = 0, len(str) - 1
    while start < end:
        str[start], str[end] = str[end], str[start]
        start += 1
        end -= 1
    print(str)


my_str = ["h", "e", "l", "l", "o"]
reverseString(my_str)
