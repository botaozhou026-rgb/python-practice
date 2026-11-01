# languages = ['Python', 'Java', 'C++']
# languages.append('JavaScript')
# print(languages)  # ['Python', 'Java', 'C++', 'JavaScript']
# languages.insert(1, 'SQL')
# print(languages)  # ['Python', 'SQL', 'Java', 'C++', 'JavaScript']


# # 列表.remove()方法用于删除列表中指定的元素
# languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
# if 'Java' in languages:
#     languages.remove('Java')
# if 'Swift' in languages:
#     languages.remove('Swift')
# print(languages)  # ['Python', 'SQL', C++', 'JavaScript']
# languages.pop()// 删除列表中的最后一个元素
# temp = languages.pop(1)  # 删除索引为1的元素，并将其赋值给temp
# print(languages)  # ['Python', 'C++']
# //append insert:加     remove pop del:删

# languages = ['Python', 'SQL', 'C++', 'JavaScript','python']
# languages.remove('python')
# print(languages)


# items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
# print(items.index('Python'))     # 0
# # 从索引位置1开始查找'Python'
# print(items.index('Python', 1))  # 5


# items = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
# items.sort()
# print(items)  # ['C++', 'Java', 'Kotlin', 'Python', 'Swift']
# items.reverse()
# print(items)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']//reverse:反转列表


# items=[]
# for i in range(1,101):
#     if(i%3==0 or i%5==0):
#         items.append(i)
# print(items)

# 或者
# items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
# print(items)


# nums1 = [1, 2, 3, 4, 5]
# nums2 = []
# for num in nums1:
#      s=num**2
#      nums2.append(s)
# print(nums2)  # [1, 4, 9, 16, 25]


# scores = []
# for _ in range(5):
#     temp = []
#     for _ in range(3):
#         score = int(input('请输入: '))
#         temp.append(score)
# #     scores.append(temp)
# # print(scores)


# import random
# scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
# print(scores)


# import random
# red_balls = list(range(1, 34))
# selected_balls = []
# # 添加6个红色球到选中列表
# for _ in range(6):
#     # 生成随机整数代表选中的红色球的索引位置
#     index = random.randrange(len(red_balls))
#     # 将选中的球从红色球列表中移除并添加到选中列表
#     selected_balls.append(red_balls.pop(index))
# # 对选中的红色球排序
# selected_balls.sort()
# # 输出选中的红色球
# for ball in selected_balls:
#     print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# # 随机选择1个蓝色球
# blue_ball = random.randrange(1, 17)
# # 输出选中的蓝色球
# print(f'\033[034m{blue_ball:0>2d}\033[0m')
# # //30代表黑色,31代表红色,32代表绿色,33代表黄色,34代表蓝色,35代表紫色,36代表青色,37代表白色


