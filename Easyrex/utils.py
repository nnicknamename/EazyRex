"""The utils module: implements usual Expressions and regular operations relating to EasyRex.
"""


from Easyrex.expression import Expression

class Utils:
    """implements usual Expressions and regular operations relating to EasyRex.
    """

    word=Expression(r"\w+")
    digits=Expression(r"\d+")
