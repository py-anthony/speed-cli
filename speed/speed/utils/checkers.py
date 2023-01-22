from .utils import *
# Future implementation

def is_required(arg:Tuple) -> bool:
    """Check if the argument is required or not"""
    return bool(arg.value)

class TypeChecker:
    """Class for checking that the value match with the argument type after creating the argument and after parsing the arguments"""
    def __init__(self):
        pass

    def check(self, arg:Tuple):
        pass