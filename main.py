import pygame
mw = pygame.display.set_mode(
    (500, 500)
)
LIGHT_BLUE = (200, 200, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
clock = pygame.time.Clock()
mw.fill(LIGHT_BLUE)

class Area():
    def __init__(self, x, y, widht, height, color):
        self.rect = pygame.Rect(x, y, widht, height)
        self.color = color
    def set_color(self, new_color):
        self.color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.color, self.rect,)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)

class Picture(Area):
    def __init__(self, filename, x, y, widht, height, color):
        Area.__init__(self, x, y, widht, height, color)
        self.image  = pygame.transform.scale(pygame.image.load(filename), (widht, height))

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

ball = Picture('ball.png', 100, 100, 50, 50, RED)
platform = Picture('plat.png', 200, 200, 100, 30, RED)
x, y = 10, 10
x_shift = 25
count = 8
lines = 3
blocks = list()

for j in range(lines):
    for i in range(count):
        block = Picture('block.jfif', x, y, 55, 55, RED)
        x += 60
        blocks.append(block)
    x = 10 
    x+= x_shift
    x_shift+= 25
    y += 60
    count -= 1

while True:
    ball.draw()
    platform.draw()
    for block in blocks:
        block.draw()

    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
    pygame.display.update()
    clock.tick(40)