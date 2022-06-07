from select import select
from typing_extensions import Self
from state import State
from typing import List

class Australia:
    def __init__(self) -> None:
        # initialize the continent as a graph
        self.aus = {}
    
    def addstate(self, parentState: State, neighbours: List):
        # add the the state list to the graph
        self.aus[parentState] = neighbours