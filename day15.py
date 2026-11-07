# lambda的用法:   lambda是匿名函数，lambda x: x**2表示一个函数，输入x，返回x的平方
# import random
# import time

def download(a):
    """下载文件"""
    print(f'开始下载{a}.')
    time.sleep(random.random() * 6)
    print(f'{a}下载完成.')

    
def upload(filename):
    """上传文件"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')

# start = time.time()
# download('MySQL从删库到跑路.avi')
# end = time.time()
# print(f'花费时间: {end - start:.2f}秒')
# start = time.time()
# upload('Python从入门到住院.pdf')
# end = time.time()
# print(f'花费时间: {end - start:.2f}秒')

import time
import random

def record_time(func):

    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        # 返回被装饰函数的返回值
        return result
    
    return wrapper
download = record_time(download)
upload = record_time(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')