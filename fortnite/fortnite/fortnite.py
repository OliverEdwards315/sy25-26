import pygame
import math
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Shooter with Gun")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player properties
player_pos = [WIDTH // 2, HEIGHT // 2]
player_size = 20

# Gun properties
gun_length = 40
gun_width = 8
gun_color = (50, 50, 50)  # Dark gray

# Bullet properties
bullets = []
bullet_speed = 15

# Enemy properties
enemies = []
enemy_size = 30
enemy_speed = 2
SPAWN_ENEMY_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_ENEMY_EVENT, 1500)  # spawn every 1.5 sec

def spawn_enemy():
    x = random.randint(0, WIDTH)
    y = 0
    enemies.append([x, y])

def draw_gun(surface, position, angle):
    # Draw a rotated rectangle as a gun
    gun_surface = pygame.Surface((gun_length, gun_width))
    gun_surface.fill(gun_color)
    gun_surface.set_colorkey((0, 0, 0))
    # Rotate the gun surface
    rotated_gun = pygame.transform.rotate(gun_surface, -math.degrees(angle))
    rect = rotated_gun.get_rect()
    rect.center = position
    surface.blit(rotated_gun, rect.topleft)

def main():
    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == SPAWN_ENEMY_EVENT:
                    spawn_enemy()

            # Get mouse position for aiming
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx = mouse_x - player_pos[0]
            dy = mouse_y - player_pos[1]
            angle = math.atan2(dy, dx)

            # Shooting
            mouse_buttons = pygame.mouse.get_pressed()
            if mouse_buttons[0]:  # Left click to shoot
                # Add new bullet in the direction of the mouse
                bullets.append([player_pos[0], player_pos[1], angle])

            # Move bullets
            for bullet in bullets[:]:
                bullet[0] += bullet_speed * math.cos(bullet[2])
                bullet[1] += bullet_speed * math.sin(bullet[2])
                if not (0 <= bullet[0] <= WIDTH and 0 <= bullet[1] <= HEIGHT):
                    bullets.remove(bullet)

            # Move enemies downward
            for enemy in enemies[:]:
                enemy[1] += enemy_speed
                if enemy[1] > HEIGHT:
                    enemies.remove(enemy)

            # Check collisions
            for enemy in enemies[:]:
                for bullet in bullets[:]:
                    dist = math.hypot(enemy[0] - bullet[0], enemy[1] - bullet[1])
                    if dist < enemy_size / 2:
                        enemies.remove(enemy)
                        bullets.remove(bullet)
                        break

            # Drawing
            screen.fill(BLACK)

            # Draw player
            pygame.draw.circle(screen, WHITE, (int(player_pos[0]), int(player_pos[1])), player_size)

            # Draw gun as a rectangle rotated to face the mouse
            draw_gun(screen, player_pos, angle)

            # Draw bullets
            for bullet in bullets:
                pygame.draw.circle(screen, RED, (int(bullet[0]), int(bullet[1])), 5)

            # Draw enemies
            for enemy in enemies:
                pygame.draw.rect(screen, GREEN, (enemy[0] - enemy_size/2, enemy[1] - enemy_size/2, enemy_size, enemy_size))

            pygame.display.flip()
            clock.tick(60)
    except Exception as e:
        print("Error:", e)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()