
class Int(int):
    """Int argument type class"""
    def __repr__(self) -> str:
        return f"[{int.__name__}]"

class Str(str):
    """Str argument type class"""
    def __repr__(self) -> str:
        return f"[{str.__name__}]"

class List(list):
    """List argument type class"""
    def __repr__(self) -> str:
        return f"[{list.__name__}]"

def custom_type(obj):
    """Assign one of the top types depending of obj type:
        int -> Int
        str -> Str
        list -> List
    """
    if issubclass(obj, int):
        return Int()
    elif issubclass(obj, str):
        return Str()
    elif issubclass(obj, list):
        return List()
    else:
        raise TypeError("Obj must be instance of one of these class: int | str | list")