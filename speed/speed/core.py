import sys
from wind_parser import Parser
from .utils import *

# Not yet finished
class Config(dict):
    def __init__(self):
        super().__init__()

    def add_subcommand(self, function, args:Dict) -> None:
        args_dict = {}
        
        for arg in args:
            if hasattr(args[arg][0], "BOOL"):
                args_dict[arg] = args[arg]
            
            elif hasattr(args[arg][0], "STR") or hasattr(args[arg][0], "INT"):
                args_dict[arg] = args[arg]
            
            elif hasattr(args[arg][0], "LIST"):
                args_dict[arg] = args[arg]
        
        self[function] = args_dict


def is_required(arg:Tuple) -> bool:
    """Check if the argument is required or not"""
    return bool(arg.value)

def list_subcommands(config):
    subcommands = {key.__name__:key for key in config.keys()}
    return subcommands

class Speed:
    def __init__(self, name="Speed"):
        self.name = name
        self.config = Config()
        self.uconfig = {} # Config after user input

    def transform(self):
        """Transform function into cli subcommand"""
        def wrapper(component:Callable):
            fargs : Dict  = struct_args(component)
            if mergeable(self.config, fargs):
                self.config.add_subcommand(component, fargs)
                
                self.parse_args()
                check_values(self.uconfig)
            
                return component
        return wrapper

    def parse_args(self):
        parser = Parser(sys.argv) # Return a dict of all arguments
        subcommand = parser.subcommand
        args = parser.args

        _list_subcommands = list_subcommands(self.config)

        if subcommand in _list_subcommands.keys():
            c = self.config
            subcommand_args = c[_list_subcommands[subcommand]] # Get args for current subcommand
            print(subcommand_args)

            for arg in subcommand_args:
                if hasattr(subcommand_args[arg].type, "BOOL"):
                    self.uconfig[arg] = Arg(subcommand_args[arg].type, bool(args.get(arg)))
                
                elif hasattr(subcommand_args[arg].type, "STR"):
                    self.uconfig[arg] = Arg(subcommand_args[arg].type, args[arg])
                
                elif hasattr(subcommand_args[arg].type, "INT"):
                    self.uconfig[arg] = Arg(subcommand_args[arg].type, int(args[arg]))
                
                elif hasattr(subcommand_args[arg].type, "LIST"):
                    self.uconfig[arg] = Arg(subcommand_args[arg].type, args[arg])

    def action(self, func, args:Dict):
        pass

    def run(self):
        pass
    


