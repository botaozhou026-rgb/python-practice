# print("\'hello, world!\'")


# s2 = '!' * 3
# print(s2)    # !!!



# print("",'A'<'a')  #True



# print(ord('骆'))            # 39558,字也对应数字



# s1 = 'a whole new world'
# s2 = 'hello world'
# print(s1 < s2)              # True，看第一个字母


# s1 = 'hello, world!'
# # 字符串首字母大写
# print(s1.capitalize())  # Hello, world!
# # 字符串每个单词首字母大写
# print(s1.title())       # Hello, World!
# # 字符串变大写
# print(s1.upper())       # HELLO, WORLD!
# s2 = 'GOODBYE'
# # 字符串变小写
# print(s2.lower())       # goodbye
# # 检查s1和s2的值
# print(s1)               # hello, world
# print(s2)               # GOODBYE


# s = 'hello world!'
# print(s.find('or', 9))   # -1  这里的九代表索引九,find作用和index差不多
# # 逆向查找  rfind，rindex


# s1 = 'hello, world!'
# print(s1.startswith('He'))   # False
# print(s1.startswith('hel'))  # True
# print(s1.endswith('!'))      # True
# s2 = 'abc123456'
# print(s2.isdigit())  # False
# print(s2.isalpha())  # False
# print(s2.isalnum())  # True
# 说明：上面的isdigit用来判断字符串是不是完全由数字构成的，isalpha用来判断字符串是不是完全由字母构成的，这里的字母指的是 Unicode 字符但不包含 Emoji 字符，isalnum用来判断字符串是不是由字母和数字构成的。
# 格式化


# s1 = '   jackfrued@126.com  '
# print(s1.strip())      # jackfrued@126.com
# s2 = '~你好，世界~'
# print(s2.lstrip('~'))  # 你好，世界~
# print(s2.rstrip('~'))  # ~你好，世界



s = 'I love you'
words = s.split()
print(words)            # ['I', 'love', 'you']
print('~'.join(words))  # I~love~you


a = '骆昊'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)                  # b'\xe9\xaa\x86\xe6\x98\x8a'
print(c)                  # b'\xc2\xe6\xea\xbb'
print(b.decode('utf-8'))  # 骆昊
print(c.decode('gbk'))    # 骆昊