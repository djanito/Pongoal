import pygame as pg
from Ball import Ball
from Paddle import Paddle
from Particle import Particle
import constants as const

bg = pg.image.load("png/court_01.png")
goals_post_left = pg.image.load("png/goal_posts_left.png")
goals_post_left_rect = goals_post_left.get_rect(center = (70, const.SCREEN_HEIGHT//2 - 6//2))

goals_post_right = pg.image.load("png/goal_posts_right.png")
goals_post_right_rect = goals_post_right.get_rect(center = (const.SCREEN_WIDTH - 48, const.SCREEN_HEIGHT//2 + 24//2))

line = pg.image.load("png/court_center_btn_pause.png")
line_rect = line.get_rect(center = (const.SCREEN_WIDTH//2, const.SCREEN_HEIGHT//2 - 6//2))
particles = pg.sprite.Group()

class Game:

	def __init__(self):
		self.screen = pg.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))

		self.player = Paddle(1, "png/pud_left.png", 5, 1)
		self.opponent = Paddle(2, "png/pud_right.png", 5, 1)
		self.ball = Ball('png/ball_frames.png', 6, 1)
		self.running = True
		self.clock = pg.time.Clock()

		self.game_area = pg.Rect((0, 0), (970, 560))
		self.game_area.center = self.screen.get_rect().center

	def event_loop(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.running = False

	def collision(self, ball, paddle):
		return ball.rect.colliderect(paddle.rect) 

	def paddle_collisions(self):
		if self.collision(self.ball, self.player):
			self.player.set_is_animated(True)
			self.ball.speed_x *= -1
			particles.add(Particle(self.player.rect.midright[0], self.player.rect.midright[1]))
		elif self.collision(self.ball, self.opponent):
			self.opponent.set_is_animated(True)
			self.ball.speed_x *= -1
			particles.add(Particle(self.opponent.rect.midleft[0], self.opponent.rect.midleft[1]))

	def border_collisions(self):
		if self.ball.horizontal_wall_collision(self.game_area):
			self.ball.speed_y *= -1
			particles.add(Particle(self.ball.rect.centerx, self.ball.rect.centery))
		if self.ball.vertical_wall_collision(self.game_area):
			self.ball.set_ball_at_center()
			if self.ball.speed_x < 0:
				self.opponent.score_up()
			else:
				self.player.score_up()


	def update(self):
	    # Get all the keys currently pressed
		pressed_keys = pg.key.get_pressed()

		self.ball.move()
		self.border_collisions()

		# Paddle logic
		self.paddle_collisions()
		self.player.move(pressed_keys)
		self.player.wall_collision(self.game_area)

		# Opponent logic
		self.opponent.ia_move(self.ball.rect)
		self.opponent.wall_collision(self.game_area)

		# Animation logic
		particles.update()

	def draw(self):
		self.screen.blit(bg, (0, 0))
		self.screen.blit(line, line_rect)
		self.player.draw(self.screen)
		self.opponent.draw(self.screen)
		particles.draw(self.screen)
		self.ball.draw(self.screen)

		self.screen.blit(goals_post_left, goals_post_left_rect)
		self.screen.blit(goals_post_right, goals_post_right_rect)

		self.player.draw_score(self.screen, 15)
		self.opponent.draw_score(self.screen, const.SCREEN_WIDTH - 80)



	def run(self):
	    while self.running:
	        self.event_loop()
	        self.update()
	        self.draw()
	        pg.display.flip()
	        self.clock.tick(60)


if __name__ == '__main__':
	pg.init()
	pg.display.set_caption("Pong")
	game = Game()
	game.run()
	pg.quit()
