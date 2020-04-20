# quadratic2.py
import math
def main():
    print("This program find the real solutions to a quadratic\n")
    a,b,c=eval(input("Please enter the coefficients(a,b,c): "))
    delta=b*b-4*a*c
    if delta>=0:
        delta=math.sqrt(delta)    #sqrt()开根号
        root1=(-b+delta)/(2*a)    #一元二次方程根=-b±根号dela/2a
        root2=(-b-delta)/(2*a)
        print("\nThe solutions are: ", root1, root2 )
    else:
        print("The equation has no real roots!")
main()
