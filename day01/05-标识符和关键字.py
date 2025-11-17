"""
标识符解释：
    概述：
        就是用来给类、函数、变量等起名字的规则和规范。
    命名规则：
        1. 必须由英文字母、数字、下划线组成，且数字不能开头。
        2. 区分大小写。
        3. 最好做到见名知意，虽然这个是规范，但是要当规则用。
        4. 不能和关键字重名

    常用命名规范：
        大驼峰命名法，也叫双驼峰命名法
            要求：
                每个单词的首字母都大写，其他全部小写。
            例如：HelloWorld

        小驼峰命名法，也叫单驼峰命名法
            要求：
                从第2个单词开始，每个单词的首字母都大写，其他全部小写
            例如：hellowWorld,maxValue
        蛇形命名法，
            要求：
                单词间用下划线隔开
            例如：
                MAX_VALUE,max_valve
        串行命名法， python不支持
            要求：
                单词间用中划线隔开
            例如：
                MAX-VALUE
关键字：
    概述：
        被python赋予了特殊含义的单词。
    特点：
        常见的编辑器针对关键字都会高亮显示。
    常见的关键字如下：
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
        'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
        'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
        'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

"""

# 1. 演示： 不符合 见名知意 规范的 变量名
age = "张三"
print(age)

# 2. 演示 python中的关键字
import keyword   # 导入包
print(keyword.kwlist)  # key word list: 关键字列表