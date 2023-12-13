from Easyrex import *
import re



if __name__=="__main__":
    expression=Expression("abc")
    expression=expression.repeat(10,"greedy")
    print(expression)

    expression=Expression("abc")
    expression=expression.repeat((10,20),"greedy")
    print(expression)

    expression=Expression("abc")
    expression=expression.repeat("+","Lazy")
    print(expression)

    expression=Expression("abc")
    expression=expression.repeat("+","possessive")
    print(expression)