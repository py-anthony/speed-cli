
class Bool:
    BOOL = 1 
    """Bool argument type class"""
    def __repr__(self) -> str:
        return f"[{bool.__name__}]"

class Int(int):
    INT = 1
    """Int argument type class"""
    def __repr__(self) -> str:
        return f"[{int.__name__}]"

class Str(str):
    STR = 1
    """Str argument type class"""
    def __repr__(self) -> str:
        return f"[{str.__name__}]"

class List(list):
    LIST = 1
    """List argument type class"""
    def __repr__(self) -> str:
        return f"[{list.__name__}]"


def custom_type(obj):
    """Assign one of the top types depending of obj type:
        int -> Int
        str -> Str
        list -> List
    """
    if issubclass(obj, bool): # Must be the first because bool is a subclass of int
        return Bool()
    elif issubclass(obj, int):
        return Int()
    elif issubclass(obj, str):
        return Str()
    elif issubclass(obj, list):
        return List()

    else:
        raise TypeError("Argument must be a subclass of one of these class: int | str | list | bool")