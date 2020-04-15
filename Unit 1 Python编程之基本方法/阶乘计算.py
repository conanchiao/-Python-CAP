# 阶乘注释
'''
阶乘：n!=1*2*3*...*(n-1)*n
0!=1
n!=(n-1)!*n
'''
sum, tmp=0,1
for i in range(1,11):
    tmp*=i
    sum+=tmp
print("运算结果是：{}".format(sum))

