import numpy as np 

class Complex:

	def __init__(self, re, im):
		self.re = re
		self.im = im

	def __str__(self):
		if self.im >= 0:
			return '{} + {}i'.format(self.re, self.im)
		else:
			return '{} - {}i'.format(self.re, -self.im)

	def __add__(self, other):
		return Complex(self.re + other.re, self.im + other.im)

	def __add__(self, other):
		return Complex(self.re + other.re, self.im + other.im)

	def __mul__(self, other):
		return Complex(self.re*other.re - self.im*other.im, self.re*other.im + self.im*other.re)

	def __rmul__(self, other):
		return Complex(other*self.re, other*self.im)

	def __div__(self, other):
		return 1/(other.re**2 + other.im**2)*Complex(self.re*other.re + self.im*other.im, self.im*other.re - self.re*other.im)

	def modulus(self):
		return (self.re**2 + self.im**2)**(1/2)

	def angle(self):
		theta = np.degrees(np.arctan(self.im/self.re))
		if self.re >= 0:
			if theta < 0:
				theta = theta + 360
			return theta
		else:
			return 180 + theta

	def transpose(self):
		self.im = -self.im 

	def cartesian_to_polar(self):
		return self.modulus(), self.angle()


def polar_to_cartesian(r, th):
	rad = np.deg2rad(th)
	return Complex(r*np.cos(rad), r*np.sin(rad))
