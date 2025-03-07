from math import inf

class HeapImp:
    def __init__(self):
        self.distances: list[float] = []
        self.nodes: list[int] = []
        self.indexes: dict[int, int] = {}

    def start(self, graph: dict[int, dict[int, float]]):
        for node in graph:
            self.distances.append(inf)
            self.nodes.append(node)
            self.indexes[node] = len(self.nodes) - 1
        return
    
    def push(self, distance: float, node: int):
        self.distances.append(distance)
        self.nodes.append(node)
        self.indexes[node] = len(self.nodes) - 1
        self.up(len(self.nodes) - 1)
        return
    
    def update(self, new_distance: float, node: int):
        index = self.indexes.get(node)
        old_distance = self.distances[index]
        self.distances[index] = new_distance

        if (new_distance < old_distance):
            self.up(index)
        else:
            self.down(index)
        return
    
    def swap(self, index1: int, index2: int):
        self.distances[index1], self.distances[index2] = self.distances[index2], self.distances[index1]
        self.nodes[index1], self.nodes[index2] = self.nodes[index2], self.nodes[index1]
        self.indexes[self.nodes[index1]] = index1
        self.indexes[self.nodes[index2]] = index2
        return
    
    def parent(self, index: int) -> int:
        if (index == 0):
            return -1
        return (index - 1) // 2
    
    def children(self, index: int) -> tuple[int, int]:
        return (2 * index + 1, 2 * index + 2)

    def up(self, index: int):
        if (index == 0):
            return
        
        parent_index = self.parent(index)

        if self.distances[index] < self.distances[parent_index]:
            self.swap(index, parent_index)
            self.up(parent_index)

    def pop_min(self) -> tuple[float, int]:
        if len(self.distances) == 0:
            raise IndexError("Trying to pop from an empty queue")
        
        min_distance = self.distances[0]
        min_node = self.nodes[0]
        self.distances[0] = self.distances[-1]
        self.nodes[0] = self.nodes[-1]
        self.indexes[self.nodes[0]] = 0
        
        self.distances.pop()
        self.nodes.pop()
        self.indexes.pop(min_node)

        self.down(0)

        return (min_distance, min_node)
    
    def down(self, index: int):
        size = len(self.distances)
        while True:
            left, right = self.children(index)
            smallest = index

            if left < size and self.distances[left] < self.distances[smallest]:
                smallest = left
            
            if right < size and self.distances[right] < self.distances[smallest]:
                smallest = right

            if smallest == index:
                break
            
            self.swap(index, smallest)
            index = smallest

        return
