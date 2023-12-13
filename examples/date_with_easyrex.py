"""Example of utilization of EasyRex for the creation of a date regular expression.
"""

from Easyrex import Utils,Expression


# To create a regular expression for a date with Easyrex,
# we can use one of the following approaches:
if __name__=="__main__":
    # using the provided base regular expressions and the addition operator.
    #   the addition operator concatenates the expressions.
    date=Utils.digits+" "+Utils.word+" "+Utils.digits
    print(date)

    # we can do the same thing using custom expressions and even a mix of strings and expressions
    date=Expression(r"\d+")+r" \w+ "+Utils.digits
    print(date)
