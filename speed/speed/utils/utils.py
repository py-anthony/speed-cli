import inspect
from typing import Dict, List, Union, Callable, Tuple
from collections import deque, defaultdict, namedtuple
from pprint import pprint
from .types import custom_type
from .logging_config import *
from .colors import *


Subcommand = namedtuple("Subcommand", ["function", "args"])
Arg = namedtuple("Arg", ["type", "value"]) # For storing the argument type and value


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
        if arg!="self" and arg not in function_spec.annotations:
            raise TypeError(f"Argument '{arg}' doesn't have type annotation among : int | list | str | bool")

# TODO: Add tests for this function
def struct_args(function:Callable):
    """Structure a function arguments like:
    { 
        arg1 : Arg(type, value), 
        arg2 : Arg(type, value)
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

# TODO: Add tests for this function
def check_required_arguments(uconfig:dict):
    """Check if there are no required argument that are not have value in the config after parsing the arguments"""
    for key in uconfig:
        if uconfig[key].value is None:
            Error(f"Argument '{key}' is required")
            exit()

