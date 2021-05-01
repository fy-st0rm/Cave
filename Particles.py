import pygame, sys, random

class Particles(object):
	
	def __init__(self, Display_size, color, display):
		
		#[Location, Velocity, time]
		self.Particles = []
		self.Display_size = Display_size
		self.x = Display_size[0]/2
		self.y = Display_size[1]/2
		self.color = color
		self.display = display


	def render(self):
		self.Particles.append([[self.x,self.y],[random.randint(0,20)/10 - 1, -2], random.randint(1,2)])

		for Particle in self.Particles:

			# Particle Properties
			Particle[0][0] += Particle[1][0]
			Particle[0][1] += Particle[1][1]
			Particle[2] -= 0.1
			Particle[1][1] += 1

			# Draws Circle as Particles
			pygame.draw.circle(self.display, self.color, [int(Particle[0][0]), int(Particle[0][1])],Particle[2])
			if Particle[2] <= 0:
				self.Particles.remove(Particle) # Removes Particles
				



























# FUNK U ;3