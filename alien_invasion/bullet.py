import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class which is used to manage the bullet set off from the ship"""
	def __init__(self, ai_settings, screen, ship):
		"""Create a bullet at the position of the ship"""
		super(Bullet, self).__init__()
		self.screen = screen
		
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		self.y = float(self.rect.y)
		
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		"""move the bullet towads top"""
		
		self.y-= self.speed_factor
		self.rect.y = self.y
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
		