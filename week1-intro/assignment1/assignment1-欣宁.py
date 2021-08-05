# Assignment 1 Ning
# This assignment is for exercising Python fundamental I and getting familiar with Python syntax.

# 注意 - Copy this file and rename as assignment1-{first_name}.py then complete code with a PR.

# Q1. Write a program which can compute the factorial of a given numbers.
# factorial 阶乘

def factorial(x: int) -> int:
    if x < 0:
        print("请输入一个正整数")
    elif x == 0:
        return int(1)
    else:
        x_fac = 1
        while x >= 1:
            x_fac = x_fac * x
            x -= 1
        return x_fac


assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(9) == 362880


# Q2. Write a program which take a num and print a str as the sum of all numbers from 1 to this number
# [1 + 2 + ... + x] and x is always >= 1.

# 法一：循环算法

def print_sum1(x: int) -> str:
    total = 0
    for i in range(x + 1):
        total += i
    return str(total)


# 没弄明白return""的用法


assert print_sum1(1) == "1"
assert print_sum1(3) == "6"
assert print_sum1(5) == "15"


# 法二：高斯求和公式

def print_sum2(x: int) -> str:
    total = (1 + x) * x / 2
    return str(int(total))


assert print_sum(1) == "1"
assert print_sum(3) == "6"
assert print_sum(5) == "15"


# Q3. Write a program to check is a year is leap year (x is always > 0)
# 能被400整除，或者能被4整除但不能被100整除的都是闰年，其余的年份均为平年

def is_leap_year(year: int) -> bool:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return 1
    else:
        return 0


# 对return不熟


assert is_leap_year(2000)
assert is_leap_year(1996)
assert not is_leap_year(1900)
assert not is_leap_year(2001)


# Q4. Write a program to convert a list of lowercase words to uppercase words.
# 法一：用upper()函数：
def to_upper_case(words: [str]) -> [str]:
    words_upper = []
    for word in words:
        words_upper.append("".join(word.upper()))
    return words_upper


# 不能直接upper，直接upper输出的是str

assert to_upper_case(["abc", "de"]) == ["ABC", "DE"]
assert to_upper_case(["Amazon", "Apple"]) == ["AMAZON", "APPLE"]


# 法二：用ASCII码
def to_upper_case2(words: [str]) -> [str]:
    words_upper = []
    for word in words:
        word_upper = []
        for letter in word:
            if 97 <= ord(letter) <= 122:  # 小写字母
                upper_letter = ord(letter) - 32  # 大小写字母之前差了32, chr()函数可以将编码数值转为字符（python没有字符的概念）
            else:
                upper_letter = ord(letter)
            word_upper.append(chr(upper_letter))
        words_upper.append("".join(word_upper))
    return words_upper


assert to_upper_case2(["abc", "de"]) == ["ABC", "DE"]
assert to_upper_case2(["Amazon", "Apple"]) == ["AMAZON", "APPLE"]


# Q5. Write a program to use only 'and' and 'or' to implement 'xor'
# https://baike.baidu.com/item/%E5%BC%82%E6%88%96/10993677?fromtitle=xor&fromid=64178

def xor(a: bool, b: bool) -> bool:
    if a != b:
        return True
    else:
        return False


assert not xor(True, True)
assert xor(True, False)
assert xor(False, True)
assert not xor(False, False)


# Q6. Write a Python program to display the current date and time under standard ISO 8601. e.g. 2021-12-03T10:15:30Z

def get_current_time() -> str:
    import time
    current_time = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime())
    return current_time


assert "T" in get_current_time()
assert "Z" in get_current_time()
assert 20 == len(get_current_time())


# Q7. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
# please define function and test yourself.

def special_sum(x: int, y: int) -> int:
    spe_sum: int = x + y
    if 15 <= spe_sum <= 20:
        return 20
    else:
        return spe_sum


assert special_sum(10, 5) == 20
assert special_sum(8, 10) == 20
assert special_sum(5, 5) == 10
assert special_sum(10, 20) == 30
