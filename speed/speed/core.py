import sys

from collections import deque
from wind_parser import Parser
from .utils import *

# Not yet finished
class Config:
    """Configuration for list of possible arguments"""
    def __init__(self, args:Dict):
        if not isinstance(args, Dict):
            raise TypeError("Config arguments must be dictionary")
        self.args = args
    
    def __repr__(self) -> str:
        return f"Config :\n {self.args}"


class Speed:
    def __init__(self, name="Speed"):
        self.name = name
        self.registry = {"kwargs": {},"flags": {},"lists": {}}

    # TODO: Add `required` and `short_name` functionalities
    def transform(self, required=False, short_name=False):
        """Transform function parameters into cli arguments"""
        def wrapper(component:Callable):
            fargs : Dict  = struct_args(component)
            if mergeable(self.registry, fargs):
                for arg in fargs:
                    if hasattr(fargs[arg][0], "BOOL"):
                        self.registry["flags"][arg] = fargs[arg]
                    
                    elif hasattr(fargs[arg][0], "STR") or hasattr(fargs[arg][0], "INT"):
                        self.registry["kwargs"][arg] = fargs[arg]
                    
                    elif hasattr(fargs[arg][0], "LIST"):
                        self.registry["lists"][arg] = fargs[arg]
            return component
        return wrapper

    def run(self):
        pass
    
    def __repr__(self):
        return f"<[ {self.name} ] : {' | '.join([i+': '+str(len(self.registry[i])) for i in self.registry.keys()])} >"

def main():
    app = Speed("App")

    @app.transform(required=True, short_name=True)
    def comp(cities:list = ["1","2","3"],name:str="Anthony", age:int=16):
        pass
    

    print(app.registry)
    print(app)

