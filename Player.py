import pygame
import os
import random

from SpriteSheet import *
from Animator import *
from Collision import *
from Particles import *


class Player:
	def __init__(self, surface, rect):
		self.surface = surface
		self.rect = rect

		self.player_sprite = spritesheet(os.path.join("res/Sprites/player.png"))
		self.animator = Animator()

		# Player animation tree
		self.images = {
			"idle": {
				"right":  [self.player_sprite.load_image(4, 0, self.rect.w, self.rect.h)],
				"left" :  [flip(self.player_sprite.load_image(4, 0, self.rect.w, self.rect.h), True, False)],
				"up"   :  [self.player_sprite.load_image(2, 0, self.rect.w, self.rect.h)],
				"down" :  [self.player_sprite.load_image(0, 0, self.rect.w, self.rect.h)]
			},
			"walk" : {
				"right":  self.animator.load_image(self.player_sprite.load_strip([64, 0, self.rect.w, self.rect.h], 2), 1),
				"left" :  self.animator.load_image(flip_list(self.player_sprite.load_strip([64, 0, self.rect.w, self.rect.h], 2), True, False), 1),
				"up"   :  self.animator.load_image(flip_list(self.player_sprite.load_strip([32, 0, self.rect.w, self.rect.h], 2), True, False), 1),
				"down" :  self.animator.load_image(flip_list(self.player_sprite.load_strip([0, 0, self.rect.w, self.rect.h], 2), True, False), 1)	
			}
		}

		# animation stuff
		self.left = False
		self.right = False
		self.up = False
		self.down = False

		self.state = "walk"
		self.side = "right"
		self.frame = 0

		# Movements
		self.speed = 2

		# Colors
		self.shirt = (129, 129, 129) # or whatever yellow color you want
		self.pant = (68, 68, 68)
		self.threshold = (10, 10, 10) # or whatever threshold works
		
		self.new_shirt = pygame.Color("cyan")
		self.new_pant = pygame.Color("brown")

		# Collision stuff
		self.collision = Collision(self)


		self.particles = []

	def event(self, e):
		# Player event stuff here:

		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_a:
				self.left = True
			if e.key == pygame.K_d:
				self.right = True
			if e.key == pygame.K_w:
				self.up = True
			if e.key == pygame.K_s:
				self.down = True

		if e.type == pygame.KEYUP:
			if e.key == pygame.K_a:
				self.left = False
			if e.key == pygame.K_d:
				self.right = False
			if e.key == pygame.K_w:
				self.up = False
			if e.key == pygame.K_s:
				self.down = False

	def __break(self, collision_rect, game_map):
		
		if pygame.mouse.get_pressed()[0]:

			# Checking the side and guessing the block position
			if self.side == "right":
				tile = pygame.Rect(self.rect.x+16, self.rect.y, 16, 16)
			elif self.side == "left":
				tile = pygame.Rect(self.rect.x-16, self.rect.y, 16, 16)
			elif self.side == "up":
				tile = pygame.Rect(self.rect.x, self.rect.y-16, 16, 16)
			elif self.side == "down":
				tile = pygame.Rect(self.rect.x, self.rect.y+16, 16, 16)

			# Checking if that block is a collidable block
			for rect in collision_rect:
				if tile == rect[0]:

					# If yes getting its corrd and index of game map
					coord = rect[1]
					index = rect[2]

					# Changing the value of wall to floor
					game_map[coord][index][1] = "floor"

					self.particles = generate_particles(10, (tile.x, tile.y))

	def draw(self, scroll, collision_rect, game_map):
		# Player rendering stuff

		# Player movement lst
		self.movement = [0, 0]

		if self.left:
			self.state = "walk"
			self.side = "left"
			self.movement[0] -= self.speed

		if self.right:
			self.state = "walk"
			self.side = "right"
			self.movement[0] += self.speed

		if self.up:
			self.state = "walk"
			self.side = "up"
			self.movement[1] -= self.speed

		if self.down:
			self.state = "walk"
			self.side = "down"
			self.movement[1] += self.speed

		if not self.left and not self.right and not self.up and not self.down:
			self.state = "idle"

		image = self.images[self.state][self.side]

		# Increasing the frames
		self.frame += 1
		if self.frame >= len(image):
			self.frame = 0

		final_image = image[self.frame]

		# Changing the color
		pygame.transform.threshold(final_image, final_image, self.shirt, self.threshold, self.new_shirt, 1, None, True)
		pygame.transform.threshold(final_image, final_image, self.pant, self.threshold, self.new_pant, 1, None, True)


		# For breaking blocks
		self.__break(collision_rect, game_map)

		# Calculating collisions
		self.collision.calculate_collision(collision_rect)

		render_particles(self.surface, self.particles, scroll)

		self.surface.blit(final_image, (self.rect.x-scroll[0], self.rect.y-scroll[1]))

