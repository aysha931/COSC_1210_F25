# adventure_functions.py
import os
import pygame
import config

def simple_room(screen, row, col):
    left = col * config.ROOM_WIDTH
    right = left + config.ROOM_WIDTH
    top = row * config.ROOM_HEIGHT
    bottom = top + config.ROOM_HEIGHT
    mid_x = (left + right) // 2
    mid_y = (top + bottom) // 2

    # Top wall
    if row == 0:
        pygame.draw.line(screen, config.WALL_COLOR, (left, top), (right, top), config.WALL_THICK)

    # Bottom wall
    if row == config.GRID_ROWS - 1:
        pygame.draw.line(screen, config.WALL_COLOR, (left, bottom), (right, bottom), config.WALL_THICK)

    # Left wall
    if col == 0:
        pygame.draw.line(screen, config.WALL_COLOR, (left, top), (left, bottom), config.WALL_THICK)

    # Right wall
    if col == config.GRID_COLS - 1:
        pygame.draw.line(screen, config.WALL_COLOR, (right, top), (right, bottom), config.WALL_THICK)

def is_blocked(x, y):
    """Return True if the player is hitting a wall (excluding doors)"""
    for row in range(config.GRID_ROWS):
        for col in range(config.GRID_COLS):
            left = col * config.ROOM_WIDTH
            right = left + config.ROOM_WIDTH
            top = row * config.ROOM_HEIGHT
            bottom = top + config.ROOM_HEIGHT
            mid_x = (left + right) // 2
            mid_y = (top + bottom) // 2

            if left <= x <= right and top <= y <= bottom:
                return False
    return True

def draw_box(screen, kind_of_box):
    '''draws a simple rectangle'''
    rect_x = config.HEIGHT / 3
    rect_y = config.HEIGHT / 3
    rheight = 20
    rwidth = 20
    if kind_of_box == "trigger_ball_box":
        ball_trigger = pygame.Rect(rect_x, rect_y,rheight,rwidth)
        return ball_trigger
    
_player_image = None
_warned_once = False

def load_goose(direction):
    """Call once at startup after pygame.init()."""
    global _player_image, _warned_once
    _player_image = None  # default    

    if direction == "R":
        path = getattr(config, "PLAYER_IMAGE_R", None)
    if direction == "RS":
        path = getattr(config, "PLAYER_IMAGE_RS", None)
    if direction == "L":
        path = getattr(config, "PLAYER_IMAGE_L", None)
    if direction == "LS":
        path = getattr(config, "PLAYER_IMAGE_LS", None)
    size = getattr(config, "PLAYER_IMAGE_SIZE", None)
    if path and os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        if size:
            img = pygame.transform.smoothscale(img, size)
        _player_image = img
    else:
        if not _warned_once:
            print("No player image found or PLAYER_IMAGE_PATH not set; using circle.")
            _warned_once = True

def draw_player(screen, x, y):
    """Draw sprite centered at (x, y); fall back to circle if no image."""
    if _player_image:
        rect = _player_image.get_rect(center=(int(x), int(y)))
        screen.blit(_player_image, rect.topleft)
    else:
        pygame.draw.circle(screen, config.PLAYER_COLOR, (int(x), int(y)), config.PLAYER_RADIUS)
        pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), config.PLAYER_RADIUS, 2)

def show_game_over(screen):
    """Draw a Game Over box in the center of the screen."""
    font = pygame.font.Font(None, 72)  # default font, large size
    text = font.render("GAME OVER", True, (255, 255, 255))
    text_rect = text.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2))

    # Draw a semi-transparent dark box behind the text
    box_width = text_rect.width + 40
    box_height = text_rect.height + 40
    box_surface = pygame.Surface((box_width, box_height))
    box_surface.set_alpha(180)  # transparency
    box_surface.fill((0, 0, 0))
    box_rect = box_surface.get_rect(center=text_rect.center)

    # Blit box then text
    screen.blit(box_surface, box_rect)
    screen.blit(text, text_rect)
    pygame.display.flip()

    # Pause to let player see the message
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                waiting = False





