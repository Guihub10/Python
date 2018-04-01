import json

class Settings(object):
	""" Store all the configure of Alien Invasion """
	def __init__(self):
		
		self.filename = 'config.json'
		self.settings={}
		with open(self.filename, 'r') as file_object:
			self.settings = json.load(file_object)
		# screen setting
		self.screen_width  = self.get_value('screen_width', 1200)
		self.screen_height = self.get_value('screen_height', 800)
		self.bg_color            = self.get_value('bg_color', (230, 230, 230))
		
		#bullet setting
		self.bullet_width            = self.get_value('bullet_width', 3)
		self.bullet_height          = self.get_value('bullet_height', 15)
		self.bullet_color             = self.get_value('bullet_color', (60, 60, 60))
		self.bullets_allowed      =  self.get_value('bullets_allowed', 10)
		
		#alien setting
		self.fleet_drop_speed =    self.get_value('fleet_drop_speed', 10)
		self.speedup_scale      =    self.get_value('speedup_scale', 1.1)
		self.score_scale             =    self.get_value('score_scale', 1.5)
		#ship setting
		self.ship_limit                =     self.get_value('ship_limit', 3)


		self.start_time = 0
		self.substance_time = 3
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		self.ship_speed_factor =  self.get_value('ship_speed_factor', 1.5)
		self.bullet_speed_factor = self.get_value('bullet_speed_factor', 3)
		self.alien_speed_factor =   self.get_value('alien_speed_factor', 1)
		#fleet_direction: 1(right),-1(left)
		self.fleet_direction          =  self.get_value('fleet_direction', 1)
		
		self.alien_points = self.get_value('alien_points', 50)
	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale 
		self.bullet_speed_factor  *= self.speedup_scale 
		self.alien_speed_factor  *= self.speedup_scale 
		self.alien_points = int(self.score_scale * self.alien_points)

	def get_value(self, key, default_value):
		if key in self.settings.keys():
			return self.settings[key]
		else:
			return default_value
