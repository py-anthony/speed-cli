from colorama import Fore, Style

COLORS = {
    "red": Fore.RED,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "blue": Fore.BLUE,
    "magenta": Fore.MAGENTA,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE,
    "lightblue": Fore.LIGHTBLUE_EX,
    "reset": Fore.RESET,
}

STYLE = {
    "bold": Style.BRIGHT,
    "reset": Style.RESET_ALL,
}

def check_color(color):
    if color not in COLORS:
        raise ValueError(f"Color: '{color}' doesn't exist or not supported.")

class Output:
    """
    Class to handle output color to the terminal.
    """
    def __init__(self, msg, color="reset"):
        self.color = color
        self.msg = msg

class Warning:
    """
    Class to handle warning color to the terminal.
    """
    def __init__(self, msg, color="yellow"):
        self.msg = COLORS[color]\
            +STYLE["bold"]+"WARNING : "\
            +STYLE["reset"]\
            +COLORS[color]+msg\
            +COLORS["reset"]
        
        print(self.msg)

class Error:
    """
    Class to handle error color to the terminal.
    """
    def __init__(self, msg, color="red"):
        self.msg = COLORS[color]\
            +STYLE["bold"]+"ERROR : "\
            +STYLE["reset"]\
            +COLORS[color]+msg\
            +COLORS["reset"]
        
        print(self.msg+"\n")

if __name__ == '__main__':
    Output("This is an output message.")
    Warning("This is a warning message.")
    Error("This is an error message.")

