import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Fonts
font = pygame.font.Font(None, 36)
score_font = pygame.font.Font(None, 24)

# Snake properties
snake_pos = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (0, 1)  # (dx, dy)
snake_length = 1

# Food properties
food_types = {"apple": {"color": RED, "score": 1},
              "cherry": {"color": BLUE, "score": 2},
              "banana": {"color": YELLOW, "score": 3}}
current_food = random.choice(list(food_types.keys()))
food_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Score
score = 0

# Clock
clock = pygame.time.Clock()

# Functions
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def game_over():
    screen.fill(BLACK)
    draw_text("Game Over", font, WHITE, screen, WIDTH//2 - 100, HEIGHT//2 - 50)
    draw_text(f"Your Score: {score}", font, WHITE, screen, WIDTH//2 - 80, HEIGHT//2)
    draw_text("Press r to Restart", font, WHITE, screen, WIDTH//2 - 120, HEIGHT//2 + 50)
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False

def reset_game():
    global snake_pos, snake_direction, snake_length, score
    snake_pos = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    snake_direction = (0, 1)
    snake_length = 1
    score = 0

def spawn_food():
    global current_food, food_pos
    current_food = random.choice(list(food_types.keys()))
    food_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Game loop
running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)
    
    # Update snake position
    new_head = (snake_pos[0][0] + snake_direction[0], snake_pos[0][1] + snake_direction[1])
    snake_pos.insert(0, new_head)
    
    # Check for collision with food
    if snake_pos[0] == food_pos:
        score += food_types[current_food]["score"]
        spawn_food()
        snake_length += 1
    
    # Check for collision with walls or itself
    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= GRID_WIDTH or
        snake_pos[0][1] < 0 or snake_pos[0][1] >= GRID_HEIGHT or
        snake_pos[0] in snake_pos[1:]):
        game_over()
        reset_game()
    
    # Draw food
    pygame.draw.rect(screen, food_types[current_food]["color"], (food_pos[0] * GRID_SIZE, food_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    
    # Draw snake
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, (pos[0] * GRID_SIZE, pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    
    # Trim snake if it's too long
    if len(snake_pos) > snake_length:
        snake_pos.pop()
    
    # Display score
    draw_text(f"Score: {score}", score_font, WHITE, screen, 10, 10)
    
    pygame.display.flip()
    clock.tick(10)  # FPS

pygame.quit()

