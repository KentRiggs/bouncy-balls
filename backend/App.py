import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WIDTH, HEIGHT = 800, 600

# Define colors (primary bold color palette)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, CYAN, MAGENTA]

# Background color
BACKGROUND_COLOR = (0, 0, 0)

def get_user_input():
    # Collect user inputs
    username = input("Enter your name: ")
    print(f"Welcome to the Bouncy Balls Simulator, {username}!")  # Personalized welcome message
    num_balls = int(input("Enter the number of balls: "))
    min_size = int(input("Enter minimum ball size as low as 1: "))
    max_size = int(input("Enter maximum ball size up to 100: "))
    return username, num_balls, min_size, max_size

def generate_balls(screen, num_balls, min_size, max_size):
    balls = []
    for _ in range(num_balls):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.randint(min_size, max_size)
        color = random.choice(COLORS)
        speed = random.uniform(1, 2)
        direction = random.uniform(0, 2 * math.pi)
        balls.append(Ball(screen, x, y, radius, color, speed, direction))
    return balls

class Ball:
    def __init__(self, screen, x, y, radius, color, speed, direction):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.direction = direction

    def update(self):
        # Update position based on speed and direction
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)

        # Make balls oscillate as they move
        self.direction += random.uniform(-0.1, 0.1)  # Adjust the direction slightly
        
        # Bounce off screen edges with a more dynamic angle change
        if self.x < 0 or self.x > WIDTH:
            self.direction = math.pi - self.direction + random.uniform(-0.5, 0.5)
        if self.y < 0 or self.y > HEIGHT:
            self.direction = -self.direction + random.uniform(-0.5, 0.5)
        
        # Slightly change size as the ball moves
        self.radius += random.randint(-1, 1)

        # Clamp radius to avoid negative sizes
        self.radius = max(1, self.radius)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)

def main(num_balls, min_size, max_size):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bouncy Balls")

    running = True
    balls = generate_balls(screen, num_balls, min_size, max_size)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        # Update and draw balls
        for ball in balls:
            ball.update()
            ball.draw()

        pygame.display.flip()
        pygame.time.delay(5)  # Delay for smooth animation

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    username, num_balls, min_size, max_size = get_user_input()
    print(f"Starting the simulation for {username} with {num_balls} balls.")
    main(num_balls, min_size, max_size)
