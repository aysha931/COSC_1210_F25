import pygame, random, math
import config_goose as config

# --------- Game objects ---------
class Ball:
    def __init__(self, x, y, vx, vy, color=None):
        self.x, self.y = float(x), float(y)
        self.vx, self.vy = float(vx), float(vy)
        self.r = config.BALL_RADIUS
        self.color = color or config.BALL_COLOR

    @property
    def rect(self):
        return pygame.Rect(int(self.x - self.r), int(self.y - self.r), self.r*2, self.r*2)

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        # bounce on walls
        if self.x - self.r <= 0:
            self.x = self.r
            self.vx *= -1
        elif self.x + self.r >= config.WIDTH:
            self.x = config.WIDTH - self.r
            self.vx *= -1
        if self.y - self.r <= 0:
            self.y = self.r
            self.vy *= -1
        elif self.y + self.r >= config.HEIGHT:
            self.y = config.HEIGHT - self.r
            self.vy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.r)

class Bread:
    def __init__(self, x, y):
        self.x, self.y = int(x), int(y)

    @property
    def center(self):
        return (self.x, self.y)

    @property
    def rect(self):
        # approximate bread as a 20x20 rect centered on (x,y)
        w, h = config.BREAD_IMAGE_SIZE
        return pygame.Rect(self.x - w//2, self.y - h//2, w, h)
