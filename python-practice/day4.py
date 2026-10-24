# total=0
# i=1 
# while i<=100: 
#   total+=i
#   i+=1
# print(total)


# i=0
# total=0
# while i<=100:
    # total+=i
    # i+=2
# print(total)



# total = 0
# i = 2
# while True:
    # total += i
    # i += 2
    # if i > 100:
        # break
# print(total) 


# total=0
# for i in range(1,101):
#     if i%2==0:
#         total+=i
# print(total)缩进在python中非常重要


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{i}*{j}={i*j}',end='\t')
#     print()


# num =int(input("请输出一个整数；"))
# end = int(num**0.5)
# kk = True
# for kk in range(2,end+1):
#     if num%kk==0:
#         kk = False
#         break
# if kk:
#     print(f'{num}是素数')
# if not kk:
#     print(f'{num}不是素数')
  
# x=int(input("x="))
# y=int(input("y="))
# for l in range(x,0,-1):
#     if x%l == 0 and y%l == 0:
#       print(l)
#       break


# x=int(input("x="))
# y=int(input("y="))
# while y%x!=0:
#     x,y=y%x,x
# print(f'最大公约数: {x}')


# for i in range(2, 100):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break           
#     else:       
#            print(i)


# i,j=0,1
# for _ in range(20):
#     i,j=j,i+j
#     print(i,end=' ')


# N= int(input("请输出一个整数N:"))
# for i in range(100,1000):
#     sum=0   
#     mu=i
#     for _ in range(N):
#         s=mu%10
#         sum+=(s**N)
#         mu=mu//10
#     if sum==i:
#         print(i,end=' ')


# import time
# for i in range(10,-1,-1):
#    print(i,end=' ',flush=True)
#    time.sleep(2)
        
    










































