import pygame, time

WHITE, BLACK = (255,255,255) , (0,0,0)
SCALE = 10
WIDTH, HEIGHT = (960,720)
OFFSET = 0.061

pygame.init()
display = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

pygame.mixer.music.load("ba.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

files = open("data.txt", "r")
x,y = 0,0
counter = 0 

for lines in files:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.display.quit()
            raise SystemExit

    currentLine = files.readline()
    if currentLine.find("1") != -1:
        for data in currentLine:
            if data == '1': pygame.draw.rect(display, WHITE ,pygame.Rect((x*20,y*SCALE), (2,1)))
            else: pygame.draw.rect(display, BLACK ,pygame.Rect((x*20,y*SCALE), (20,SCALE)))
            y += 1

    x += 1
    x %= WIDTH // 10
    y = 0
    counter += 1

    if not counter % 96: 
        pygame.display.flip()
        display.fill(BLACK)
        time.sleep(OFFSET)

