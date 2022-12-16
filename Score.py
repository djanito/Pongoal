import pygame
import constants as const

class Score (pygame.sprite.Sprite):
	def __init__ (self):
		super(Score, self).__init__()
		self.score = 0
		self.sheet = pygame.image.load("png/numbers_score.png").convert_alpha()
		self.tiles = 10

		w, h = self.sheet.get_width(), self.sheet.get_height()
		cols, rows = 4, 3
		tw = w / cols
		th = h / rows

		self.numbers = list([pygame.Rect((tw * i) % w, (i// cols) * th, tw, th) for i in range(self.tiles)])
		self.rect = self.numbers[self.score]
		

	def score_up(self):
		self.score += 1
		self.rect = self.numbers[self.score]

	def draw(self, surface, x):
		surface.blit(self.sheet, (x, const.SCREEN_HEIGHT//2 - self.rect.h//2), self.rect)