import sys
import pygame
import random
import time

from threading import Thread
from time import sleep
from bullet import Bullet
from alien import Alien
from reward import Reward

def check_keydown_events(event, ai_settings, screen, ship,bullets, stats, sound):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
		ship.moving_left    = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left    = True
		ship.moving_right = False
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets, sound)
	elif event.key == pygame.K_q:
		#store high score
		store_high_score(stats)
		sound.stop = True
		sys.exit()


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
##	if play_button.rect.collidepoint(mouse_x, mouse_y):
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		#reset settings
		ai_settings.initialize_dynamic_settings()
		pygame.mouse.set_visible(False)
		
		stats.reset_stats()
		stats.game_active = True
		#reset game
		
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()
		
		aliens.empty()
		bullets.empty()
		
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		
def check_keyup_events(event, ship, sound):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_SPACE:
		sound.is_shotting = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, sound):
	""" response button press and mouse click """
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#store high score
			store_high_score(stats)
			sound.stop = True
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets, stats, sound)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship, sound)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
		
def update_screen(ai_settings, screen, stats, sb, ship, aliens,bullets, play_button, rewards):
	""" update image on screen, and switch to new screen"""
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()		
	
	ship.blitme()
	aliens.draw(screen)
	if len(rewards) > 0:
		rewards.draw(screen)
	
	sb.show_score()	
	if not stats.game_active:
		play_button.draw_button()
	#set current render visible
	pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb,  ship, aliens, bullets):
	bullets.update()
	
	#Delete the bullets removed
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
			
	check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
	
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
	#Kill the alien who is shotted
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			#stats.temp_score = stats.score
			stats.inc_score = stats.score - stats.temp_score
			sb.prep_score()
		check_high_score(stats, sb)
	if len(aliens) == 0:
		level_up(ai_settings, screen, stats, sb, ship, aliens, bullets)
	
def level_up(ai_settings, screen, stats, sb, ship, aliens, bullets):
	#Create new alien fleet if all of the aliens are destroyed
	bullets.empty()
	ai_settings.increase_speed()
	#increase level
	stats.level += 1
	sb.prep_level()
		
	create_fleet(ai_settings, screen, ship, aliens)
		
def fire_bullet(ai_settings, screen, ship, bullets, sound):
	if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ai_settings, screen, ship)
			bullets.add(new_bullet)
			sound.is_shotting = True

def create_fleet(ai_settings, screen, ship, aliens):
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(ai_settings, alien_width):
	avaliable_space_x = ai_settings.screen_width - 3 * alien_width
	number_aliens_x = int(avaliable_space_x / (2 * alien_width))
	return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
	## Calculate how many aliens could the screen containes.
	avaliable_space_y = (ai_settings.screen_height - (10 * alien_height) - ship_height)
	number_rows = int(avaliable_space_y / (2 * alien_height))
	return number_rows

def check_fleet_edges(ai_settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges() and alien.stop_factor != 0:
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *=  -1

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets, sound):
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
	
	#Game over
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets, sound)
	
	check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets, sound)

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets, sound):
	#lives -1
	stats.ships_left -= 1
	sb.prep_ships()
	if stats.ships_left >0:
		#empty roles
		aliens.empty()
		bullets.empty()
		#flush all
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		#pause
		sound.crash()
		sleep(1.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets, sound):
	
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets, sound)
			break

def check_high_score(stats, sb):
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()

def store_high_score(stats):
	with open ('record.txt','w') as file_object:
		file_object.write(str(stats.high_score))
		

def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper

@async
def play_sound(sound):
	while sound.stop == False:
		if sound.is_shotting:
			sound.shot()
			pygame.time.delay(1000)
	return

def generate_reward(ai_settings, screen, stats):
	if(stats.inc_score >= 1000):
		stats.inc_score = 0
		stats.temp_score = stats.score
		rect_x = random.randint(50, ai_settings.screen_width - 50)
		rect_y = random.randint(50, ai_settings.screen_height * 0.5)
		#S: STOP MOVING, L:LARGE BULLET, L:ADD A LIFE ,T:TEN TIMES SCORE
		reward_type = random.choice('SLGT')
		reward = Reward(ai_settings, screen, reward_type, rect_x, rect_y)
		return reward
	else:
		return 0;

def update_rewards(ai_settings, stats, rewards, ship, screen, aliens, sb):
	reward = generate_reward(ai_settings, screen, stats)
	if reward != 0:
		rewards.add(reward)
	
	if len(rewards) > 0:
		rewards.update()

		for reward in rewards.copy():
			if reward.rect.bottom <= 0:
				rewards.remove(reward)
		#apply rewards			
		check_rewards_ship_collisions(rewards, ship, ai_settings, aliens, stats, sb, screen)

def check_rewards_ship_collisions(rewards, ship, ai_settings, aliens, stats, sb, screen):
	collisions = pygame.sprite.spritecollide(ship, rewards, True)
	if collisions:
		for reward in collisions:
			#for reward in rewards:
			if reward.reward_type == 'G':
				#enlarge bullets
				ai_settings.bullet_width *= 10
				ship.start_time = time.clock()
				
			elif reward.reward_type == 'S':
				#stop alien fleet
				for alien in aliens:
					alien.stop_moving ()
					
			elif reward.reward_type == 'L':
				#add a life
				if sb.stats.ships_left < 3:
					sb.stats.ships_left +=1
					sb.prep_ships()
					
				#score =10000
				else:
					sb.stats.score += 10000
					sb.prep_score()
					if sb.stats.score > sb.stats.high_score:
						sb.prep_high_score()

			elif reward.reward_type == 'T':
					#level up
					sb.stats.level += 1
					sb.prep_level()
					aliens.empty()
					create_fleet(ai_settings, screen, ship, aliens)

