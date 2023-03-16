import json
from typing import List


def key_list(src) -> List[str]:
    with open(src, "r") as file:
        db = json.load(file)
    if db is not None:
        return list(db.keys())
    return []
