from tracemalloc import start
from state import State
from australia import Australia

domain = {
    0: "red",
    1: "green",
    2: "blue"
}

class Constraint:
    def __init__(self) -> None:
        self.frontier = []
        self.explored = []
    
    def checkConstraint(self, graph: Australia, node: State) -> bool:
        n_list = []
        for n in graph[node]:
            # check the colors of the neighbours
            if n.color == "":
                continue
            elif n.color == node.color:
                n_list.append[False]
            elif n.color != node.color:
                n_list.append(True)
        
        if False in n_list:
            return False
        
        else:
            return True

    
    def colorGraph(self, graph: Australia, startNode: State):
        # assume nothing is colored at the mooment
        self.frontier.append(startNode)
        
        # color the first node
        startNode.color = domain[0]

        while(len(self.frontier) != 0):
            for neighbours in graph[startNode]:
                # something
                pass 