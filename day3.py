#如果if条件成立的情况下需要执行多条语句，只要保持多条语句具有相同的缩进就可以了
# python中缩进很重要，相同缩进代表相同的代码块
# a=1
# print('a =', a)///////
# height = float(input('身高(cm)：'))
# weight = float(input('体重(kg)：'))
# bmi = weight / (height / 100) ** 2
# print(f'{bmi = :.1f}')
# if 18.5 <= bmi < 24:
#     print('你的身材很棒！')
# else:
    # print('你的身材不够标准哟！')   
    # status_code = int(input('响应状态码: '))
# match status_code:
    # case 400 | 405: description = 'Invalid Request'
    # case 401 | 403 | 404: description = 'Not Allowed'
    # case 418: description = 'I am a teapot'
    # case 429: description = 'Too many requests'
    # case _: description = 'Unknown Status Code'
# print('状态码描述:', description)///////
# #####match-case语句是python3.10版本新增的语法，类似于其他语言中的switch-case语句,见上
# print(f'周长为:{perimeter:.2f}')
# import time

# print('hello, world')
# time.sleep(3)  # 是暂停3秒
# range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长（跨度），即每次递增的值，101取不到。   相当于左开右闭区间[1, 101)。
# range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长（跨度），即每次递减的值，0取不到。

total = 0
for i in range(2, 101, 2):
    total += i
print(total)