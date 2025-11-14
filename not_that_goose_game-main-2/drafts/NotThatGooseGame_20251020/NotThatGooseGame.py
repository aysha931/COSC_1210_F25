import pygame
import config
import os
from adventure_functions import (
    draw_room, is_blocked, draw_obstacle, draw_player, load_player_image, show_game_over, simple_room
)

def main():
    pygame.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("3x3 Adventure Grid")
    clock = pygame.time.Clock()

    # Load the sprite ONCE
    load_player_image()

    player_x = config.WIDTH // 2
    player_y = config.HEIGHT // 2

    running = True
    while running:
        dt = clock.tick(config.FPS) / 1000.0
        
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if keys[pygame.K_ESCAPE]:
                show_game_over(screen)
                return
                running = False
                show_game_over(screen)
            #if player_x < 50 and player_y < 50:
            #    running = False
            #    show_game_over(screen)
        # non-ESP Input
        dx = dy = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: dx = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]: dy = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: dy = 1
        if dx != 0 and dy != 0:
            dx *= 0.7071
            dy *= 0.7071

        new_x = player_x + dx * config.PLAYER_SPEED * dt
        new_y = player_y + dy * config.PLAYER_SPEED * dt

        # Movement with collision
        if not is_blocked(new_x, new_y):
            player_x, player_y = new_x, new_y

        # Draw everything
        screen.fill(config.BG_COLOR)

        # Rooms/walls first
        for row in range(config.GRID_ROWS):
            for col in range(config.GRID_COLS):
                simple_room(screen, row, col)
                #draw_room(screen, row, col)

        # Any extra decor/obstacles
        draw_obstacle(screen)

        # Then the player
        draw_player(screen, player_x, player_y)

        pygame.display.flip()

    pygame.quit()
    os._exit
    #sys.exit()

if __name__ == "__main__":
    main()
