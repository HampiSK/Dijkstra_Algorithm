import pygame
import random

def display_text(message,x,y,size = 10,color = (0,0,0),message_font = None):
    font = pygame.font.Font(message_font,size)
    textSurface = font.render(message, True, color)
    TextRect = textSurface.get_rect()
    TextRect.center = ((x,y))
    win.blit(textSurface,TextRect)

    pygame.display.update()

def Djikstra(current_vertex,end_vertex,distances,nodes):
    # Setup
    path_list = []
    visited = []
    unvisited = {node: (None,None) for node in nodes}
    current_distance = 0

    pygame.draw.rect(win,(225, 225, 225),((150,40),(600, 50)))
    display_text('FINDING BEST PATH...',450,60,28,BLACK,'freesansbold.ttf')

    while True:
        ## For visualization
        for event in pygame.event.get():
        # Close game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        clock.tick(1)

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

            ## For visualization
            pygame.draw.circle(win, BLUE, vertices[end_vertex], size) 
            x,y = vertices[end_vertex]
            display_text(end_vertex,x,y,25,WHITE)

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

        ## For visualization
        pygame.draw.circle(win, BLUE, vertices[current_vertex], size)
        x,y = vertices[current_vertex]
        display_text(current_vertex,x,y,25,WHITE)

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

def intro():
    clock=pygame.time.Clock()

    counter = 0
    while True:       
        for event in pygame.event.get():
            # Close game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Close intro
            click = pygame.mouse.get_pressed()
            if event.type == pygame.KEYDOWN or click[0] == 1:
                return True           

        if counter == 0:
            win.fill((255, 255, 255))

            # Header
            pygame.draw.rect(win,(96,96,96),((149,39),(602, 52)))
            pygame.draw.rect(win,(160, 160, 160),((150,40),(600, 50)))
            display_text("Dijkstra's algorithm",450,67,30,BLACK,'freesansbold.ttf')

            # Body
            pygame.draw.rect(win,(96,96,96),((149,149),(602, 392)))
            pygame.draw.rect(win,(160, 160, 160),((150,150),(600, 320)))
            body1 = "Dijkstra's Shortest Path First algorithm, is an algorithm for"
            display_text(body1,450,200,20,BLACK,'freesansbold.ttf')
            body2 = " finding the shortest paths between nodes in a graph, which" 
            display_text(body2,450,230,20,BLACK,'freesansbold.ttf')
            body3 = "may represent, for example, road networks."
            display_text(body3,450,260,20,BLACK,'freesansbold.ttf')
            body4 = "It was conceived by computer scientist Edsger W. Dijkstra."
            display_text(body4,450,330,20,BLACK,'freesansbold.ttf')
            body5 ="The algorithm exists in many variants. Dijkstra's original    "
            display_text(body5,450,360,20,BLACK,'freesansbold.ttf')
            body6 = "algorithm found the shortest path between two given nodes,"
            display_text(body6,450,390,20,BLACK,'freesansbold.ttf')
            body7 = "producing a shortest-path tree."
            display_text(body7,450,420,20,BLACK,'freesansbold.ttf')

            # End
            display_text('Press any button to continue',450,505,19,WHITE,'freesansbold.ttf')

            counter = 1

        pygame.display.update()
        clock.tick(15)

###################################################################################################################

pygame.init()

### SETUP ###
# Window setup
win_name = "Dijkstra algorithm"
display_width = 900
display_height = 700
# Collors
WHITE = (255,255,255)
BLACK = (0,0,0)
PINK = (141,74,74)
DARKRED = (98,50,50)
SEAGREEN = (32,178,170)
BLUE = (51,153,255)

size = 20
thickness = 3
counter = 0
path = []
nodes = ('A','B','C','D','E','F','G','H','I','J','K','L')
find = False

# vertices
vertex_A = (150, 140)
vertex_B = (350, 140)
vertex_C = (550, 140)
vertex_D = (750, 140)
vertex_E = (150, 340)
vertex_F = (350, 340)
vertex_G = (550, 340)
vertex_H = (750, 340)
vertex_I = (150, 540)
vertex_J = (350, 540)
vertex_K = (550, 540)
vertex_L = (750, 540)

vertices = {
        'A': vertex_A,            
        'B': vertex_B,         
        'C': vertex_C,                
        'D': vertex_D,                                
        'E': vertex_E,                
        'F': vertex_F,
        'G': vertex_G,
        'H': vertex_H,                    
        'I': vertex_I,                                  
        'J': vertex_J,                
        'K': vertex_K,                  
        'L': vertex_L          
        }

# Window init
win = pygame.display.set_mode((display_width, display_height))
# Window bar init
pygame.display.set_caption(win_name)
icon = pygame.image.load('tab.png')
pygame.display.set_icon(icon)

