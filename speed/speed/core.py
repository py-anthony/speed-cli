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

    def subcommand(self, debug=False):
        """Transform function into CLI subcommand"""
        def wrapper(component:Callable):
            fargs : Dict  = struct_args(component)
            if mergeable(self.config, fargs):
                custom_function = CustomFunction(component) # Change __repr__ of the function
                self.config.add_subcommand(custom_function, fargs)
                
                if debug:
                    logging.debug(f"Subcommand[{component.__name__}] args : {self.config[custom_function]}")
            
                self.parse_args()
                
                if debug:
                    logging.debug(f"Subcommand[{component.__name__}] args after parsing : {self.uconfig}\n")
                
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

    def debug(self):
        logging.debug(f"Subcommands list : {list_subcommands(self.config)}")

    def run(self):
        pass
    
    def __repr__(self):
        return f"[{self.name}] : Subcommands : {' | '.join(list(map(lambda f:f.__name__,self.config.keys())))}"
    


