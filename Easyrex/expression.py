
from typing import Literal

class Expression():
    # word=Expression("\w+")
    # digits=Expression("\d+")
    def __init__(self,base_expression:str,name:str=None,grouped=False) -> None:
        self.name=name 
        self.base_expression=base_expression
        self.grouped=grouped

    def ensure_expression(expression):
        assert type(expression)==Expression or type(expression)==str ,"addition is accepted only between str and Expressions"
        if type(expression)==str:
            return Expression(expression)
        return expression

    def enforce_expression_parameters(f):
        def func(*args,**kwargs):
            new_args=[]
            for i,arg in enumerate(args):
                new_args.append(Expression.ensure_expression(arg))

            for key in kwargs.keys():
                kwargs[key]=Expression.ensure_expression(kwargs[key])
            return f(*new_args,*kwargs)
        return func


    def get_expression(self):
        return self.base_expression

    def group(a,name=None):
        a=Expression.ensure_expression(a)
        if name==None:
            return "(?:%s)"%a.get_expression()
        if type(name)==str:
            if name=="":
                return Expression("(%s)"%a.get_expression(),grouped=True) 
            return Expression("(?P<%s>%s)"%(name,a.get_expression()),grouped=True)
        raise Exception("exprected name type to be None or str")
    
    def repeat(self,method:Literal["greedy","non_greedy","possessive"]="greedy"):
        a=Expression.ensure_expression(a)
        
        return 
    
    @enforce_expression_parameters
    def __add__(a, b):
        return Expression("%s%s"%(a.get_expression(),b.get_expression()))
    
    @enforce_expression_parameters
    def __or__(a:Exception, b:Exception):
        return Expression.group("%s|%s"%(a.get_expression(),b.get_expression()))

    def __str__(self):
        return self.base_expression