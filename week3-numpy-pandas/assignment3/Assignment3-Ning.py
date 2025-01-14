# Assignment 3 Ning
# 注意 - Copy this file and rename as assignment3_{first_name}.py then complete code with a PR.

# Q1.
"""
请实现 2个python list 的 ‘cross product’ function.（向量叉乘）
要求按照Numpy 中cross product的效果: https://numpy.org/doc/stable/reference/generated/numpy.cross.html
只实现 1-d list 的情况即可.

x = [1, 2, 0]
y = [4, 5, 6]
cross(x, y)
> [12, -6, -3]
"""


def cross_product(x: list, y: list) -> list:
    z1 = x[1] * y[2] - x[2] * y[1]
    z2 = x[2] * y[0] - x[0] * y[2]
    z3 = x[0] * y[1] - x[1] * y[0]
    return [z1, z2, z3]


assert cross_product([1, 2, 0], [4, 5, 6]) == [12, -6, -3]

'''
import inspect
source_code = inspect.getsource(np.cross)
print(source_code)
'''

# Q2.
"""
交易传输指令经常需要验证完整性，比如以下的例子
{ 
    request : 
    { 
        order# : 1, 
        Execution_details: ['a', 'b', 'c'],
        request_time: "2020-10-10T10:00EDT"
    },
    checksum:1440,
    ...
}
可以通过很多种方式验证完整性，假设我们通过判断整个文本中的括号 比如 '{}', '[]', '()' 来判断下单是否为有效的。
比如 {{[],[]}}是有效的，然而 []{[}](是无效的。 
写一个python 程序来进行验证。
 def checkOrders(orders: [str]) -> [bool]:
 return a list of True or False.
checkOrders(["()", "(", "{}[]", "[][][]", "[{]{]"]) return [True, False, True, True, False]
"""


def checkOrders(orders: [str]) -> [bool]:
    TFL = list()
    for o in orders:
        if not (o.count("(") == o.count(")") and o.count("[") == o.count("]") and o.count("{") == o.count("}")):
            TFL.append(False)
        else:
            osc = [1, o]
            j = 1
            while osc[j] != osc[j - 1]:
                for i in range(0, len(o) - 1):
                    if (o[i] == "(" and o[i + 1] == ")") or (o[i] == "[" and o[i + 1] == "]") or (
                            o[i] == "{" and o[i + 1] == "}"):
                        list_str = list(o)  # 将字符串转换为列表
                        list_str.pop(i)
                        list_str.pop(i)
                        o = ''.join(list_str)  # 再将列表转换成字符串
                        break
                osc.append(o)
                j += 1
            TFL.append(not bool(o))
    return TFL


assert checkOrders(["()", "(", "{}[]", "[][][]", "[{]{]", "[]{[}]("]) == [True, False, True, True, False, False]

'''
o = "abc"
a = [1, o]
print(a)
print(type(a))
'''

# Q3
"""
我们在进行交易的时候通常会选择一家broker公司而不是直接与交易所交易。
假设我们有20家broker公司可以选择 (broker id is 0...19)，通过一段时间的下单表现(完成交易的时间)，我们希望找到最慢的broker公司并且考虑与其解除合约。
我们用简单的数据结构表达broker公司和下单时间: [[broker id, 此时秒数]]
[[0, 2], [1, 5], [2, 7], [0, 16], [3, 19], [4, 25], [2, 35]]
解读: 
Broker 0 使用了0s - 2s = 2s
Broker 1 使用了5 - 2 = 3s
Broker 2 使用了7 - 5 = 2s
Broker 0 使用了16 - 7 = 9s
Broker 3 使用了19 - 16=3s
Broker 4 使用了25 - 19=6s
Broker 2 使用了35 - 25=10s
综合表现，是broker2出现了最慢的交易表现。

def slowest(orders: [[int]]) -> int:

slowest([[0, 2], [1, 5], [2, 7], [0, 16], [3, 19], [4, 25], [2, 35]]) return 2
"""


def slowest(orders: [[int]]) -> int:
    s = orders[0]
    for i in range(2, len(orders)):
        if (orders[i][1] - orders[i - 1][1]) > s[1]:
            s = [orders[i][0], orders[i][1] - orders[i - 1][1]]
    return s[0]


assert slowest([[0, 2], [1, 5], [2, 7], [0, 16], [3, 19], [4, 25], [2, 35]]) == 2

# Q4
"""
判断机器人是否能返回原点

一个机器人从平面(0,0)的位置出发，他可以U(向上), L(向左), R(向右), 或者D(向下)移动一个格子。
给定一个行走顺序，问是否可以回到原点。

例子
1. moves = "UD", return True.
2. moves = "LL", return False.
3. moves = "RRDD", return False.
4. moves = "LDRRLRUULR", return False.

def judgeRobotMove(moves: str) -> bool:

"""


def judgeRobotMove(moves: str) -> bool:
    return moves.count("U") == moves.count("D") and moves.count("R") == moves.count("L")


assert judgeRobotMove("UD")
assert not judgeRobotMove("LL")
assert not judgeRobotMove("RRDD")
assert not judgeRobotMove("LDRRLRUULR")

# Q5
"""
写一个验证email格式的程序， 对于给定的string监查是不是一个email地址:
1. 必须只包含小写字母(97-122)，"-"(45), "/" (47), "."(46) , "_"(95) 和数字(48-57)
2. 有且仅有一个"@": email.count("@") == 1
3. @之前之后不能为空: bool(email.partition(email[:-4])) == 1
4. 以 ".edu" 或 ".com" 结尾: email[-4:] == ".edu" or ".com"

可以使用regex或者python标准包的方法。
"""


# import re: re包没学会


def isEmail(email: str) -> bool:
    legal_ascii = list(range(45, 58))
    legal_ascii.extend((95, 64))
    legal_ascii.extend(list(range(97, 123)))
    con1 = True
    i = 0
    while i < len(email) and con1 == True:
        if ord(email[i]) in legal_ascii:
            con1 = True
        else:
            con1 = False
        i += 1
    con2 = email.count("@") == 1 and bool(email.partition(email[:-4])) == 1
    con4 = email[-4:] == ".edu" or email[-4:] == ".com"
    return con1 == con2 == con4 == 1


assert isEmail("160/1588/156@qq.com")
assert isEmail("missxu-xn@163.com")
assert isEmail("ning_xxn@163.com")
assert not isEmail("ning@xxn@163.com")
assert not isEmail("ning$xxn@163.com")