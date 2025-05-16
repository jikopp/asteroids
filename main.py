# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from asteroidfield import *
from player import Player
from asteroid import Asteroid

def main():
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
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
		for obj in asteroids:
			if player.collision(obj):
				print("Game over!")
				pygame.quit()
				exit()
		for obj in drawable:
			obj.draw(screen)
		pygame.display.flip()

if __name__ == "__main__":
	main()