"""The expression module: implements the EasyRex representation for a regular expression

"""

from typing import Literal

class Expression():
    """The EasyRex representation of a regular expression.

    defines operations between Expressions and strings.
    """

    # word=Expression("\w+")
    # digits=Expression("\d+")
    def __init__(self,base_expression:str,name:str=None,grouped=False) -> None:
        self.name=name
        self.base_expression=base_expression
        self.grouped=grouped
    @staticmethod
    def ensure_expression(expression):
        """Checks and makes sure that the expression is an instance of Expression
        
        Keyword arguments:
        expression -- the expression to be checked
        Return: an instance of Expression
        """

        assert isinstance(expression,(Expression,str)),"operations are accepted between str and Expressions only"
        if isinstance(expression,str):
            return Expression(expression)
        return expression

    @staticmethod
    def enforce_expression_parameters(f):
        """Decorator that makes sure that arguments are of type Expression
        """
        def func(*args,**kwargs):
            new_args=[]
            for _,arg in enumerate(args):
                new_args.append(Expression.ensure_expression(arg))

            for key in kwargs:
                kwargs[key]=Expression.ensure_expression(kwargs[key])
            return f(*new_args,*kwargs)
        return func


    def get_expression(self):
        """returns the final expression
        
        Keyword arguments:
        Return: a string representing the final regular expression
        """
        return self.base_expression

    @staticmethod
    def group(a,name=None):
        """Puts an Expression in a group
        
        Keyword arguments:
        name -- The name of the group in case of a named group, None otherwise.
        Return: returns the grouped Expression.
        """

        a=Expression.ensure_expression(a)
        if name is None:
            return "(?:%s)"%a.get_expression()
        if isinstance(name,str):
            if name=="":
                return Expression("(%s)"%a.get_expression(),grouped=True) 
            return Expression("(?P<%s>%s)"%(name,a.get_expression()),grouped=True)
        raise ValueError("exprected name type to be None or str")

    @enforce_expression_parameters
    def repeat(self,method:Literal["greedy","non_greedy","possessive"]="greedy"):
        """Repeats the Expression based on the chosen method
        
        Keyword arguments:
        method -- the method used for the repitition.
        Return: the resulting Expression.
        """

        if method=="greedy":
            return Expression(self.group(self.get_expression())+"*")
        if method=="non_greedy":
            return Expression(self.group(self.get_expression())+"*?")
        if method=="possessive":
            return Expression(self.group(self.get_expression())+"*+")

        return self

    @enforce_expression_parameters
    def __add__(self, b):
        return Expression("%s%s"%(self.get_expression(),b.get_expression()))

    @enforce_expression_parameters
    def __or__(self:Exception, b:Exception):
        return Expression.group("%s|%s"%(self.get_expression(),b.get_expression()))

    def __str__(self):
        return self.base_expression
