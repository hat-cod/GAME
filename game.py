import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)  # Black background
SQUARE_COLOR = (255, 0, 0)  # Red square
SQUARE_SIZE = 50
SPEED = 5

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Moving Square')

# Initialize the square's position
square_x = SCREEN_WIDTH // 2 - SQUARE_SIZE // 2
square_y = SCREEN_HEIGHT // 2 - SQUARE_SIZE // 2

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle key events for movement
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        square_x -= SPEED
    if keys[pygame.K_RIGHT]:
        square_x += SPEED
    if keys[pygame.K_UP]:
        square_y -= SPEED
    if keys[pygame.K_DOWN]:
        square_y += SPEED

    # Prevent the square from going out of bounds
    square_x = max(0, min(SCREEN_WIDTH - SQUARE_SIZE, square_x))
    square_y = max(0, min(SCREEN_HEIGHT - SQUARE_SIZE, square_y))

    # Fill the screen with the background color
    screen.fill(BACKGROUND_COLOR)

    # Draw the red square
    pygame.draw.rect(screen, SQUARE_COLOR, (square_x, square_y, SQUARE_SIZE, SQUARE_SIZE))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
