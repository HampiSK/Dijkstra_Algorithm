# Add comments you idiot!

# Tuple version

nodes = ('A', 'B', 'C', 'D') # vertices
visited = []
unvisited = {node: (None,None) for node in nodes}
#unvisited = {node: None for node in nodes}
current_distance = 0
distances = {
    'A': {'B': 3, 'D': 15},
    'B': {'A': 3, 'D': 10, 'C': 2},   
    'C': {'B': 2, 'D': 20},
    'D': {'A': 15, 'B': 10, 'C': 20}}
current_vertex = 'D'
table = []
while True:
    print(current_vertex)
    for neighbour, distance in distances[current_vertex].items():
        if neighbour in visited: 
            continue
        
        # unpack tuple
        unvisited_distance,unvisited_vertex = unvisited[neighbour]
 
        new_distance = current_distance + distance
    
        if unvisited_distance is None or unvisited_distance > new_distance:
            unvisited[neighbour] = (new_distance,current_vertex)

    visited.append(current_vertex)
    unvisited.pop(current_vertex)
    if len(unvisited) < 1:
        break
    
    current_connections = {}
    for k, v in unvisited.items():
        distance,vertex = v       
        if distance != None:        
            current_connections.update({k:distance})
    
    sv_unvisited = min(current_connections.keys(), key=(lambda k: current_connections[k]))
    current_distance = current_connections[sv_unvisited]

    
    current_vertex = sv_unvisited

# Without Tuple


# while True:


#     for neighbour, distance in distances[current_vertex].items():
#         if neighbour in visited: 
#             continue
  
#         new_distance = current_distance + distance

#         if unvisited[neighbour] is None or unvisited[neighbour] > new_distance:
#             unvisited[neighbour] = new_distance
        
    
#     visited.append(current_vertex)
#     unvisited.pop(current_vertex)
#     if len(unvisited) < 1:
#         break
    
#     current_connections = {}
#     for k, v in unvisited.items():
#         if v != None:          
#             current_connections.update({k:v})
    

#     sv_unvisited = min(current_connections.keys(), key=(lambda k: current_connections[k]))
#     current_distance = current_connections[sv_unvisited]

    
#     current_vertex = sv_unvisited
