import pygame, sys, random



def generate_particles(amt, pos):
	particles = []
	for i in range(amt):
		particles.append([[pos[0], pos[1]],[random.randint(0,20)/10 - 1, -2], random.randint(3,6)])
	return particles


def render_particles(surface, particles, scroll):
	for Particle in particles:
		# Particle Properties
		Particle[0][0] += Particle[1][0]
		Particle[0][1] += Particle[1][1]
		Particle[2] -= 0.1
		Particle[1][1] += .1

		# Draws Circle as Particles
		pygame.draw.circle(surface, pygame.Color("white"), [int(Particle[0][0]-scroll[0]), int(Particle[0][1]-scroll[1])], int(Particle[2]))
		if Particle[2] <= 0:
			particles.remove(Particle) # Removes Particles


class Particles(object):
	
	def __init__(self, surface, color):
		self.surface = surface
		self.color = color

		#[Location, Velocity, time]
		self.Particles = []

	def generate(self, pos, amt):
		self.Particles = []
		for i in range(amt):
			self.Particles.append([[pos[0], pos[1]],[random.randint(0,20)/10 - 1, -2], random.randint(3,6)])

	def render(self):
		for Particle in self.Particles:
			# Particle Properties
			Particle[0][0] += Particle[1][0]
			Particle[0][1] += Particle[1][1]
			Particle[2] -= 0.1
			#Particle[1][1] += 1

			# Draws Circle as Particles
			pygame.draw.circle(self.surface, self.color, [int(Particle[0][0]), int(Particle[0][1])], int(Particle[2]))
			if Particle[2] <= 0:
				self.Particles.remove(Particle) # Removes Particles
