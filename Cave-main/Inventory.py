import os
import pygame



class Inventory:
	def __init__(self, surface, font, x, y):
		self.surface = surface
		self.font = font

		# Pos
		self.x = x
		self.y = y
		
		# Inventory stuff
		self.inventory_img = pygame.image.load(os.path.join("res/UI/ui_inventorybg.png"))#Image name
		self.invent_size = 50

		# Inventory Title
		self.ui_title_invt = self.font.render('Inventory',True, (0, 0, 0)) 

		# Inventory Subtitle
		self.ui_item_invt = self.font.render('Items',True, (0, 0, 0))

		# Inventory toggle button
		self.toggle = False

	def event(self, e):
		# Inventory event system

		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_e:
				if self.toggle:
					self.toggle = False
				else:
					self.toggle = True

	def __ui_instruction(self):
		ui_control = self.font.render('Inventory [E]',True, (225, 225, 225)) 
		self.surface.blit(ui_control,(10,150))#Displays Control to open inventory

	def draw(self):
		# Inventory renderer system
		if self.toggle:
			#Draws Inventory Back Ground
			self.surface.blit(pygame.transform.scale(self.inventory_img, (self.invent_size*4,self.invent_size*3)), (self.x, self.y))

			# Draws Title 
			self.surface.blit(self.ui_title_invt, (self.x + 50 , self.y + 20))# Connected to the background image

			#Draw Sub Title
			self.surface.blit(self.ui_item_invt, (self.x + 50 , self.y + 40))# Connected to the background image
		else:
			self.__ui_instruction()

