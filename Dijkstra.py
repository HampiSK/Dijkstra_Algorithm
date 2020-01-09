distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},    
    'F': {'A': 5, 'E': 2, 'C': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2}
}

nodes = ('A', 'B', 'C', 'D','F','G','E') # vertices
start_vertex = 'B'
end_vertex = 'F'

def Dijkstra(current_vertex,end_vertex,distances,nodes):
    # Setup
    path_list = []
    visited = []
    unvisited = {node: (None,None) for node in nodes}
    current_distance = 0

    while True:
        # looping trought current vertex connections
        for neighbour, distance in distances[current_vertex].items():
            if neighbour in visited: 
                continue
            
            # unpack tuple
            unvisited_distance,unused_vertex = unvisited[neighbour]
    
            new_distance = current_distance + distance

            # updating unvisited dictionary with new values
            if unvisited_distance is None or unvisited_distance > new_distance:
                unvisited[neighbour] = (new_distance,current_vertex)

        if current_vertex == end_vertex:
            return path_list 
            
        # appending and deleting
        path_list.append(unvisited.copy())
        visited.append(current_vertex)
        unvisited.pop(current_vertex)

        current_connections = {}

        # new dictionary without None values and tuples based on unvisited dictionary
        for k, v in unvisited.items():
            distance,unused_vertex = v       
            if distance != None:        
                current_connections.update({k:distance})

        # finding smallest distance in unvisited dictionary
        sv_unvisited = min(current_connections.keys(), key=(lambda k: current_connections[k]))

        # updating current distance
        current_distance = current_connections[sv_unvisited]

        # next smallest vertex
        current_vertex = sv_unvisited
    

def shortest_path(reversed_path_list,last_vertex):
    # This function returns taken path

    taken_path = [last_vertex]
    for row in reversed_path_list:
        for k,tple in row.items():
            unused_distance,vertex = tple
            if k == last_vertex and vertex != None:
                taken_path.append(vertex)                
                last_vertex = vertex
    return taken_path[::-1] # reverse list

path_list = Dijkstra(start_vertex,end_vertex,distances,nodes)

print()
print('Start: ' + start_vertex)
print('End: ' + end_vertex)

print('Path:',shortest_path(reversed(path_list),end_vertex))
print()
