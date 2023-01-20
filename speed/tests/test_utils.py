import pytest
import inspect
from speed.utils import check_args, mergeable, check_annotations


def test_check_args():
    pass


class TestMergeableDicts:
    def test_true(self):
        dict1 = {"key1": None, "key2": None}
        dict2 = {"class": None, "nothing": None}
        assert mergeable(dict1, dict2)

    def test_key_error(self):
        dict1 = {"key1": None}
        dict2 = {"key1": None}
        with pytest.raises(KeyError):
            mergeable(dict1, dict2)


class TestStructArgs:
    pass


class TestCheckAnnotations:
    def test_valid(self):
        def function_with_annotation(a: int, b: str, c: list, d: bool):
            pass

        assert check_annotations(
            inspect.getfullargspec(function_with_annotation)) is None
    
    def test_no_annotation(self):
        def function_without_annotation(a, b, c, d):
            pass

        with pytest.raises(TypeError):
            check_annotations(inspect.getfullargspec(function_without_annotation))
