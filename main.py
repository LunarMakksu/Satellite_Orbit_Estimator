import pygame
import math
from PIL import Image
pygame.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Satellite Estimator")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (5, 0, 159)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
ORANGE = (255,165,0)
BLACK = (0, 0 , 0)

FONT = pygame.font.SysFont("courier", 20)
global img_fp 
#img_fp = Image.open("iss.gif")

class Earth:
        x = 500
        y = 400
        colour = LIGHT_BLUE
        radius = 100

def Draw(win):
    pygame.draw.circle(win, Earth.colour, (Earth.x, Earth.y), Earth.radius)

class Satellite:
        AU = 149.6e6 * 1000
        G = 6.67428e-11
        SCALE = 250 / AU  # 1AU = 100 pixels
        TIMESTEP = 3600*24 # 1 day

        def __init__(self, x, y, colour, mass, altitude):
            self.x = x
            self.y = y
            self.colour = colour
            self.mass = mass
            self.altitude = altitude 

            #img = img_fp

            self.orbit = []
            self.earth = False
            
            self.x_vel = 0
            self.y_vel = 0


        def draw(self, win):
            x = self.x * self.SCALE + WIDTH / 2
            y = self.y * self.SCALE + HEIGHT / 2

            if len(self.orbit) > 2:
                updated_points = []
                for point in self.orbit:
                    x, y = point
                    x = x * self.SCALE + WIDTH / 2
                    y = y * self.SCALE + HEIGHT / 2
                    updated_points.append((x, y))

                pygame.draw.lines(win, self.color, False, updated_points, 2)
            
            pygame.draw.circle(win, self.colour, (x, y), self.radius)


def main():
    run = True
    clock_elapsed = pygame.time.Clock()

    while run:
        clock_elapsed.tick(60)
        WIN.fill(BLACK)

        EARTH = Earth

        Draw(WIN)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    pygame.quit()

main()