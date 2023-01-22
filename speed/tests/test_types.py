import pytest
from speed.utils._types import Int, Bool, Str, List, custom_type

class TestCustomType:
    def test_int(self):
        assert isinstance(custom_type(int), Int)

    def test_str(self):
        assert isinstance(custom_type(str), Str)

    def test_list(self):
        assert isinstance(custom_type(list), List)

    def test_bool(self):
        assert isinstance(custom_type(bool), Bool)

    def test_invalid(self):
        with pytest.raises(TypeError):
            custom_type(float)

class TestMyType:
    def test_is_bool(self):
        assert Bool().is_bool()
    
    def test_is_int(self):
        assert Int().is_int()

    def test_is_str(self):
        assert Str().is_str()
    
    def test_is_list(self):
        assert List().is_list()

    def test_bool_is_not_int(self):
        assert not Bool().is_int()