"""
类型转换解释：
    概述：
        就是用来把 某个类型的值 转成 其他类型的值。
    涉及到的函数：
        int()       把字符串形式的整数 或者 float类型的小数，转成 整数，可能会丢失精度（慎用）
        float()     把字符串形式的小数 或者 int类型的整数，转成 小数。
        str()       把整数 或者 小数，转成 字符串
        bool()      把值转成布尔类型的值， 0 -> False  非零 -> True
        eval()      相当于去掉引号，是什么就是什么。
                    例如：'10'-> 10, '10.3' -> 10.3, 'True' -> True, 'name' -> name 变量，如果没有这个变量就会报错。
"""

# 1. 演示 int()   # 把字符串形式的整数或者float类型的小数，转成整数，可能会丢失精度（慎用）
print(int(10.3))
print(int('20'))
# print(int('10.3'))    # 报错

# 2. 演示 float()  # 把字符串形式的数字或者int类型的整数，转成小数。
print(float('10'))
print(float('20.3'))


# 3. 演示 str()   # 把整数或者小数，转成字符串。
print(str(10))
print(str(10.3))

# 4. 演示 bool()  # 把值转成布尔类型的值，   0 ---> False,   非零 ---> True
print(bool(0))  # False
print(bool(1))  # True
print(bool(1.2))    # True
print(bool('张三'))   # True

# 5. 演示 eval()     # 相当于去掉引号，是什么就是什么
print(eval('10'))
print(eval('10.3'))
print(eval('True'))
name = 'mask'
print(eval('name'))   # 相当于去掉'name'的引号，name就不是字符串了，而是变量名。

print(type(eval('10')))
print(type(eval('10.3')))
print(type(eval('True')))

