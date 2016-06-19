import spidev

class Pos:
	def __init__(self, i=0, j=0):
		self.i = i
		self.j = j

class Color:
	def __init__(self, red = 0, green = 0, blue = 0, brightness = 0):
		self.red = red
		self.green = green
		self.blue = blue
		self.brightness = brightness

class Display:
	def __init__(self, n = 9, m = 13):
		assert n > 0 and m > 0

		self.n = n
		self.m = m
		self.num_leds = self.n*self.m
		self.led_map = [ [ i*self.m + (j if i%2 == 0 else self.m-1-j) for j in range(self.m) ] \
				 for i in range(self.n) ]

		# Init buffer values
		self.ledstart = 0b11100000
		self.leds = [self.ledstart,0,0,0] * self.num_leds

		# Init SPI
		self.spi = spidev.SpiDev()
		self.spi.open(0, 1)
		self.spi.max_speed_hz=8000000

	def setPixel(self, pos, color):
		assert pos.i >= 0 and pos.i < self.n and pos.j >= 0 and pos.j < self.m
		assert color.red >= 0 and color.red < 256 and \
		       color.green >= 0 and color.green < 256 and \
		       color.blue >= 0 and color.blue < 256

		start_index = 4*self.led_map[pos.i][pos.j]
		self.leds[start_index] = (color.brightness & 0b00011111) | 0b11100000
		self.leds[start_index+3] = color.red
		self.leds[start_index+2] = color.green
		self.leds[start_index+1] = color.blue

	def setFrame(self, colors):
		assert len(colors) == self.n and len(colors[0]) == self.m

		for i,color_row in enumerate(colors):
			for j,color in enumerate(color_row):
				self.setPixel(Pos(i,j), color)

	def update(self):
		# Start frame
		self.spi.xfer2([0]*4)

		# Data
		self.spi.xfer2(self.leds)

		# End frame
		for _ in range((self.num_leds + 15) // 16):
			self.spi.xfer2([0x00])

	def clearFrame(self):
		self.setFrame(self.n * [ self.m * [Color()] ])

	def close(self):
		self.clearFrame()
		self.update()
		self.spi.close()
