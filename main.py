import pygame
import random

WIDTH, HEIGHT = 550, 550
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")


FPS = 60

rectangles = []
mine = []

crect = pygame.Surface((50,50))
crect.fill((125,125,125))

def draw_window():
    sentx = 10
    senty = 10
    mines = 10
    WIN.fill((0,0,0))
    while(sentx < 550):
        while(senty < 550):

            if(random.randint(1,9) == 1 and mines > 0):
                mine.append(1)
                mines = mines - 1
                rectangles.append(pygame.draw.rect((WIN), (125, 0, 125), (sentx, senty, 50, 50)))
            else:
                mine.append(0)
                rectangles.append(pygame.draw.rect((WIN), (125, 125, 125), (sentx, senty, 50, 50)))
            senty = senty + 60
        senty = 10

        sentx = sentx + 60
    pygame.display.update()


def main():
    draw_window()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False

        sent = 0
        for rect in rectangles:
            mines = 0
            if(sent < 80):
                if(mine[sent + 1] == 1):
                    mines = mines + 1
            if(sent > 0):
                if (mine[sent - 1] == 1):
                    mines = mines + 1
            if(sent < 73):
                if (mine[sent + 8] == 1):
                    mines = mines + 1
            if(sent < 72):
                if (mine[sent + 9] == 1):
                    mines = mines + 1
            if(sent < 71):
                if (mine[sent + 10] == 1):
                    mines = mines + 1
            if(sent > 7):
                if (mine[sent - 8] == 1):
                    mines = mines + 1
            if(sent > 8):
                if (mine[sent - 9] == 1):
                    mines = mines + 1
            if(sent > 9):
                if (mine[sent - 10] == 1):
                    mines = mines + 1

            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(rect.collidepoint(pygame.mouse.get_pos())):
                    if(mine[sent] == 1):
                        run = False
                    else:
                        if(mines == 1):
                            pygame.draw.rect((WIN), (0, 50, 125), (rect.x, rect.y, 50, 50))
                        elif(mines == 2):
                            pygame.draw.rect((WIN), (100,100,50), (rect.x, rect.y, 50, 50))
                        elif (mines == 3):
                            pygame.draw.rect((WIN), (100, 50, 225), (rect.x, rect.y, 50, 50))
                        elif (mines == 4):
                            pygame.draw.rect((WIN), (150, 100, 0), (rect.x, rect.y, 50, 50))
                        elif (mines == 5):
                            pygame.draw.rect((WIN), (50, 50, 12), (rect.x, rect.y, 50, 50))
                        elif (mines == 6):
                            pygame.draw.rect((WIN), (50, 255, 50), (rect.x, rect.y, 50, 50))
                        elif (mines == 7):
                            pygame.draw.rect((WIN), (200, 50, 125), (rect.x, rect.y, 50, 50))
                        elif (mines == 8):
                            pygame.draw.rect((WIN), (200, 100, 50), (rect.x, rect.y, 50, 50))
                        else:
                            pygame.draw.rect((WIN), (0,125,125), (rect.x, rect.y, 50,50))
                        pygame.display.update()



            sent = sent + 1


    pygame.quit()

if __name__ == "__main__":
    main()

