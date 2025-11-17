"""
数据类型介绍：
    概述：
        数据类型指的是，变量值的类型，根据变量值不同，类型也不同，例如：int,float,bool,str
    常用的数据类型介绍：
        int     整形， 即：所有的整数
        float   浮点型，    即：所有的小数
        bool    布尔型，值比较特殊，只有True 和 False 两个值，分别表示：正确，错误
        str     字符串，值比较特殊，值必须用引号包裹，单双引号均可

"""
# 1. 定义变量a,b,c,d 分别存储上述的4种值。
a = 11
b = 13.3
c = True
d = '邓紫棋'

# 细节：多行字符串，必须写成三引号形式，单双引号均可。
f = """
select
    *
from
    student;
"""

# 2.打印上述的变量值
print(a)
print(b)

# 3.细节，python独有写法，同时输出多个变量值。
print(a,b,c,d)

print(f)    # 发现： 三引号会保留字符串格式，一般用在传输json、传输数据时使用

# 4.通过type()函数，可以查看变量值的数据类型
# 格式：type(变量名 或者 变量值)
print(type(11))
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'bool'>
print(type(d))  # <class 'str'>



