from typing import Any, List

import pytest

from json_ql.extracter.object_list_data_extracter import ObjectListDataExtracter


class TestObjectListDataExtracter:

    @pytest.mark.parametrize('lst,key,output', [
        # invalid key
        ([{}], "hello", None),
        # value doesn't exist
        ([{"b": "c"}], "b=a", None),
        # happy path
        ([{"b": "a"}], "b=a", {"b": "a"}),
        # happy path multiple match only one returns
        ([{"b": "a"}, {"b": "a"}], "b=a", {"b": "a"}),
    ])
    def test_extract(self, lst: List, key: str, output: Any):
        assert ObjectListDataExtracter().extract(lst, key) == output
