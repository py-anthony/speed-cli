from .utils import *
from ._types import *
# Future implementation


class TypeChecker:
    """
    Class for checking that the config values are of the correct type.
    
    Parameters
    ----------
    args: tuple
        Named tuple with the argument type and the argument value
    """
    @staticmethod
    def check(arg_name, arg):
        if arg.type.is_bool():
            if not isinstance(arg.value, bool):
                raise Exception(f"Option '{arg_name}' it's not supposed to take any value")
        
        elif arg.type.is_int():
            try: 
                int(arg.value)
            except TypeError:
                print(arg.value)
            
        elif arg.type.is_str():
            if not isinstance(arg.value, str):
                raise Exception(f"Value of '{arg_name}' must be a valid string")
        
        elif arg.type.is_list():
            if not isinstance(arg.value, list):
                raise Exception(f"Value of '{arg_name}' must be a ',' separated list of values")