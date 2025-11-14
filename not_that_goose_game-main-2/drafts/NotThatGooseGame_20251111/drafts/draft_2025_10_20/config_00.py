# config.py

# Grid and Room Settings
GRID_ROWS = 3
GRID_COLS = 3
ROOM_WIDTH = 600
ROOM_HEIGHT = 600
WALL_THICK = 4
DOOR_SIZE = 40

# Player Settings
PLAYER_RADIUS = 10
PLAYER_SPEED = 100

# Screen Size
WIDTH = ROOM_WIDTH
HEIGHT = ROOM_HEIGHT

# Colors (R, G, B)
BG_COLOR = (55,79,47) # green
WALL_COLOR = (200, 200, 200)
PLAYER_COLOR = (100, 200, 255)
BOX_COLOR = (225,153,100)

# Frames Per Second
FPS = 60

# --- Player appearance ---
PLAYER_IMAGE_PATHL = "./goose_left.png"  # transparent PNG, e.g. 48x48
PLAYER_IMAGE_PATHLS = "./gooseLS.png"  # transparent PNG, e.g. 48x48
PLAYER_IMAGE_PATHR = "./goose_right.png"  # transparent PNG, e.g. 48x48
PLAYER_IMAGE_PATHRS = "./gooseRS.png"  # transparent PNG, e.g. 48x48
PLAYER_IMAGE_SIZE = (48, 48)             # w, h in pixels
PLAYER_RADIUS = 24                       # half of width; used by your collision


# Ball properties
ball_x = WIDTH // 2  # Initial x-position (center)
ball_y = HEIGHT // 2 # Initial y-position (center)
ball_radius = 20
ball_color = (255, 0, 0)  # Red

# Ball movement speed
ball_speed_x = 5
ball_speed_y = 5
