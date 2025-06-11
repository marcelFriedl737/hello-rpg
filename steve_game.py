# Simple Pygame Example: Move Steve the Red Square with WASD
import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move Steve the Red Square!")
clock = pygame.time.Clock()

# Steve's properties
steve_size = 50
steve_color = (255, 0, 0)  # Red
steve_pos = [WIDTH // 2, HEIGHT // 2]
steve_speed = 5

# Power-up properties
powerup_size = 20
powerup_color = (0, 255, 0)  # Green
powerup_spawn_time = 2000  # milliseconds
powerups = []
last_powerup_time = pygame.time.get_ticks()

# Steve's strength
steve_strength = 1
font = pygame.font.SysFont(None, 36)

class PowerUp:
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.speed = 3
    def move_away_from(self, target_pos):
        tx, ty = target_pos
        px, py = self.rect.center
        dx = px - tx
        dy = py - ty
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist > 0:
            dx /= dist
            dy /= dist
            self.rect.x += int(dx * self.speed)
            self.rect.y += int(dy * self.speed)
        # Wrap around screen for boundless movement
        if self.rect.left > WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = HEIGHT

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn power-ups at intervals
    current_time = pygame.time.get_ticks()
    if current_time - last_powerup_time > powerup_spawn_time:
        x = random.randint(0, WIDTH - powerup_size)
        y = random.randint(0, HEIGHT - powerup_size)
        powerups.append(PowerUp(x, y, powerup_size, powerup_color))
        last_powerup_time = current_time

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        steve_pos[1] -= steve_speed
    if keys[pygame.K_s]:
        steve_pos[1] += steve_speed
    if keys[pygame.K_a]:
        steve_pos[0] -= steve_speed
    if keys[pygame.K_d]:
        steve_pos[0] += steve_speed

    # Wrap Steve around the screen
    if steve_pos[0] < 0:
        steve_pos[0] = WIDTH - steve_size
    elif steve_pos[0] > WIDTH - steve_size:
        steve_pos[0] = 0
    if steve_pos[1] < 0:
        steve_pos[1] = HEIGHT - steve_size
    elif steve_pos[1] > HEIGHT - steve_size:
        steve_pos[1] = 0

    # Move power-ups away from Steve
    steve_center = (steve_pos[0] + steve_size // 2, steve_pos[1] + steve_size // 2)
    for p in powerups:
        p.move_away_from(steve_center)

    # Check for collision with power-ups
    steve_rect = pygame.Rect(*steve_pos, steve_size, steve_size)
    new_powerups = []
    for p in powerups:
        if steve_rect.colliderect(p.rect):
            steve_strength += 1
            steve_size_increase = 2
            steve_size += steve_size_increase
        else:
            new_powerups.append(p)
    powerups = new_powerups

    screen.fill((30, 30, 30))  # Dark background
    # Draw power-ups
    for p in powerups:
        pygame.draw.rect(screen, p.color, p.rect)
    # Draw Steve
    pygame.draw.rect(screen, steve_color, (*steve_pos, steve_size, steve_size))
    # Draw strength
    strength_text = font.render(f"Strength: {steve_strength}", True, (255, 255, 255))
    screen.blit(strength_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
