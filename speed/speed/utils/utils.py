from typing import Dict, List, Union
from collections import deque
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



