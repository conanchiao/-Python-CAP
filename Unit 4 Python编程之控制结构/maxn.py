# maxn.py
# 寻找一组数中的最大值
def main():
    n=eval(input("How many numbers are there?"))
    max=eval(input("Enter a number >> "))    #将第一个值赋值给max
    for i in range(n-1):
        x=eval(input("Enter a number >> "))    #连续与后边n-1个值比较
        if x>max:
            max=x
        print("The largest value is ", max)
main()
