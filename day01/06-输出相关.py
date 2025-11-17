"""
输出介绍：
    概述：
        python中的输出函数指的是print()函数，它可以把小括号中的内容输出到控制台。
    格式：
        print(变量值 或者 变量)
    分类，即：常用的输出的写法
        1. 输出单个值
        2. 同时输出多个值
        3. 换行输出和不换行输出
        4. 格式化输出 ---> 占位符输出
        5. 格式化输出 ---> 插值表达式


"""
# 定义多个变量值
name = "阿童木"
age = 18
salary = 28888
flag = False # 是否是正面人物，True: 是，False 不是

# 演示 1. 输出单个值。
print('我的的姓名是' + name)
# print('我的的年龄是' + age)   # 报错，Python中字符串和整数不能进行加法运算

# 演示 2. 同时输出多个值
print('-' * 35)
print(name,age,salary,flag)

print('-' * 35)

# 演示 3. 换行输出 和 不换行输出
print('hello')
print('world')

# 上述的代码，完整写法如下
print('hello',end='\n')    # end = '\n'，是程序默认给print()函数添加的，即换行输出。
print('world', end='\n')

print('hello',end='\t')
print('world',end='')

# 不换行输出
print('hello',end='')
print('world')

# 换行输出
print('hello\nworld')  # \n \t  \' \" 这些都是转义符，有特的函数

# 转义符演示
print("I'm Tom!")
print('I\'m Tom!')

print('-' * 35)

# 演示 4. 格式化输出 ---> 占位符方式,   规则：%s ---> 字符串，%d ---> 整数， %f ---> 小数
print('我叫%s' % name)    #一个占位符写法
print('我叫%s,今年%d岁了，我的工资是%f，你猜我是反派吗？ %s' % (name, age, salary, flag))    # 多个占位符的写法

# 占位符的特殊写法： %5d ---> 期望得到5位数的整数，不够前面补空格， %05d ---> 期望得到5位数的整数，不够前面补0
# %.2f ---> 保留两位小数，会进行四舍五入。
print('我叫%s,今年%d岁了，我的工资是%.3f,你猜我是反派吗？%s' % (name, age, salary, flag))       # 多个占位符的写法
print('我叫%s,今年%05d岁了，我的工资是%.2f,你猜我是反派吗？%s' % (name, age, salary, flag))     # 多个占位符的写法

# 特殊写法：两个% ---> % 即：%% ---> %, 一般用于显示比例
print('我叫%s,今年%05d岁了,我的工资是%.2f,我的成绩全班排名前3%% ' % (name, age, salary))


# 演示 5. 格式化输出 ---> 插值表达式  格式： f'正常写你的内容{变量名}'
print(f'我叫{name},今年{age}岁了，我的工资是{salary}')
print(f'我叫{name},今年{age:05d}岁了，我的工资是{salary:.3f}')





