"""
比较运算符：
    概述：
        就是用来做比较操作的，也称之为：关系运算符。
        无论比较表达式简单还是复杂，其结果必定是：布尔值，要么True,要么Fals。
    分类：
        >, >=,<,<=,==,!=

    细节：
        不要把 == 写成 = ,一个= 是赋值，两个= 是比较.


逻辑运算符：
    概述：
        它适用于 多条件的判断，即同时满足多个条件，还是满足多个条件的任意一个条件，还是取反等操作。
        分类：
            and     逻辑与，并且的意思，即：有False则整体为False.
            or      逻辑或，或者的意思，即：有True则整体为True.
            not     逻辑非，取反的意思，即：False -> 取反后，True, True -> 取反后 False.
        细节：
            1. 逻辑运算符主要操作的是关系表达式，但是它也可以操作数字， 例如：10 and 5
            2. 逻辑运算符操作的小技巧：你把0当作False,非0当作True即可.

"""

# 案例1：演示比较运算符。
a, b = 10, 3
print(a > b)    # True
print(a >= b)   # True
print(a < b)    # False
print(a <= b)   # False
print(a == b)   # False
print(a != b)   # True
print(5 >= 5)   # True

# 案例2: 演示 逻辑运算符。
print(a > 5 and b <= 3 )

# 演示 and     逻辑与，并且的意思，即：有False则整体为False.
print(True and True)    #   True
print(True and False)   #   False
print(False and True)   #   False
print(False and False)  #   False

# 演示 or      逻辑或，或者的意思，即：有True则整体为True.
print(True or True)    #   True
print(True or False)   #   True
print(False or True)   #   True
print(False or False)  #   False

# 演示 not     逻辑非，取反的意思，即：False -> 取反后，True, True -> 取反后 False.
print(not True)         #   False
print(not False)        #   True
print(not not False)    #   False,同一个值，偶数次取反，该数值不变

# 扩展：逻辑运算符操作数字，小技巧：你把0当作False,非0当作True即可。
# 逻辑与操作数字，结论（技巧）：有0则0（即：有False则整体为False),否则取最后1个（非0）数字。
print(10 and 0 and 5)   # 0
print(0 and 3 and 5)    # 0
print(10 and 3 and 5)   # 5
print(0 and 0 and 0)    # 0
    # 0

# 逻辑或操作数字，结论（技巧）：有非0则非0（即：有True则整体为True），否则取第一个（非0）数字。
print(0 or 0 or 0)      # 0
print(10 or 0 or 5)     # 10
print(0 or 3 or 5)      # 3
print(10 or 3 or 5)     # 10
