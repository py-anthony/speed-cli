from speed.utils import check_args, mergeable

import pytest

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