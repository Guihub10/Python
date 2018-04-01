import pygame
class Sound(object):
	def __init__(self):
		###	pygame.init()
			pygame.mixer.init()
			pygame.time.delay(1000)
			self.shot_channel = pygame.mixer.Channel(2)
			self.shot_sound = pygame.mixer.Sound('sounds/shot.wav')
			
			self.crash_channel = pygame.mixer.Channel(3)
			self.crash_sound = pygame.mixer.Sound('sounds/boom.wav')
			self.is_shotting = False
			self.is_crashing = False
			self.stop = False

	def shot(self):
		if self.shot_channel.get_busy() == False:
                   self.shot_channel.play(self.shot_sound)

	def crash(self):
		if self.crash_channel.get_busy() == False:
                   self.crash_channel.play(self.crash_sound)

 
			
