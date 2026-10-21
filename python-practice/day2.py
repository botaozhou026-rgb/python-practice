# print(0b100)#二进制
# print(0o100)#八进制
# print(0x100)#十六进制
# print(100)#十进制

# print(123.456)    # 数学写法
# print(1.23456e2)  # 科学计数法
a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
# print(ord('d'))         # str类型的'd'转成int，输出100
# print(chr(a))           # int类型的100转成str，输出'd'
# print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
# print(float(e))         # str类型的'123.45'转成float，输出123.45
# print(int(b))
# print((a:=19))#内部加括号是因为海象运算符的优先级低于print函数的优先级，起强调作用
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
# print('flag0 =', flag0)     # flag0 = True
# print('flag1 =', flag1)     # flag1 = True
# print('flag2 =', flag2)     # flag2 = False
# print('flag3 =', flag3)     # flag3 = False
# print('flag4 =', flag4)     # flag4 = True
# print('flag5 =', flag5)     # flag5 = False
# print(flag1 and not flag2)  # True
# print(1 > 2 or 2 == 3)      # False
# print('flag4 =', flag4)     # flag4 = True  or:只要有一个true就返回true，and:只要有一个false就返回false

# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度'%(f, c))//变量的格式  %（   ，  ，   ，  ，）
# perimeter = 2 * 3.1416 * radius
# area = 3.1416 * radius * radius
# print('周长: %.2f' % perimeter)
# print('面积: %.2f' % area)
# year = int(input('请输入年份: '))
# is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# print(f'{is_leap = }')
import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'周长: {perimeter:.2f}')
print(f'面积: {area:.2f}')