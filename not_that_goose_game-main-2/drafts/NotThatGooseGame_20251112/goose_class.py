import config_goose as config

class Ball:
    def __init__(self):
        self.x = random.randint(config.BALL_RADIUS, WIDTH - config.BALL_RADIUS)
        self.y = random.randint(config.BALL_RADIUS, HEIGHT - config.BALL_RADIUS)
        self.vx = random.choice([-4, -3, 3, 4])
        self.vy = random.choice([-4, -3, 3, 4])
        self.color = (random.randint(50,255), random.randint(50,255), random.randint(50,255))

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Bounce off walls
        if self.x <= config.BALL_RADIUS or self.x >= WIDTH - config.BALL_RADIUS:
            self.vx *= -1
        if self.y <= config.BALL_RADIUS or self.y >= HEIGHT - config.BALL_RADIUS:
            self.vy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), config.BALL_RADIUS)

    def check_collision(self, other):
        dist = math.hypot(self.x - other.x, self.y - other.y)
        return dist < config.BALL_RADIUS * 2
    
    class Bread:
    def __init__(self):
        self.x = random.randint(config.BREAD_RADIUS, WIDTH - config.BREAD_RADIUS)
        self.y = random.randint(config.BREAD_RADIUS, HEIGHT - config.BREAD_RADIUS)

    def draw(self, screen):
        rect = _bread_image.get_rect(center=(int(x), int(y)))
        pygame.draw.circle(screen, self.color, (self.x, self.y), BALL_RADIUS)



    def check_collision(self, other):
        dist = math.hypot(self.x - other.x, self.y - other.y)
        return dist < BALL_RADIUS * 2