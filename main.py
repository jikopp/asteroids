# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from asteroidfield import *
from player import Player
from asteroid import Asteroid
from shot import Shot


def main():

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots)

	pygame.init()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	field = AsteroidField()
	while True:
		screen.fill("black")		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		dt = clock.tick(60)/1000
		updatable.update(dt)
		shots.update(dt)
		for shot in shots:
			shot.draw(screen)
		for asteroid in asteroids:
			if player.collision(asteroid):
				print("Game over!")
				pygame.quit()
				exit()
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collision(shot):
					asteroid.split()
					shot.kill()
		for obj in drawable:
			obj.draw(screen)
		pygame.display.flip()

if __name__ == "__main__":
	main()