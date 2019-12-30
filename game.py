import pygame
import random
from pygame import freetype
import time

# Text Displaying
# Choose font size: game_font = pygame.freetype.Font("Font.ttf", 24)
# Choose text to render: text_surface, rect = game_font.render(("Monster Clash"), (0, 0, 0))
# choose where to put it: gameDisplay.blit(text_surface, (240, 100))


# Initialize the game engine
pygame.init()


DisplayWidth,DisplayHeight = 800, 800
clock = pygame.time.Clock()
game_font = pygame.freetype.Font("Font.ttf", 50)

gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))
pygame.display.set_caption("Puzzle")

def boardScramble(board,boardColors,boardXy):
    for i in range(2):
        for i in range(5):
            for i in range(2):
                rannum = random.randint(1,2)
                if rannum == 1:
                    rannum2 = random.randint(1,2)
                    if rannum2 == 1:
                        Type = "right"
                    else:
                        Type = "left"
                    num = random.randint(0,4) * 5
                    num1 = boardXy[0+num]
                    num2 = boardXy[1+num]
                    num3 = boardXy[2+num]
                    num10 = boardXy[3+num]
                    num11 = boardXy[4+num]
                    
                    num4 = board[0+num]
                    num5 = board[1+num]
                    num6 = board[2+num]
                    num12 = board[3+num]
                    num13 = board[4+num]
                    
                    num7 = boardColors[0+num]
                    num8 = boardColors[1+num]
                    num9 = boardColors[2+num]
                    num14 = boardColors[3+num]
                    num15 = boardColors[4+num]
                    if Type == "left":
                        boardColors[0+num] = num15
                        boardColors[1+num] = num7
                        boardColors[2+num] = num8
                        boardColors[3+num] = num9
                        boardColors[4+num] = num14
                        board[0+num] = num13
                        board[1+num] = num4
                        board[2+num] = num5
                        board[3+num] = num6
                        board[4+num] = num12
                        boardXy[0+num] = num11
                        boardXy[1+num] = num1
                        boardXy[2+num] = num2
                        boardXy[3+num] = num3
                        boardXy[4+num] = num10
                    else:
                        boardColors[0+num] = num8
                        boardColors[1+num] = num9
                        boardColors[2+num] = num14
                        boardColors[3+num] = num15
                        boardColors[4+num] = num7
                        board[0+num] = num5
                        board[1+num] = num6
                        board[2+num] = num12
                        board[3+num] = num13
                        board[4+num] = num4
                        boardXy[0+num] = num2
                        boardXy[1+num] = num3
                        boardXy[2+num] = num10
                        boardXy[3+num] = num11
                        boardXy[4+num] = num1
                else:
                    rannum2 = random.randint(1,2)
                    if rannum2 == 1:
                        Type = "down"
                    else:
                        Type = "up"
                    num = random.randint(1,4)
                    num1 = boardXy[0+num]
                    num2 = boardXy[5+num]
                    num3 = boardXy[10+num]
                    num10 = boardXy[15+num]
                    num11 = boardXy[20+num]
                    num4 = board[0+num]
                    num5 = board[5+num]
                    num6 = board[10+num]
                    num12 = board[15+num]
                    num13 = board[20+num]
                    num7 = boardColors[0+num]
                    num8 = boardColors[5+num]
                    num9 = boardColors[10+num]
                    num14 = boardColors[15+num]
                    num15 = boardColors[20+num]
                    if Type == "down":
                        boardColors[0+num] = num15
                        boardColors[5+num] = num7
                        boardColors[10+num] = num8
                        boardColors[15+num] = num9
                        boardColors[20+num] = num14
                        board[0+num] = num13
                        board[5+num] = num4
                        board[10+num] = num5
                        board[15+num] = num6
                        board[20+num] = num12
                        boardXy[0+num] = num11
                        boardXy[5+num] = num1
                        boardXy[10+num] = num2
                        boardXy[15+num] = num3
                        boardXy[20+num] = num10
                    else:
                        boardColors[0+num] = num8
                        boardColors[5+num] = num9
                        boardColors[10+num] = num14
                        boardColors[15+num] = num15
                        boardColors[20+num] = num7
                        board[0+num] = num5
                        board[5+num] = num6
                        board[10+num] = num12
                        board[15+num] = num13
                        board[20+num] = num4
                        boardXy[0+num] = num2
                        boardXy[5+num] = num3
                        boardXy[10+num] = num10
                        boardXy[15+num] = num11
                        boardXy[20+num] = num1   

    return [board,boardColors,boardXy]
    

def draw(x,y,color,num):
    pygame.draw.rect(gameDisplay, color, (x, y, 200, 200), 0)

    text_surface, rect = game_font.render(str(num), (0, 0, 0))
    if num >= 10:
        gameDisplay.blit(text_surface, (x+60, y+60))
    else:
        gameDisplay.blit(text_surface, (x+70, y+60))

def drawOutline(x,y):
    pygame.draw.rect(gameDisplay, (0,0,0), (x, y, 160, 160), 5)
        

