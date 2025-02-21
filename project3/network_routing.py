from arrayImp import ArrayImp
from heap import HeapImp
from math import inf

def find_shortest_path_with_heap(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the heap-based algorithm.

    Args:
        graph: Dictionary of dictionaries representing weighted graph
        source: Starting node
        target: Destination node

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """   
    
    queue = HeapImp()
    queue.start(graph)
    queue.update(0, source)
    dist: dict[int, float] = {node:inf for node in graph}
    dist[source] = 0
    prev: dict[int, int] = {node:None for node in graph}

    while (queue):
        distance, node = queue.pop_min()
        
        if (node == target):
            break
        if (distance > dist[node]):
            continue

        for next,weight in graph[node].items():
            new_dist = dist[node] + weight
            if new_dist < dist[next]:
                dist[next] = new_dist
                prev[next] = node
                queue.update(new_dist, next)

    if (dist[target] == inf):
        return [], inf

    path: list[int] = []
    next: int = target
    while next is not None:
        path.append(next)
        next = prev[next]

    return path[::-1], dist[target]

def find_shortest_path_with_array(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the array-based (linear lookup) algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """
    queue = ArrayImp()
    queue.start(graph)
    queue.update(0, source)
    dist = {node:inf for node in graph}
    dist[source] = 0
    prev: dict[int, int] = {node:None for node in graph}
    
    while(queue):
        distance, node = queue.pop_min()
        
        if (node == target):
            break
        if (distance > dist[node]):
            continue

        for next,weight in graph[node].items():
            new_dist = dist[node] + weight
            if new_dist < dist[next]:
                dist[next] = new_dist
                prev[next] = node
                queue.update(new_dist, next)

    if (dist[target] == inf):
        return [], inf
    
    path: list[int] = []
    next: int = target
    while next is not None:
        path.append(next)
        next = prev[next]

    return path[::-1], dist[target]

# graph = {
#     0: {1: 2, 2: 4},
#     1: {2: 1, 3: 7},
#     2: {3: 3},
#     3: {}
# }
# source = 0
# target = 3

# print(find_shortest_path_with_array(graph, source, target))