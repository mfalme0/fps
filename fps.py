import psutil
import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("System Monitor")

# Set up the font
FONT_SIZE = 20
font = pygame.font.SysFont(None, FONT_SIZE)

# Set up the clock
clock = pygame.time.Clock()

# Main loop
while True:
    # Get system vitals
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent

    # Get FPS
    fps = int(clock.get_fps())

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Render text for system vitals
    cpu_text = font.render(f"CPU: {cpu_percent}%", True, (0, 0, 0))
    memory_text = font.render(f"Memory: {memory_percent}%", True, (0, 0, 0))

    # Render text for FPS
    fps_text = font.render(f"FPS: {fps}", True, (0, 0, 0))

    # Blit text to the screen
    screen.blit(cpu_text, (10, 10))
    screen.blit(memory_text, (10, 40))
    screen.blit(fps_text, (SCREEN_WIDTH - 70, 10))

    # Update the display
    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Tick the clock
    clock.tick(60)
