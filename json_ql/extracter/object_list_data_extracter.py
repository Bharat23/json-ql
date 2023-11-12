from typing import Union, Dict, List
from .data_extracter import DataExtracter


class ObjectListDataExtracter(DataExtracter):
    def __init__(self):
        super().__init__()

    def extract(self, obj_list: List, key: str) -> Union[Dict, None]:
        try:
            dict_key, dict_value = key.split("=")
            dict_key = dict_key.strip()
            dict_value = dict_value.strip()
            for obj in obj_list:
                if dict_key in obj and obj[dict_key] == dict_value:
                    return obj
        except Exception:
            pass
        return None
