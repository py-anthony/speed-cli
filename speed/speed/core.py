import sys
from wind_parser import Parser
from .utils import *
from .utils.checkers import is_required
from .utils.colors import *

class SubcommandsDict(dict):
    def __init__(self) -> None:
        super().__init__()

    def add_subcommand(self, function:Callable, args:Dict) -> None:
        self[function.__name__] = Subcommand(function, args)

class Speed:
    """
    Main class for the speed framework.

    Parameters
    ----------
    name : Optional[str]
        Name of the CLI instance application
    """
    def __init__(self, name="Speed"):
        self.name = name
        self.config = SubcommandsDict()
        self.uconfig = {} # Config after user input
        self.main_subcommand = None

    def main(self, debug=False):
        """
        Decorator for use the decorated function as default command.
        This function is an subcommand but it will be called if no subcommand is specified.
        """
        def wrapper(component:Callable):
            fargs : Dict  = struct_args(component)
            if mergeable(self.config, fargs):
                self.config.add_subcommand(component, fargs)
                self.main_subcommand = component.__name__

                if debug:
                    logging.debug(f"Main command created : {self.config[component.__name__]}")
                return component
        return wrapper

    def subcommand(self, debug=False):
        """
        Decorator for adding subcommand in config dictionary

        Parameters
        ----------
        debug: Optional[bool]
            Debug mode for displaying the subcommand default config.

        Returns
        -------
        Decorated function
        """
        def wrapper(component:Callable):
            fargs : Dict  = struct_args(component)
            if mergeable(self.config, fargs):
                self.config.add_subcommand(component, fargs)

                if debug:
                    logging.debug(f"Subcommand[{component.__name__}] created : {self.config[component.__name__]}")
            
                return component
        return wrapper
    

    def parse_args(self, args, subcommand:str):
        """
        Parse the arguments and add them to the config dictionary.

        Parameters
        ----------
        args : dict
            Arguments from the parser.
        subcommand : str
            Subcommand name from the parser.

        Returns
        -------
        Exception if the subcommand doesn't exist.

        """
        if subcommand in self.config.keys():
        
            subcommand_args = self.config[subcommand].args

            for arg in args:
                if arg not in subcommand_args.keys():
                    Error(f"Option '{arg}' unknown")
                    exit()
                arg_type = subcommand_args[arg].type
                arg_value = args[arg]

                if arg_type.is_bool():
                    self.config[subcommand].args[arg] = Arg(arg_type, bool(arg_value))
                elif arg_type.is_str():
                    self.config[subcommand].args[arg] = Arg(arg_type, arg_value)
                elif arg_type.is_int():
                    self.config[subcommand].args[arg] = Arg(arg_type, int(arg_value))
                elif arg_type.is_list():
                    self.config[subcommand].args[arg] = Arg(arg_type, arg_value)
        else:
            Error(f"Subcommand '{subcommand}' doesn't exist")
            exit()

    def execute(self, subcommand: Subcommand):
        """
        Execute the subcommand with the arguments after parsing user input.

        Parameters
        ----------
        subcommand : Subcommand
            Subcommand is a named tuple with the function and the argument.
        """
        args: Dict = subcommand.args 
        kwargs = {name:arg.value for name,arg in args.items()} # Get a dictionary of function keyword arguments after parsing user input

        subcommand.function(**kwargs) # Call the function with the keyword arguments


    def run(self):
        """
        Run the application.
        """
        parser = Parser(sys.argv)

        args = parser.args # Subcommands arguments from the parser
        try:
            subcommand = parser.subcommand # Subcommand name from the parser
            
        except AttributeError as attr:
            if self.main_subcommand is not None:
                subcommand = self.main_subcommand
            else:
                # Here, in the future, we will add the help command as default subcommand
                if args:
                    Error(f"Option '{list(args.keys())[0]}' unknown")
                    exit()
                else:
                    Error("No subcommand specified")
                    exit()
        
        self.parse_args(args, subcommand)
        check_required_arguments(self.config[subcommand].args)
        
        try:
            self.execute(self.config[subcommand])
        except KeyError as e:
            Error(f"Subcommand '{subcommand}' doesn't exist")
    
    def __repr__(self):
        """
        Return the name of the application and the subcommands list.
        """
        return f"[{self.name}] : < {' | '.join(self.config.keys())}>"
    