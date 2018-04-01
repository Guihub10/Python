import json

filename = 'config.json'
settings ={
  'screen_width':1200, 'screen_height':700, 'bg_color':(230, 230, 230), 
  'bullet_width':3, 'bullet_height':15, 'bullet_color':(60, 60, 60),
  'bullets_allowed':10, 'fleet_drop_speed' :15, 'speedup_scale':1.2,
  'score_scale':1.5, 'ship_limit':3, 'ship_speed_factor':1.5,
  'bullet_speed_factor':3, 'alien_speed_factor':1,'fleet_direction':1,
  'alien_points':50, 'reward_substance_time':5
}

with open(filename, 'w') as file_object:
	json.dump(settings, file_object)

