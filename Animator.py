import pygame
import numpy as np


# Flips a single image
def flip(img, horizontal, vertical):
	return pygame.transform.flip(img, horizontal, vertical)


# Flips a list of images
def flip_list(lst, horizontal, vertical):
	new_lst = []
	for i in lst:
		new_lst.append(flip(i, horizontal, vertical))
	return new_lst


class Animator:
	def load_image(self, images, speed):
		length = len(images)
		speed = speed/10
		data_base = []

		for i in np.arange(0, length, speed):
			data_base.append(images[int(i)])

		return data_base

	def change_state(self, current_state, new_state, frame):
		if current_state != new_state:
			current_state = new_state
			frame = 0
		return current_state, frame



