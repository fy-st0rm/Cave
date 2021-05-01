
class Collision:
	def __init__(self, obj):
		self.obj = obj

	def return_hit_list(self, rect1, rect2):
		hit_list = []

		for i in rect2:
			if rect1.colliderect(i):
				hit_list.append(i)

		return hit_list

	"""
	def implement_collision(self):
		if self.collision_type["DOWN"]:
			self.obj.airtime = 0
			self.obj.vertical_movement = 0
		else:
			self.obj.airtime += self.gravity
	"""

	def calculate_collision(self, collision_rect):
		self.rect = self.obj.rect
		self.movement = self.obj.movement

		# Collision type dictionary
		self.collision_type = {"LEFT": False, "RIGHT": False, "UP": False, "DOWN": False}

		# Moving player in X-axis
		self.rect.x += self.movement[0]

		# Gathering the collided objects when moving in X-Axis
		hit_list = self.return_hit_list(self.rect, collision_rect)
		
		# Actual collision system
		for hit in hit_list:
			if self.movement[0] > 0:
				self.rect.right = hit.left
				self.collision_type["RIGHT"] = True
			if self.movement[0] < 0:
				self.rect.left = hit.right
				self.collision_type["LEFT"] = True

		# Moving player in Y-axis
		self.rect.y += self.movement[1]

		# Gathering the collided objects when moving in Y-Axis
		hit_list = self.return_hit_list(self.rect, collision_rect)
		
		# Actual collision system
		for hit in hit_list:
			if self.movement[1] > 0:
				self.rect.bottom = hit.top
				self.collision_type["DOWN"] = True
			if self.movement[1] < 0:
				self.rect.top = hit.bottom
				self.collision_type["TOP"] = True