def game_loop():
    game_run = True
    finished = False

    board = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    boardXy = [[0,0],[160,0],[320,0],[480,0],[640,0],[0,160],[160,160],[320,160],[480,160],[640,160],[0,320],[160,320],[320,320],[480,320],[640,320],[0,480],[160,480],[320,480],[480,480],[640,480],[0,640],[160,640],[320,640],[480,640],[640,640]]
    boardColors = [(255,0,0),(245,5,0),(235,10,0),(225,15,0),(215,20,0),(205,25,30),(195,30,30),(185,35,30),(175,40,30),(165,45,30),(155,50,60),(145,55,60),(135,60,60),(125,65,60),(115,70,60),(105,75,90),(95,80,90),(85,85,90),(75,90,90),(65,95,90),(55,100,120),(45,105,120),(35,110,120),(25,115,120),(15,120,120)]

    scrambled = []
    scrambled = boardScramble(board,boardColors,boardXy)
    board = scrambled[0]
    boardColors = scrambled[1]
    boardXy = scrambled[2]
    startClock = time.process_time()* 2
    
    x = 0
    y = 0
    

    while game_run == True:

        gameDisplay.fill((50, 50, 50))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if y > 0:
                        y -= 160
                if event.key == pygame.K_DOWN:
                    if y < 640:
                        y += 160
                if event.key == pygame.K_RIGHT:
                    if x < 640:
                        x += 160
                if event.key == pygame.K_LEFT:
                    if x > 0:
                        x -= 160
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    if event.key == pygame.K_a:
                        Type = "right"
                    else:
                        Type = "left"
                    if y == 0:
                        num = 0
                    if y == 160:
                        num = 5
                    if y == 320:
                        num = 10
                    if y == 480:
                        num = 15
                    if y == 640:
                        num = 20
                    num1 = boardXy[0+num]
                    num2 = boardXy[1+num]
                    num3 = boardXy[2+num]
                    num10 = boardXy[3+num]
                    num11 = boardXy[4+num]
                    
                    num4 = board[0+num]
                    num5 = board[1+num]
                    num6 = board[2+num]
                    num12 = board[3+num]
                    num13 = board[4+num]
                    
                    num7 = boardColors[0+num]
                    num8 = boardColors[1+num]
                    num9 = boardColors[2+num]
                    num14 = boardColors[3+num]
                    num15 = boardColors[4+num]
                    if Type == "left":
                        boardColors[0+num] = num15
                        boardColors[1+num] = num7
                        boardColors[2+num] = num8
                        boardColors[3+num] = num9
                        boardColors[4+num] = num14
                        board[0+num] = num13
                        board[1+num] = num4
                        board[2+num] = num5
                        board[3+num] = num6
                        board[4+num] = num12
                        boardXy[0+num] = num11
                        boardXy[1+num] = num1
                        boardXy[2+num] = num2
                        boardXy[3+num] = num3
                        boardXy[4+num] = num10
                    else:
                        boardColors[0+num] = num8
                        boardColors[1+num] = num9
                        boardColors[2+num] = num14
                        boardColors[3+num] = num15
                        boardColors[4+num] = num7
                        board[0+num] = num5
                        board[1+num] = num6
                        board[2+num] = num12
                        board[3+num] = num13
                        board[4+num] = num4
                        boardXy[0+num] = num2
                        boardXy[1+num] = num3
                        boardXy[2+num] = num10
                        boardXy[3+num] = num11
                        boardXy[4+num] = num1
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    if event.key == pygame.K_s:
                        Type = "down"
                    else:
                        Type = "up"
                    if x == 0:
                        num = 0
                    if x == 160:
                        num = 1
                    if x == 320:
                        num = 2
                    if x == 480:
                        num = 3
                    if x == 640:
                        num = 4
                    num1 = boardXy[0+num]
                    num2 = boardXy[5+num]
                    num3 = boardXy[10+num]
                    num10 = boardXy[15+num]
                    num11 = boardXy[20+num]
                    num4 = board[0+num]
                    num5 = board[5+num]
                    num6 = board[10+num]
                    num12 = board[15+num]
                    num13 = board[20+num]
                    num7 = boardColors[0+num]
                    num8 = boardColors[5+num]
                    num9 = boardColors[10+num]
                    num14 = boardColors[15+num]
                    num15 = boardColors[20+num]
                    if Type == "down":
                        boardColors[0+num] = num15
                        boardColors[5+num] = num7
                        boardColors[10+num] = num8
                        boardColors[15+num] = num9
                        boardColors[20+num] = num14
                        board[0+num] = num13
                        board[5+num] = num4
                        board[10+num] = num5
                        board[15+num] = num6
                        board[20+num] = num12
                        boardXy[0+num] = num11
                        boardXy[5+num] = num1
                        boardXy[10+num] = num2
                        boardXy[15+num] = num3
                        boardXy[20+num] = num10
                    else:
                        boardColors[0+num] = num8
                        boardColors[5+num] = num9
                        boardColors[10+num] = num14
                        boardColors[15+num] = num15
                        boardColors[20+num] = num7
                        board[0+num] = num5
                        board[5+num] = num6
                        board[10+num] = num12
                        board[15+num] = num13
                        board[20+num] = num4
                        boardXy[0+num] = num2
                        boardXy[5+num] = num3
                        boardXy[10+num] = num10
                        boardXy[15+num] = num11
                        boardXy[20+num] = num1
                        


        for i in range(25):
            draw(boardXy[board.index(i+1)][0],boardXy[board.index(i+1)][1],boardColors[i],board[i])

        drawOutline(x,y)

        

        pygame.display.flip()
        clock.tick(20)

        if finished == True:
            print("Time: " + str(timeTooken2))
            time.sleep(2)
            game_loop()
            

        if board == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] and scrambled != []:
            timeTooken = str(time.process_time()*2 - startClock)
            count = 0
            timeTooken2 = ""
            for i in range(len(timeTooken)):
                if timeTooken[i] == ".":
                    count = i
            for i in range(count + 3):
                timeTooken2 += timeTooken[i]

            finished = True


game_loop()
