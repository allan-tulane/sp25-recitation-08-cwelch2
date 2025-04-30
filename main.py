import heapq
from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    # Priority queue holds: (total_weight, num_edges, current_node)
    heap = [(0, 0, source)]

    # Final result: node → (shortest_weight, fewest_edges)
    result = {}

    while heap:
        total_weight, num_edges, node = heapq.heappop(heap)

        if node in result:
            continue  # Already visited with the shortest path

        result[node] = (total_weight, num_edges)

        for neighbor, weight in graph.get(node, []):
            if neighbor not in result:
                heapq.heappush(heap, (total_weight + weight, num_edges + 1, neighbor))

    return result



    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parent = {}  # child → parent mapping
    visited = set([source])
    queue = deque([source])

    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    return parent

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    path = []
    current = destination

    while current in parents:
        parent = parents[current]
        path.append(parent)
        current = parent

    path.reverse()
    return ' -> '.join(path)


