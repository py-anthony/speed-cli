import inspect
from typing import Dict, List, Union, Callable, Tuple
from collections import deque, defaultdict, namedtuple
from pprint import pprint
from ._types import custom_type
from .logging_config import *



Arg = namedtuple("Arg", ["type", "value"]) # For storing the argument type and value


def check_args(u_args:Dict, config_args:Dict):
    """Check if the user args exist in the defined args otherwise raise an Error.
        u_args: User args from the terminal
        config_args: Defined args
    NOTE: This is for the future, not yet implemented
    """

    for key in u_args.key():
        if key not in config_args:
            raise KeyError(key)

def mergeable(dict1, dict2) -> bool:
    """Check if two dictionaries don't have one or many same key """
    doubles = []
    for key in dict1:
        if key in dict2:
            doubles.append(key)
    if doubles:
        raise KeyError(f"The arguments name: {','.join(doubles)} are defined two times, use another name")
 
    return True

def check_annotations(function_spec) -> None:
    """Check if the function has annotations, if not raise an TypeError
            function_spec: function specification obtained from inspect.getfullargspec
    """
    for arg in function_spec.args:
        if arg not in function_spec.annotations:
            raise TypeError(f"Argument '{arg}' doesn't have type annotation among : int | list | str | bool")

# TODO: Add test for this function
def struct_args(function:Callable):
    """Structure a function arguments like:
    { 
        arg1 : (default_value, annotation), 
        arg2 : (default_value, annotation)
        ...  : ...
    }
    If default value doesn't exist, then use None instead, if annotation doesn't exist, raise an TypeError.
    """
    function_spec = inspect.getfullargspec(function)
    check_annotations(function_spec)  # Check if all function parameters has type annotation
    structured_data = {}
    args = function_spec.args


    if function_spec.defaults:
        defaults = deque(function_spec.defaults)
        defaults.extendleft([None]*(len(args)-len(defaults)))
    else:
        defaults = [None]*len(args)

    for i in range(len(args)):
        structured_data[args[i]] = Arg(custom_type(function_spec.annotations[args[i]]), defaults[i])
    
    return structured_data

def check_values(uconfig:dict):
    """Check if there are no required argument that are not have value in the config after parsing the arguments"""
    for key in uconfig:
        if uconfig[key].value is None:
            raise ValueError(f"Argument '{key}' is required")
    
    return True

class CustomFunction:
    """Custom function class to overwrite a function __repr__ and __str__
    NOTE: This is only for debugging purpose
    """
    def __init__(self, function):
        self.function = function
        self.__name__ = function.__name__
    
    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)
    
    def __repr__(self):
        return f"<function : '{self.function.__name__}'>"


