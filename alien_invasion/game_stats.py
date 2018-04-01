import os
class GameStats(object):
	"""trace the information"""
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False
		if os.path.isfile("record.txt"):
			with open('record.txt', 'r') as file_object:
				high_score = file_object.read()
				if high_score: 
					self.high_score = int(high_score)
				else:
					self.high_score = 0
		else:
			self.high_score = 0

		self.level = 1
		self.inc_score = 0
		self.temp_score = 0
	def reset_stats(self):
		#lives
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.inc_score = 0
		self.temp_score = 0
		
		
		
