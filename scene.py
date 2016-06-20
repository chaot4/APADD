import defs

class SceneObject:
	def __init__(self, data, pos = defs.Pos(0,0), brightness_scaling = 1):
		self.data = data
		self.pos = pos
		self.brightness_scaling = brightness_scaling
		self.rotate = 0
		pass

class Scene:
	def __init__(self, n = 9, m = 13):
		self.n = n
		self.m = m
		self.scene_objects = []

	def addObjects(self, scene_objects):
		self.scene_objects += scene_objects

	def removeObject(self, id):
		del self.scene_objects[id]

	def moveObject(self, id, direction):
		pos = self.scene_objects[id].pos
		pos.i += direction[0]
		pos.j += direction[1]

	def moveAllObjects(self, direction):
		for obj in scene_objects:
			pos = obj.pos
			pos.i += direction[0]
			pos.j += direction[1]

	def rotateObject(self, id, amount):
		self.scene_objects[id].rotate = (self.scene_objects[id].rotate + amount)%4

	def render(self):
		colors = self.n * [self.m * [defs.Color()]]

		for obj in self.scene_objects:
			pos = obj.pos
			for i,row in enumerate(obj.data):
				if pos.i+i < 0:
					continue
				if pos.i+i >= self.n:
					break

				for j,color in enumerate(row):
					if pos.j+j < 0:
						continue
					if pos.j+j >= self.m:
						break

					colors[pos.i+i][pos.j+j] = color

		return colors
