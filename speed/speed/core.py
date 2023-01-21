from wind_parser import Parser
from .utils import *

# Not yet finished
class Config(dict):
    def __init__(self):
        super().__init__()

    def add_subcommand(self, function, args:Dict) -> None:
        args_dict = defaultdict(dict)
        
        for arg in args:
            if hasattr(args[arg][0], "BOOL"):
                args_dict["flags"][arg] = args[arg]
            
            elif hasattr(args[arg][0], "STR") or hasattr(args[arg][0], "INT"):
                args_dict["kwargs"][arg] = args[arg]
            
            elif hasattr(args[arg][0], "LIST"):
                args_dict["lists"][arg] = args[arg]
        
        self[function] = dict(args_dict)
                
class Speed:
    def __init__(self, config, name="Speed"):
        self.name = name
        self.config = config

    def transform(self):
        """Transform function into cli subcommand"""
        def wrapper(component:Callable):
            fargs : Dict  = struct_args(component)
            if mergeable(self.config, fargs):
                self.config.add_subcommand(component, fargs)
            
            return component
        return wrapper


    def run(self):
        pass
    


