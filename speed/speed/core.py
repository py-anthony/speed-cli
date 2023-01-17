import sys
import inspect
from collections import deque
from wind_parser import Parser
from utils.utils import *

# Not yet finished
class Config:
    """Configuration for list of possible arguments"""
    def __init__(self, args:Dict):
        if not isinstance(args, Dict):
            raise TypeError("Config arguments must be dictionary")
        self.args = args
    
    def __repr__(self) -> str:
        return f"Config :\n {self.args}"


def struct_args(function):
    """Structure a function's arguments like:
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


class Speed:
    def __init__(self, name=__name__):
        self.name = name
        self.registry = {}

    def kwarg(self, required=False, short_name=False):
        """Transform function parameters into cli flag"""
        pass
            

    def flag(self, required=False, short_name=False):
        """Transform function parameters into cli argument"""
        pass

    def list(self):
        """Transform function parameters into cli list argument"""
        pass

    def run(self):
        pass


if __name__ == '__main__':
    def test(anthony:list, nom:str="Anthony", age:int=16):
        pass
    print(struct_args(test))

