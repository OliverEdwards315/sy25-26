import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions and create the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Driving Simulator")

# Define car properties
car_width = 50
car_height = 100
car_color = (255, 0, 0)  # Red car

# Starting position of the car
car_x = screen_width // 2 - car_width // 2
car_y = screen_height - car_height - 10
car_speed = 5  # Speed of the car

# Load car image (optional, replace if you have an image of a car)
# car_image = pygame.image.load('car_image.png')  # Make sure to have a car image file

# Game clock for controlling the frame rate
clock = pygame.time.Clock()

# Function to draw the car
def draw_car(x, y):
    pygame.draw.rect(screen, car_color, (x, y, car_width, car_height))

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Fill the screen with black background

    # Handle events (keyboard inputs, quitting, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Control car movement with arrow keys
    if keys[pygame.K_LEFT]:
        car_x -= car_speed  # Move car left
    if keys[pygame.K_RIGHT]:
        car_x += car_speed  # Move car right
    if keys[pygame.K_UP]:
        car_y -= car_speed  # Move car up
    if keys[pygame.K_DOWN]:
        car_y += car_speed  # Move car down

    # Prevent the car from going off-screen
    if car_x < 0:
        car_x = 0
    if car_x > screen_width - car_width:
        car_x = screen_width - car_width
    if car_y < 0:
        car_y = 0
    if car_y > screen_height - car_height:
        car_y = screen_height - car_height

    # Draw the car on the screen
    draw_car(car_x, car_y)

    # Update the screen
    pygame.display.update()

    # Control the frame rate (frames per second)
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
