import pygame
from Score import Score
import constants as const
from Spritesheet import Spritesheet

class Paddle(pygame.sprite.Sprite):

    def __init__(self, number, filename, cols, rows, color=None):
        super(Paddle, self).__init__()
        self.sprite = Spritesheet(filename, cols, rows, 1, color)
        if number == 1:
            x = const.PLAYER_X
        else:
            x = const.OPPONENT_X - self.sprite.rect.w
        self.rect = pygame.Rect(x, const.SCREEN_HEIGHT//2 - self.sprite.rect.h//2, self.sprite.rect.w, self.sprite.rect.h)
        self.speed = const.PADDLE_SPEED
        self.score = Score()
        self.is_animated = False

    # --- Class Methods ---
    def move(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if pressed_keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def set_is_animated(self, is_animated):
        self.is_animated = is_animated

    def bounce_animation(self):
        self.is_animated = self.sprite.animate_full(self.is_animated)

    def ia_move(self, ball_rect):
        if ball_rect.centery > self.rect.centery:
            self.rect.centery += self.speed
        if ball_rect.centery < self.rect.centery:
            self.rect.centery -= self.speed

    def wall_collision(self, game_area):
        if (self.rect.top <= game_area.top):
            self.rect.y = game_area.top 
        if (self.rect.bottom >= game_area.bottom):
            self.rect.bottom = game_area.bottom

    def score_up(self):
        self.score.score_up()

    def draw_score(self, screen, y):
        self.score.draw(screen, y)

    def draw(self, screen):
        self.bounce_animation()
        self.sprite.draw(screen, self.rect.x, self.rect.y)


