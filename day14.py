#                   函数使用
# 求和
# def he(*intd,**floatd):
#     zong=list(intd)+list(floatd.values())
#     return sum(zong)
# a=he(1,2,3,a=1)
# print(a)
# 转list的原因是让*intd和**floatd.values()都变成列表，然后合并成一个列表zong，最后求和。

# 高阶用法
# def calc(init_value, op_func, *args, **kwargs):               ///init_value, op_func分别是初始值和符号，*args和**kwargs是可变参数
#     items = list(args) + list(kwargs.values())
#     result = init_value
#     for item in items:
#         if type(item) in (int, float):
#             result = op_func(result, item)
#     return result
# def add(x, y):
#     return x + y


# def mul(x, y):
#     return x * y
#1 print(calc(0, add, 1, 2, 3, 4, 5))  # 15          
#1 print(calc(1, mul, 1, 2, 3, 4, 5))  # 120

# 2import operator
# print(calc(0, operator.add, 1, 2, 3, 4, 5))  # 15
# print(calc(1, operator.mul, 1, 2, 3, 4, 5))  # 120


# def guoliu(a)
#     return a%2==0
# def pingfang(a):
#     return a**2
# a=[1,2,3,4,5,6,7,8,9]
# print(list(map(pingfang,filter(guoliu,a))))  # [4, 16, 36, 64]

# old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
# new_strings = sorted(old_strings, key=len)                ////key=len表示按字符串长度排序
# print(new_strings)  # ['in', 'zoo', 'pear', 'apple', 'waxberry']


# old_nums = [35, 12, 8, 99, 60, 52]
# new_nums = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums)))      //相当于一个滚木，方便把函数嵌套起来
# print(new_nums)  # [144, 64, 3600, 2704]


