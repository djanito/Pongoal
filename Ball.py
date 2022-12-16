import pygame
import constants as const
from Spritesheet import Spritesheet
import random

class Ball(pygame.sprite.Sprite):

    shadow = pygame.image.load("png/ball_shadow.png")
    shadow_rect = shadow.get_rect()

    def __init__(self, filename, cols, rows, color=None):
        super().__init__()
        self.speed_x = const.BALL_SPEED_X * random.choice([-1, 1])
        self.speed_y = const.BALL_SPEED_Y * random.choice([-1, 1])
        self.sprite = Spritesheet(filename, cols, rows, 2, color)
        self.rect = pygame.Rect(const.SCREEN_WIDTH//2 - self.sprite.rect.w//2, const.SCREEN_HEIGHT//2 - self.sprite.rect.h//2, self.sprite.rect.w, self.sprite.rect.h)
        self.mask = pygame.mask.from_surface(self.sprite.image)

    def set_ball_at_center(self):
        self.rect.center = (const.SCREEN_WIDTH//2, const.SCREEN_HEIGHT//2)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        Ball.shadow_rect.centerx = self.rect.centerx + 2
        Ball.shadow_rect.centery = self.rect.centery + 2
        
        self.animate()

    def animate(self):
        self.sprite.animate()

    def vertical_wall_collision(self, game_area):
        return self.rect.right >= game_area.right or self.rect.left <= game_area.left

    def horizontal_wall_collision(self, game_area):
        return self.rect.top <= game_area.top or self.rect.bottom >= game_area.bottom

    def paddle_collision(self, player, opponent):
        player_rect = player.rect
        opponent_rect = opponent.rect

        if self.rect.colliderect(player_rect) and self.speed_x < 0:
            if abs(self.rect.left - player_rect.right) < const.BALL_SPEED_X:
                player.set_is_animate(True)
                self.speed_x *= -1
            elif abs(self.rect.bottom - player_rect.top) < const.BALL_SPEED_Y and self.speed_y > 0:
                player.set_is_animate(True)
                self.speed_y *= -1
            elif abs(self.rect.top - player_rect.bottom) < const.BALL_SPEED_Y and self.speed_y < 0:
                player.set_is_animate(True)
                self.speed_y *= -1

        if self.rect.colliderect(opponent_rect) and self.speed_x > 0:
            if abs(self.rect.right - opponent_rect.left) < const.BALL_SPEED_X:
                opponent.set_is_animate(True)
                self.speed_x *= -1

    def respawn(self, current_time, score_time):
        if (current_time - score_time) < 2100:
            self.speed_x, self.speed_y = 0, 0
        else:
            self.speed_x = const.BALL_SPEED_X * random.choice([-1, 1])
            self.speed_y = const.BALL_SPEED_Y * random.choice([-1, 1])
            score_time = None

        return score_time

    def draw(self, screen):
        screen.blit(Ball.shadow, Ball.shadow_rect) # draw shadow
        self.sprite.draw(screen, self.rect.x, self.rect.y) # draw animated ball