clock=pygame.time.Clock()

# Introduction

pygame.mixer.music.load("The_Witcher_3_Wild_Hunt_OST_Silver_For_Monsters.mp3")
pygame.mixer.music.play(-1,80)

intro()

pygame.mixer.music.stop()

# MAIN LOOP
while True:
    for event in pygame.event.get():
        # Close game
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
                
    # mouse information
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if counter == 0:
        for event in pygame.event.get():
        # Close game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill((225, 225, 225))

        connections = {}

        # Draw lines

        # ROW 1:
        # A Vertex connections 
        pygame.draw.line(win, BLACK, vertex_A, vertex_B, thickness)
        pygame.draw.line(win, BLACK, vertex_A, vertex_E, thickness)

        # B Vertex connections
        pygame.draw.line(win, BLACK, vertex_B, vertex_A, thickness)
        pygame.draw.line(win, BLACK, vertex_B, vertex_C, thickness)
        pygame.draw.line(win, BLACK, vertex_B, vertex_F, thickness)

        # C Vertex connections
        pygame.draw.line(win, BLACK, vertex_C, vertex_B, thickness)
        pygame.draw.line(win, BLACK, vertex_C, vertex_D, thickness)
        pygame.draw.line(win, BLACK, vertex_C, vertex_G, thickness)
    
        # D Vertex connections 
        pygame.draw.line(win, BLACK, vertex_D, vertex_C, thickness)
        pygame.draw.line(win, BLACK, vertex_D, vertex_H, thickness)

        ## ROW 2:
        # E Vertex connections 
        pygame.draw.line(win, BLACK, vertex_E, vertex_F, thickness)

        # F Vertex connections
        pygame.draw.line(win, BLACK, vertex_F, vertex_G, thickness)

        # G Vertex connections
        pygame.draw.line(win, BLACK, vertex_G, vertex_H, thickness)

        ## ROW 3:
        # I Vertex connections
        pygame.draw.line(win, BLACK, vertex_I, vertex_E, thickness)
        pygame.draw.line(win, BLACK, vertex_I, vertex_J, thickness)

        # J Vertex connections
        pygame.draw.line(win, BLACK, vertex_J, vertex_F, thickness)
        pygame.draw.line(win, BLACK, vertex_J, vertex_I, thickness)
        pygame.draw.line(win, BLACK, vertex_J, vertex_K, thickness)

        # K Vertex connections
        pygame.draw.line(win, BLACK, vertex_K, vertex_G, thickness)
        pygame.draw.line(win, BLACK, vertex_K, vertex_J, thickness)
        pygame.draw.line(win, BLACK, vertex_K, vertex_L, thickness)
        
        # L Vertex connections 
        pygame.draw.line(win, BLACK, vertex_L, vertex_H, thickness)
        pygame.draw.line(win, BLACK, vertex_L, vertex_K, thickness)
 
        counter = 1

    if counter == 1:
        # Hide previous text
        pygame.draw.rect(win,(225, 225, 225),((150,40),(600, 50)))
        pygame.draw.rect(win,(225, 225, 225),((0,560),(900, 690)))

        # Draw rectangles with random number as well as update connections dictionary
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((125, 230),(20, 26)))
        ae = random.randint(1,9)
        connections.update({'ae':ae})
        display_text(str(ae),135,245,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((325, 230),(20, 26)))
        bf = random.randint(1,9)
        connections.update({'bf':bf})
        display_text(str(bf),335,245,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((525, 230),(20, 26)))
        cg = random.randint(1,9)
        connections.update({'cg':cg})
        display_text(str(cg),535,245,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((725, 230),(20, 26)))
        dh = random.randint(1,9)
        connections.update({'dh':dh})
        display_text(str(dh),735,245,25,WHITE)

        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((125, 430),(20, 26)))
        ei = random.randint(1,9)
        connections.update({'ei':ei})
        display_text(str(ei),135,445,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((325, 430),(20, 26)))
        jf = random.randint(1,9)
        connections.update({'jf':jf})
        display_text(str(jf),335,445,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((525, 430),(20, 26)))
        gk = random.randint(1,9)
        connections.update({'gk':gk})
        display_text(str(gk),535,445,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((725, 430),(20, 26)))
        hl = random.randint(1,9)
        connections.update({'hl':hl})
        display_text(str(hl),735,445,25,WHITE)

        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((240, 109),(20, 26)))
        ab = random.randint(1,9)
        connections.update({'ab':ab})
        display_text(str(ab),250,123,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((440, 109),(20, 26)))
        bc = random.randint(1,9)
        connections.update({'bc':bc})
        display_text(str(bc),450,123,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((640, 109),(20, 26)))
        cd = random.randint(1,9)
        connections.update({'cd':cd})
        display_text(str(cd),650,123,25,WHITE)

        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((240, 309),(20, 26)))
        ef = random.randint(1,9)
        connections.update({'ef':ef})
        display_text(str(ef),250,323,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((440, 309),(20, 26)))
        fg = random.randint(1,9)
        connections.update({'fg':fg})
        display_text(str(fg),450,323,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((640, 309),(20, 26)))
        gh = random.randint(1,9)
        connections.update({'gh':gh})
        display_text(str(gh),650,323,25,WHITE)

        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((240, 509),(20, 26)))
        ij = random.randint(1,9)
        connections.update({'ij':ij})
        display_text(str(ij),250,523,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((440, 509),(20, 26)))
        jk = random.randint(1,9)
        connections.update({'jk':jk})
        display_text(str(jk),450,523,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((640, 509),(20, 26)))
        kl = random.randint(1,9)
        connections.update({'kl':kl})
        display_text(str(kl),650,523,25,WHITE)

        distances = {
        'A': {'B': connections['ab'],'E': connections['ae']},                                         
        'B': {'A': connections['ab'],'C': connections['bc'],'F':connections['bf']},                      
        'C': {'B': connections['bc'],'D': connections['cd'],'G': connections['cg']},                     
        'D': {'C': connections['cd'],'H': connections['dh']},                                         
        'E': {'A': connections['ae'],'F': connections['ef'],'I': connections['ei']},                     
        'F': {'B': connections['bf'],'E': connections['ef'],'G': connections['fg'],'J': connections['jf']}, 
        'G': {'C': connections['cg'],'F': connections['fg'],'H': connections['gh'],'K': connections['gk']}, 
        'H': {'D': connections['dh'],'G': connections['gh'],'L': connections['hl']},                     
        'I': {'E': connections['ei'],'J': connections['ij']},                                         
        'J': {'F': connections['jf'],'I': connections['ij'],'K': connections['jk']},                     
        'K': {'G': connections['gk'],'J': connections['jk'],'L': connections['kl']},                     
        'L': {'H': connections['hl'],'K': connections['kl']}                                          
        }

        counter = 2

    # Draw nodes
    if counter == 2 or counter == 3:
        if 'A' in path:
            pygame.draw.circle(win, SEAGREEN, vertex_A, size)
        elif 168 > mouse[0] > 130 and 158 > mouse[1] > 120:
            pygame.draw.circle(win, PINK, vertex_A, size)
            if click[0] == 1:
                path.append('A')
        else:
            pygame.draw.circle(win, DARKRED, vertex_A, size)
        display_text('A',150,140,25,WHITE)
        if 'B' in path:
            pygame.draw.circle(win, SEAGREEN, vertex_B, size)
        elif 368 > mouse[0] > 330 and 158 > mouse[1] > 120:
            pygame.draw.circle(win, PINK, vertex_B, size)
            if click[0] == 1:
                path.append('B')
        else:
            pygame.draw.circle(win, DARKRED, vertex_B, size)
        display_text('B',350,140,25,WHITE)
        if 'C' in path:
            pygame.draw.circle(win, SEAGREEN, vertex_C, size)
        elif 568 > mouse[0] > 530 and 158 > mouse[1] > 120:
            pygame.draw.circle(win, PINK, vertex_C, size)
            if click[0] == 1:
                path.append('C')
        else:
            pygame.draw.circle(win, DARKRED, vertex_C, size)
        display_text('C',550,140,25,WHITE)
        if 'D' in path:
            pygame.draw.circle(win, SEAGREEN, vertex_D, size) 
        elif 768 > mouse[0] > 730 and 158 > mouse[1] > 120:
            pygame.draw.circle(win, PINK, vertex_D, size)
            if click[0] == 1:
                path.append('D')               
        else:
            pygame.draw.circle(win, DARKRED, vertex_D, size)
        display_text('D',750,140,25,WHITE)

        if 'E' in path:
            pygame.draw.circle(win, SEAGREEN, vertex_E, size)   
        elif 168 > mouse[0] > 130 and 358 > mouse[1] > 320:
            pygame.draw.circle(win, PINK, vertex_E, size)
            if click[0] == 1:
                path.append('E')         
        else:
            pygame.draw.circle(win, DARKRED, vertex_E, size)
        display_text('E',150,340,25,WHITE)
        if 'F' in path:
            pygame.draw.circle(win, SEAGREEN, vertex_F, size)
        elif 368 > mouse[0] > 330 and 358 > mouse[1] > 320:
            pygame.draw.circle(win, PINK, vertex_F, size)
            if click[0] == 1:
                path.append('F')
        else:
            pygame.draw.circle(win, DARKRED, vertex_F, size)
        display_text('F',350,340,25,WHITE)
        if 'G' in path:
            pygame.draw.circle(win, SEAGREEN, vertex_G, size) 
        elif 568 > mouse[0] > 530 and 358 > mouse[1] > 320:
            pygame.draw.circle(win, PINK, vertex_G, size)
            if click[0] == 1:
                path.append('G')       
        else:
            pygame.draw.circle(win, DARKRED, vertex_G, size)
        display_text('G',550,340,25,WHITE)
        if 'H' in path:
            pygame.draw.circle(win, SEAGREEN, vertex_H, size)    
        elif 768 > mouse[0] > 730 and 358 > mouse[1] > 320:
            pygame.draw.circle(win, PINK, vertex_H, size)
            if click[0] == 1:
                path.append('H')    
        else:
            pygame.draw.circle(win, DARKRED, vertex_H, size)
        display_text('H',750,340,25,WHITE)

        if 'I' in path:
            pygame.draw.circle(win, SEAGREEN, vertex_I, size)    
        elif 168 > mouse[0] > 130 and 558 > mouse[1] > 520:
            pygame.draw.circle(win, PINK, vertex_I, size)
            if click[0] == 1:
                path.append('I')            
        else:
            pygame.draw.circle(win, DARKRED, vertex_I, size)
        display_text('I',150,540,25,WHITE)
        if 'J' in path:
            pygame.draw.circle(win, SEAGREEN, vertex_J, size)
        elif 368 > mouse[0] > 330 and 558 > mouse[1] > 520:
            pygame.draw.circle(win, PINK, vertex_J, size)
            if click[0] == 1:
                path.append('J')
        else:
            pygame.draw.circle(win, DARKRED, vertex_J, size)
        display_text('J',350,540,25,WHITE)
        if 'K' in path:
            pygame.draw.circle(win, SEAGREEN, vertex_K, size)
        elif 568 > mouse[0] > 530 and 558 > mouse[1] > 520:
            pygame.draw.circle(win, PINK, vertex_K, size)
            if click[0] == 1:
                path.append('K')
        else:
            pygame.draw.circle(win, DARKRED, vertex_K, size)
        display_text('K',550,540,25,WHITE)
        if 'L' in path:
            pygame.draw.circle(win, SEAGREEN, vertex_L, size)
        elif 768 > mouse[0] > 730 and 558 > mouse[1] > 520:
            pygame.draw.circle(win, PINK, vertex_L, size)
            if click[0] == 1:
                path.append('L')
        else:
            pygame.draw.circle(win, DARKRED, vertex_L, size)
        display_text('L',750,540,25,WHITE)

    # nodes selection
    if len(path) <= 2:
        if len(path) == 1:
            pygame.draw.rect(win,(225, 225, 225),((150,40),(600, 50)))
            display_text('CHOOSE ENDING POSITION',450,60,28,BLACK,'freesansbold.ttf')
        elif len(path) == 2:
            counter += 1
            if counter >= 4:
                counter = 4
                find = True
        else:
            display_text('CHOOSE STARTING POSITION',450,60,28,BLACK,'freesansbold.ttf')

    # When two nodes were selected
    if find == True:
        start_vertex = path[0]
        end_vertex = path[1]

        path_list = Djikstra(start_vertex,end_vertex,distances,nodes)
        path_taken = shortest_path(reversed(path_list),end_vertex)

        pygame.draw.rect(win,(225, 225, 225),((150,40),(600, 50)))
        display_text('SHORTEST PATH',450,60,28,BLACK,'freesansbold.ttf')

        for node in nodes:
            if node in path_taken:
                continue
            else:
                pygame.draw.circle(win, DARKRED, vertices[node], size)
                x,y = vertices[node]
                display_text(node,x,y,25,WHITE)
        
        display_text(str(' > '.join(path_taken)),300,620,28,BLACK,'freesansbold.ttf')
        
        while counter != 5:
            for event in pygame.event.get():
                # Close game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()      

            # mouse information
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if 690 > mouse[0] > 610 and 660 > mouse[1] > 580:
                pygame.draw.circle(win, PINK, (650,620), 40)
                display_text('AGAIN',650,620,20,WHITE,'freesansbold.ttf')
                if click[0] == 1:
                    counter = 5
            else:
                pygame.draw.circle(win, DARKRED, (650,620), 40)
                display_text('AGAIN',650,620,20,WHITE,'freesansbold.ttf')

        # reset 
        counter = 1
        path.clear()
        find = False
    
    pygame.display.update()
    clock.tick(15)
