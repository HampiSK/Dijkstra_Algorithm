import pygame
import random
#import sys

    #print(pygame.font.get_fonts())
def display_text(message,x,y,size = 10,color = (0,0,0),message_font = None):
    font = pygame.font.Font(message_font,size)
    textSurface = font.render(message, True, color)
    TextRect = textSurface.get_rect()
    TextRect.center = ((x,y))
    win.blit(textSurface,TextRect)

    pygame.display.update()

pygame.init()

# Setup
win_name = 'Shortest Distance'
display_width = 900
display_height = 700
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (  98,   50, 50)
PINK = (  141, 74,   74)
DARKRED = (98,   50,   50)

vertex1_1 = (150, 140)
vertex1_2 = (350, 140)
vertex1_3 = (550, 140)
vertex1_4 = (750, 140)
vertex2_1 = (150, 340)
vertex2_2 = (350, 340)
vertex2_3 = (550, 340)
vertex2_4 = (750, 340)
vertex3_1 = (150, 540)
vertex3_2 = (350, 540)
vertex3_3 = (550, 540)
vertex3_4 = (750, 540)

win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(win_name)
icon = pygame.image.load('gameicon.png')
pygame.display.set_icon(icon)

clock=pygame.time.Clock()
counter = 0
path = []
# def drawCircle():
#     pygame.draw.circle(screen, BLUE, pos, 20)
#random.randint
while True:
    for event in pygame.event.get():
        # Close game
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
                
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(mouse)
    size = 20
    thickness = 3
    if counter == 1:
        if 168 > mouse[0] > 130 and 158 > mouse[1] > 120:
            pygame.draw.circle(win, PINK, vertex1_1, size)
            if click[0] == 1:
                path.append('A')
        else:
            pygame.draw.circle(win, DARKRED, vertex1_1, size)
        display_text('A',150,140,25,WHITE)
        if 368 > mouse[0] > 330 and 158 > mouse[1] > 120:
            pygame.draw.circle(win, PINK, vertex1_2, size)
            if click[0] == 1:
                path.append('B')
        else:
            pygame.draw.circle(win, DARKRED, vertex1_2, size)
        display_text('B',350,140,25,WHITE)
        if 568 > mouse[0] > 530 and 158 > mouse[1] > 120:
            pygame.draw.circle(win, PINK, vertex1_3, size)
            if click[0] == 1:
                path.append('C')
        else:
            pygame.draw.circle(win, DARKRED, vertex1_3, size)
        display_text('C',550,140,25,WHITE)
        if 768 > mouse[0] > 730 and 158 > mouse[1] > 120:
            pygame.draw.circle(win, PINK, vertex1_4, size)
            if click[0] == 1:
                path.append('D')
        else:
            pygame.draw.circle(win, DARKRED, vertex1_4, size)
        display_text('D',750,140,25,WHITE)

        if 168 > mouse[0] > 130 and 358 > mouse[1] > 320:
            pygame.draw.circle(win, PINK, vertex2_1, size)
            if click[0] == 1:
                path.append('E')            
        else:
            pygame.draw.circle(win, DARKRED, vertex2_1, size)
        display_text('E',150,340,25,WHITE)
        if 368 > mouse[0] > 330 and 358 > mouse[1] > 320:
            pygame.draw.circle(win, PINK, vertex2_2, size)
            if click[0] == 1:
                path.append('F')
        else:
            pygame.draw.circle(win, DARKRED, vertex2_2, size)
        display_text('F',350,340,25,WHITE)
        if 568 > mouse[0] > 530 and 358 > mouse[1] > 320:
            pygame.draw.circle(win, PINK, vertex2_3, size)
            if click[0] == 1:
                path.append('G')
        else:
            pygame.draw.circle(win, DARKRED, vertex2_3, size)
        display_text('G',550,340,25,WHITE)
        if 768 > mouse[0] > 730 and 358 > mouse[1] > 320:
            pygame.draw.circle(win, PINK, vertex2_4, size)
            if click[0] == 1:
                path.append('H')
        else:
            pygame.draw.circle(win, DARKRED, vertex2_4, size)
        display_text('H',750,340,25,WHITE)

        if 168 > mouse[0] > 130 and 558 > mouse[1] > 520:
            pygame.draw.circle(win, PINK, vertex3_1, size)
            if click[0] == 1:
                path.append('I')
        else:
            pygame.draw.circle(win, DARKRED, vertex3_1, size)
        display_text('I',150,540,25,WHITE)
        if 368 > mouse[0] > 330 and 558 > mouse[1] > 520:
            pygame.draw.circle(win, PINK, vertex3_2, size)
            if click[0] == 1:
                path.append('J')
        else:
            pygame.draw.circle(win, DARKRED, vertex3_2, size)
        display_text('J',350,540,25,WHITE)
        if 568 > mouse[0] > 530 and 558 > mouse[1] > 520:
            pygame.draw.circle(win, PINK, vertex3_3, size)
            if click[0] == 1:
                path.append('K')
        else:
            pygame.draw.circle(win, DARKRED, vertex3_3, size)
        display_text('K',550,540,25,WHITE)
        if 768 > mouse[0] > 730 and 558 > mouse[1] > 520:
            pygame.draw.circle(win, PINK, vertex3_4, size)
            if click[0] == 1:
                path.append('L')
        else:
            pygame.draw.circle(win, DARKRED, vertex3_4, size)
        display_text('L',750,540,25,WHITE)

        counter += 1


    if counter == 0:
        win.fill((225, 225, 225))

        vertices = {}

        # ROW 1:
        #1 Vertex connections 
        pygame.draw.line(win, BLACK, vertex1_1, vertex1_2, thickness)
        pygame.draw.line(win, BLACK, vertex1_1, vertex2_1, thickness)

        # 2 Vertex connections
        pygame.draw.line(win, BLACK, vertex1_2, vertex1_1, thickness)
        pygame.draw.line(win, BLACK, vertex1_2, vertex1_3, thickness)
        pygame.draw.line(win, BLACK, vertex1_2, vertex2_2, thickness)

        # 3 Vertex connections
        pygame.draw.line(win, BLACK, vertex1_3, vertex1_2, thickness)
        pygame.draw.line(win, BLACK, vertex1_3, vertex1_4, thickness)
        pygame.draw.line(win, BLACK, vertex1_3, vertex2_3, thickness)
    
        # 4 Vertex connections 
        pygame.draw.line(win, BLACK, vertex1_4, vertex1_3, thickness)
        pygame.draw.line(win, BLACK, vertex1_4, vertex2_4, thickness)

        ## ROW 2:
        # 1 Vertex connections 
        pygame.draw.line(win, BLACK, vertex2_1, vertex1_1, thickness)
        pygame.draw.line(win, BLACK, vertex2_1, vertex2_2, thickness)
        pygame.draw.line(win, BLACK, vertex2_1, vertex3_1, thickness)

        # 2 Vertex connections
        pygame.draw.line(win, BLACK, vertex2_2, vertex1_2, thickness)
        pygame.draw.line(win, BLACK, vertex2_2, vertex2_1, thickness)
        pygame.draw.line(win, BLACK, vertex2_2, vertex2_3, thickness)
        pygame.draw.line(win, BLACK, vertex2_2, vertex3_2, thickness)

        # 3 Vertex connections
        pygame.draw.line(win, BLACK, vertex2_3, vertex1_3, thickness)
        pygame.draw.line(win, BLACK, vertex2_3, vertex2_2, thickness)
        pygame.draw.line(win, BLACK, vertex2_3, vertex2_4, thickness)
        pygame.draw.line(win, BLACK, vertex2_3, vertex3_3, thickness)
        
        # 4 Vertex connections 
        pygame.draw.line(win, BLACK, vertex2_4, vertex1_4, thickness)
        pygame.draw.line(win, BLACK, vertex2_4, vertex2_3, thickness)
        pygame.draw.line(win, BLACK, vertex2_4, vertex3_4, thickness)

        ## ROW 3:
        # 1 Vertex connections
        pygame.draw.line(win, BLACK, vertex3_1, vertex2_1, thickness)
        pygame.draw.line(win, BLACK, vertex3_1, vertex3_2, thickness)

        # 2 Vertex connections
        pygame.draw.line(win, BLACK, vertex3_2, vertex2_2, thickness)
        pygame.draw.line(win, BLACK, vertex3_2, vertex3_1, thickness)
        pygame.draw.line(win, BLACK, vertex3_2, vertex3_3, thickness)

        # 3 Vertex connections
        pygame.draw.line(win, BLACK, vertex3_3, vertex2_3, thickness)
        pygame.draw.line(win, BLACK, vertex3_3, vertex3_2, thickness)
        pygame.draw.line(win, BLACK, vertex3_3, vertex3_4, thickness)
        
        # 4 Vertex connections 
        pygame.draw.line(win, BLACK, vertex3_4, vertex2_4, thickness)
        pygame.draw.line(win, BLACK, vertex3_4, vertex3_3, thickness)

        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((125, 230),(20, 26)))
        ae = random.randint(1,9)
        vertices.update({'ae':ae})
        display_text(str(ae),135,245,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((325, 230),(20, 26)))
        bf = random.randint(1,9)
        vertices.update({'bf':bf})
        display_text(str(bf),335,245,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((525, 230),(20, 26)))
        cg = random.randint(1,9)
        vertices.update({'cg':cg})
        display_text(str(cg),535,245,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((725, 230),(20, 26)))
        dh = random.randint(1,9)
        vertices.update({'dh':dh})
        display_text(str(dh),735,245,25,WHITE)

        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((125, 430),(20, 26)))
        ei = random.randint(1,9)
        vertices.update({'ei':ei})
        display_text(str(ei),135,445,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((325, 430),(20, 26)))
        jf = random.randint(1,9)
        vertices.update({'jf':jf})
        display_text(str(jf),335,445,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((525, 430),(20, 26)))
        gk = random.randint(1,9)
        vertices.update({'gk':gk})
        display_text(str(gk),535,445,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((725, 430),(20, 26)))
        hl = random.randint(1,9)
        vertices.update({'hl':hl})
        display_text(str(hl),735,445,25,WHITE)

        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((240, 109),(20, 26)))
        ab = random.randint(1,9)
        vertices.update({'ab':ab})
        display_text(str(ab),250,123,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((440, 109),(20, 26)))
        bc = random.randint(1,9)
        vertices.update({'bc':bc})
        display_text(str(bc),450,123,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((640, 109),(20, 26)))
        cd = random.randint(1,9)
        vertices.update({'cd':cd})
        display_text(str(cd),650,123,25,WHITE)

        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((240, 309),(20, 26)))
        ef = random.randint(1,9)
        vertices.update({'ef':ef})
        display_text(str(ef),250,323,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((440, 309),(20, 26)))
        fg = random.randint(1,9)
        vertices.update({'fg':fg})
        display_text(str(fg),450,323,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((640, 309),(20, 26)))
        gh = random.randint(1,9)
        vertices.update({'gh':gh})
        display_text(str(gh),650,323,25,WHITE)

        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((240, 509),(20, 26)))
        ij = random.randint(1,9)
        vertices.update({'ij':ij})
        display_text(str(ij),250,523,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((440, 509),(20, 26)))
        jk = random.randint(1,9)
        vertices.update({'jk':jk})
        display_text(str(jk),450,523,25,WHITE)
        pygame.draw.rect(win,pygame.Color('black'),pygame.Rect((640, 509),(20, 26)))
        kl = random.randint(1,9)
        vertices.update({'kl':kl})
        display_text(str(kl),650,523,25,WHITE)

        ad_vertices = [
        [0,1,0,0,1,0,0,0,0,0,0,0], #A
        [1,0,1,0,0,1,0,0,0,0,0,0], #B 
        [0,1,0,1,0,0,1,0,0,0,0,0], #C
        [0,0,1,0,0,0,0,1,0,0,0,0], #D
        [1,0,0,0,0,1,0,0,1,0,0,0], #E
        [0,1,0,0,1,0,1,0,0,1,0,0], #F
        [0,0,1,0,0,1,0,1,0,0,1,0], #G
        [0,0,0,1,0,0,1,0,0,0,0,1], #H
        [0,0,0,0,1,0,0,0,0,1,0,0], #I
        [0,0,0,0,0,1,0,0,1,0,1,0], #J
        [0,0,0,0,0,0,1,0,0,1,0,1], #K
        [0,0,0,0,0,0,0,1,0,0,1,0]  #L
                    ]

        ad_distances = {
        'A': {'B': vertices['ab'],'E': vertices['ae']},                                         #A
        'B': {'A': vertices['ab'],'C': vertices['bc'],'F':vertices['bf']},                      #B 
        'C': {'B': vertices['bc'],'D': vertices['cd'],'G': vertices['cg']},                     #C
        'D': {'C': vertices['cd'],'H': vertices['dh']},                                         #D
        'E': {'A': vertices['ae'],'F': vertices['ef'],'I': vertices['ei']},                     #E
        'F': {'B': vertices['bf'],'E': vertices['ef'],'G': vertices['fg'],'J': vertices['jf']}, #F
        'G': {'C': vertices['cg'],'F': vertices['fg'],'H': vertices['gh'],'K': vertices['gk']}, #G
        'H': {'D': vertices['dh'],'G': vertices['gh'],'L': vertices['hl']},                     #H
        'I': {'E': vertices['ei'],'J': vertices['ij']},                                         #I
        'J': {'F': vertices['jf'],'I': vertices['ij'],'K': vertices['jk']},                     #J
        'K': {'G': vertices['gk'],'J': vertices['jk'],'L': vertices['kl']},                     #K
        'L': {'H': vertices['hl'],'K': vertices['kl']}                                          #L
        } 
        counter += 1

    counter = 1

####################################################################################################################
    

    pygame.display.update()
    clock.tick(10)
