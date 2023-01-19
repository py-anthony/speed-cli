import sys

from wind_parser import Parser
from .utils import *

# Not yet finished
class Config(dict):
    def __init__(self):
        super().__init__()

    def add_arguments(self, function, args:Dict) -> None:
        template = defaultdict(dict)
        
        for arg in args:
            if hasattr(args[arg][0], "BOOL"):
                template["flags"][arg] = args[arg]
            
            elif hasattr(args[arg][0], "STR") or hasattr(args[arg][0], "INT"):
                template["kwargs"][arg] = args[arg]
            
            elif hasattr(args[arg][0], "LIST"):
                template["lists"][arg] = args[arg]
        
        self[function] = template

class Speed:
    # TODO: Add support for toml or json configuration support (not urgent)
    def __init__(self, config, name="Speed", file=None):
        self.name = name
        self.config = config

    # TODO: Add `required` and `short_name` functionalities
    def transform(self, required=False, short_name=False):
        """Transform function parameters into cli arguments"""
        def wrapper(component:Callable):
            fargs : Dict  = struct_args(component)
            if mergeable(self.config, fargs):
                self.config.add_arguments(component, fargs)

            return component
        return wrapper

    def run(self):
        pass
    
    def __repr__(self):
        #return f"<[ {self.name} ] : {' | '.join([i+': '+str(len(self.config[i])) for i in self.config.keys()])} >"
        return str(self.config)

def main():
    config = Config()
    app = Speed(name="App", config=config)

    @app.transform(required=True, short_name=True)
    def comp(cities:list = ["1","2","3"],name:str="Anthony", age:int=16):
        pass

    print(app)


