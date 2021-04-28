import pygame
import os
import noise
import random

from SpriteSheet import *

class Map:
	def __init__(self, surface):
		self.surface = surface

		# Sprites
		self.sprites = spritesheet(os.path.join("res/Sprites/tiles.png"))
		self.tile_size = 16
		self.tiles = {
			"grass": self.sprites.load_image(0, 0, self.tile_size, self.tile_size),
			"water": self.sprites.load_image(1, 0, self.tile_size, self.tile_size)
		}

		# gen stuff
		self.chunk_size = 8
		self.game_map = {}


	def __generate_chunk(self, x, y):

		# It generates a random chunk

		chunkData = []

		for yPos in range(self.chunk_size):
			for xPos in range(self.chunk_size):
				targetX = x * self.chunk_size + xPos
				targetY = y * self.chunk_size + yPos

				self.tileType = None
				height = int(noise.pnoise2((targetX+random.randint(1, 2)) * .1, (targetY+random.randint(1, 2)) * .1, octaves=5, repeatx=9999999, repeaty=9999999)*5)

				if 7 < 8 - height <= 8:
					self.tileType = "grass"
				else:
					self.tileType = "water"

				if self.tileType is not None:
					chunkData.append([[targetX, targetY], self.tileType])

		return chunkData


	def generate_terrain(self, collision_rect, scroll):
		for y in range(5):
			for x in range(5):
				target_x = x - 1 + int(round(scroll[0] / (self.chunk_size * self.tile_size)))
				target_y = y - 1 + int(round(scroll[1] / (self.chunk_size * self.tile_size)))
				target_chunk = str(target_x) + ';' + str(target_y)

				if target_chunk not in self.game_map:
					self.game_map[target_chunk] = self.__generate_chunk(target_x, target_y)


				# Displays the tiles
				for tile in self.game_map[target_chunk]:
					self.surface.blit(self.tiles[tile[1]], (tile[0][0] * self.tile_size - scroll[0],
					                                        tile[0][1] * self.tile_size - scroll[1]))

					if tile[1] in [0, 1]:
						collision_rect.append(pygame.Rect(tile[0][0] * self.tile_size, tile[0][1] * self.tile_size,
						                                  self.tile_size, self.tile_size))


