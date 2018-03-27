class Settings(object):
	""" Store all the configure of Alien Invasion """
	def __init__(self):
		
		# screen setting
		self.screen_width     = 1200
		self.screen_height =   700
		self.bg_color            = (230, 230, 230)
		self.ship_speed_factor = 1
		
		#bullet setting
		self.bullet_speed_factor = 1
		self.bullet_width               = 3
		self.bullet_height           = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed =       10
		
		#alien setting
		self.alien_speed_factor = 1
		self.fleet_drop_speed =    50
		#fleet_direction: 1(right),-1(left)
		self.fleet_direction         = 1
		
		#ship setting
		self.ship_limit = 3
		
		
