import inspect
from typing import Dict, List, Union, Callable
from collections import deque, defaultdict
from pprint import pprint
from ._types import custom_type

def check_args(u_args:Dict, config_args:Dict):
    """Check if the user args exist in the defined args otherwise raise an Error.
        u_args: User args from the terminal
        config_args: Defined args
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
    structured_data = {}

    defaults = deque(function_spec.defaults)
    args = function_spec.args
    defaults.extendleft([None]*(len(args)-len(defaults)))

    for i in range(len(args)):
        structured_data[args[i]] = (custom_type(function_spec.annotations[args[i]]), defaults[i])
    
    return structured_data