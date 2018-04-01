import pygame
import time
from pygame.sprite import Sprite

class Ship(Sprite):
	
	def __init__(self, ai_settings, screen):
		super(Ship, self).__init__()
		self.screen = screen
		self.settings = ai_settings
		
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.center = float(self.rect.centerx)
		
		self.moving_right = False
		self.moving_left    = False
		
		self.start_time = 0
		self.substance_time = ai_settings.get_value('reward_substance_time', 5) #reward substance time, it ought to be set from file
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center+=(2 * self.settings.ship_speed_factor)
		if self.moving_left  and self.rect.left > 0:
			self.center-= (2 * self.settings.ship_speed_factor)
		
		self.rect.centerx = self.center
		if time.clock() - self.start_time  > self.substance_time:
			self.settings.bullet_width = self.settings.get_value('bullet_width', 3)

	def center_ship(self):
		self.center = self.screen_rect.centerx
