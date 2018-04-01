import sys
import pygame

from setting import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from sound import Sound
import game_functions as gf

def run_game():
	#Initialize the game and create a window!#
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	play_button = Button(ai_settings, screen, "Play")
	
	#Setup a game stats
	game_stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, game_stats)

	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	rewards = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens)
	#sound
	#pygame.mixer.init()
	sound = Sound()
	gf.play_sound(sound)
    #render cycle
	while True:
		gf.check_events(ai_settings, screen, game_stats, sb,  play_button, ship, aliens, bullets, sound, rewards)
		
		if game_stats.game_active:
			ship.update()
			gf.update_rewards(ai_settings, game_stats, rewards, ship, screen, aliens, sb)
			gf.update_bullets(ai_settings, screen, game_stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, game_stats, screen, sb, ship, aliens, bullets, sound)

		gf.update_screen(ai_settings, screen, game_stats, sb, ship, aliens, bullets, play_button, rewards)

run_game()

