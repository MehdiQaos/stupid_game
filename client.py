import pygame
from network import Network

width = 500
height = 500
VEL = 1
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Client')

client_number = 0


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = x, y, width, height

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: self.x += VEL
        if keys[pygame.K_LEFT]: self.x -= VEL
        if keys[pygame.K_DOWN]: self.y += VEL
        if keys[pygame.K_UP]: self.y -= VEL
        self.update_pos()

    def update_pos(self):
        self.rect = self.x, self.y, self.width, self.height


def redraw_window(win, player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    start_position = n.get_pos()
    p = Player(50,50,100,100,(0,255,0))
    p2 = Player(0,0,100,100,(255,0,0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        p2.x, p2.y = n.send((p.x, p.y))
        p2.update_pos()

        redraw_window(win, p, p2)

main()