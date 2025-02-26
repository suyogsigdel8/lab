import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Define the grid size and player properties
grid_size = 20
player_size = grid_size
player_x, player_y = grid_size, grid_size
player_speed = grid_size

# Define the maze grid: 1 = wall, 0 = open path
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
   
]

# Define the exit point
exit_x, exit_y = 1, 18

# Define time limit (in milliseconds)
time_limit = 30000  # 30 seconds
start_time = pygame.time.get_ticks()

# Game loop
running = True
clock = pygame.time.Clock()
game_over = False
game_message = ""

while running:
    # Check if game is over
    if game_over:
        # Show game over message
        font = pygame.font.SysFont("Arial", 50)
        message = font.render(game_message, True, BLUE)
        screen.fill(WHITE)  # Fill the screen with white
        screen.blit(message, (width // 2 - message.get_width() // 2, height // 2 - message.get_height() // 2))
        pygame.display.flip()  # Update the display
        
        # Wait for user to press any key to close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN):
                running = False
        continue

    # Track elapsed time
    elapsed_time = pygame.time.get_ticks() - start_time
    remaining_time = max(0, time_limit - elapsed_time)  # Ensure non-negative time remaining

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed for movement
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player_x > 0 and maze[player_y // grid_size][(player_x - grid_size) // grid_size] == 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - grid_size and maze[player_y // grid_size][(player_x + grid_size) // grid_size] == 0:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0 and maze[(player_y - grid_size) // grid_size][player_x // grid_size] == 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < height - grid_size and maze[(player_y + grid_size) // grid_size][player_x // grid_size] == 0:
        player_y += player_speed

    # Check if the player has reached the exit
    if player_x == exit_x * grid_size and player_y == exit_y * grid_size:
        game_message = "You Win!"
        game_over = True

    # Check if time is up
    if elapsed_time >= time_limit:
        game_message = "Time's Up! You Lose!"
        game_over = True

    # Fill the screen with a background color
    screen.fill(BLACK)

    # Draw the maze
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            color = BLACK if maze[row][col] == 1 else WHITE
            pygame.draw.rect(screen, color, (col * grid_size, row * grid_size, grid_size, grid_size))

    # Draw the exit
    pygame.draw.rect(screen, GREEN, (exit_x * grid_size, exit_y * grid_size, grid_size, grid_size))

    # Draw the player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    # Draw the remaining time
    font = pygame.font.SysFont("Arial", 30)
    time_text = font.render(f"Time Remaining: {remaining_time // 1000}s", True, WHITE)
    screen.blit(time_text, (30, 500))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(10)

# Quit Pygame
pygame.quit()
