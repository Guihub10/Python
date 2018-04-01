import pygame
import time
from pygame.sprite import Sprite 

class Alien(Sprite):
	
	def __init__(self, ai_settings, screen):
		
		super(Alien,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		self.x = float(self.rect.x)
		
		self.start_time = 0
		self.substance_time = ai_settings.get_value('reward_substance_time', 5)
		self.stop_factor = 1
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""move alien to right"""
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction * self.stop_factor)
		self.rect.x = self.x
		
		if time.clock() - self.start_time  > self.substance_time:
			self.stop_factor = 1
			
	def stop_moving(self):
		self.stop_factor = 0
		self.start_time = time.clock()
		
	def check_edges(self):
		"""return true when touching edges"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True
	
#	def set_start_time(start_time):
#		self.start_time = start_time
		
 
