# m= int(input("m="))
# n= int(input("n="))
# s= m-n
# f1=1
# f2=1
# f3=1
# for i in range(1,m+1):
#     f1=f1*i
# for i in range(1,n+1):
#     f2=f2*i
# for i in range(1,s+1):
#     f3=f3*i
# num= f1/(f2*f3)
# print(num)

# 第二种
# def jie(n):
#         f = 1
#         for i in range(1,n+1):
#             f*=i
#         return f
# m= int(input("m="))
# n= int(input("n="))
# s= m-n
# print(jie(m)/(jie(n)*jie(s)))

# # 第三种
# from math import factorial
# m= int(input("m="))
# n= int(input("n="))
# print(factorial(m)/(factorial(n)*factorial(m-n)))

# 判断是否为三角形
def pan(a,b,c):
    return a+b>c and a+c>b and b+c>a
print(pan(a=3, b=4, c=5))
