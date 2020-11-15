from typing import Dict

MyDict = Dict[str, int]


def func(d: MyDict):
    pass


func({'key': 10})
func({'key': 10.0})
func({'key': '10'})