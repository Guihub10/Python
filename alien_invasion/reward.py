import pygame
import time
from pygame.sprite import Sprite

class Reward(Sprite):
	def __init__(self, ai_settings, screen, reward_type, rect_x, rect_y):
		super(Reward, self).__init__()
		self.screen = screen
		self.reward_type = reward_type		
		if reward_type == 'L':
			self.image = pygame.image.load('images/L.bmp')
		elif reward_type == 'S':
			self.image = pygame.image.load('images/S.bmp')
		elif reward_type == 'T':
			self.image = pygame.image.load('images/T.bmp')
		elif reward_type == 'G':
			self.image = pygame.image.load('images/G.bmp')
		self.to_draw = self.image
		self.rect = self.image.get_rect()
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		self.rect.centerx = rect_x
		self.rect.centery = rect_y

	def update(self):
		"""move the reward"""
		self.rect.y+=3 
		
		
	def blitme(self):
		self.screen.blit(self.to_draw, self.rect)
