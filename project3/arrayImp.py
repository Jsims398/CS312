from math import inf

class ArrayImp:
    def __init__(self):
        self.distances: dict[int, float] = {}

    def start(self, graph:dict[int, dict[int, float]]):
        for node in graph:
            self.distances[node] = inf

    def pop_min(self) -> tuple[float,int]:
        min_node, min_distance = min(self.distances.items(), key=lambda item: item[1])
        del self.distances[min_node]
        return min_distance, min_node
    
    def update(self, new_distance: float, node: int):
        self.distances[node] = new_distance

    def push(self, new_distance: float, node: int):
        self.distances[node] = new_distance
