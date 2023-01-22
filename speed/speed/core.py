import sys
from wind_parser import Parser
from .utils import *
from .utils.checkers import is_required

# Not yet finished
class Config(dict):
    def __init__(self):
        super().__init__()

    def add_subcommand(self, function, args:Dict) -> None:
        args_dict = {}
        
        for arg in args:
            a_type = args[arg].type
            if a_type.is_bool():
                args_dict[arg] = args[arg]
            
            elif a_type.is_str() or a_type.is_int():
                args_dict[arg] = args[arg]
            
            elif a_type.is_list():
                args_dict[arg] = args[arg]
        
        self[function] = args_dict


def list_subcommands(config):
    subcommands = {key.__name__:key for key in config.keys()}
    return subcommands

class Speed:
    def __init__(self, name="Speed"):
        self.name = name
        self.config = Config()
        self.uconfig = {} # Config after user input

    def subcommand(self):
        """Transform function into cli subcommand"""
        def wrapper(component:Callable):
            fargs : Dict  = struct_args(component)
            if mergeable(self.config, fargs):
                self.config.add_subcommand(component, fargs)
                
                self.parse_args()
                check_values(self.uconfig)
            
                return component
        return wrapper
    
    def argument(self):
        """Directly add argument to the main program by default without using subcommand.
        ex:
            python main.py --argument1
                or 
            python main.py --help
        The function name doesn't matter when using this decorator.
        """
        pass

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
                a_type = subcommand_args[arg].type
                if a_type.is_bool():
                    self.uconfig[arg] = Arg(a_type, bool(args.get(arg)))
                
                elif a_type.is_str():
                    self.uconfig[arg] = Arg(a_type, args[arg])
                
                elif a_type.is_int():
                    self.uconfig[arg] = Arg(a_type, int(args[arg]))
                
                elif a_type.is_list():
                    self.uconfig[arg] = Arg(a_type, args[arg])

    def action(self, func, args:Dict):
        pass

    def run(self):
        pass
    


