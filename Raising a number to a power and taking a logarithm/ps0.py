
#Problem Set 0
import math

x=int(input("Enter number x: "))
y=int(input("Enter number y: "))

def result(x,y):
    power=x**y
    logarithm=math.log2(x)
    print("x**y =",power)
    print("log(x) =",logarithm)

result(x,y)
