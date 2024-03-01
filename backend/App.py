import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

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

# Create the display surface
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Bouncy Balls")

# Main loop
def main():
    running = True
    balls = generate_balls(100)  # Generate 20 moving balls
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

def generate_balls(num_balls):
    balls = []
    for _ in range(num_balls):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.randint(10, 30)
        color = random.choice(COLORS)  
        speed = random.uniform(1, 2)
        direction = random.uniform(0, 2*math.pi)
        balls.append(Ball(x, y, radius, color, speed, direction))
    return balls

class Ball:
    def __init__(self, x, y, radius, color, speed, direction):
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
        
        # Bounce off screen edges
        if self.x < 0 or self.x > WIDTH:
            self.direction = math.pi - self.direction
        if self.y < 0 or self.y > HEIGHT:
            self.direction = -self.direction
        
        # Slightly change size as the ball moves
        self.radius += random.randint(-1, 1)

        # Clamp radius to avoid negative sizes
        self.radius = max(1, self.radius)

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

if __name__ == "__main__":
    main()