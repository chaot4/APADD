import defs

class SceneObject:
	def __init__(self, data, pos = defs.Pos(0,0), brightness_scaling = 1):
		self.data = data
		self.pos = pos
		self.brightness_scaling = brightness_scaling
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

	def render(self):
		colors = self.n * [self.m * [defs.Color()]]

		for obj in self.scene_objects:
			pos = obj.pos
			data = obj.data

			min_i = max(0, pos.i)
			max_i = min(self.n, pos.i+len(data))
			for i in range(min_i, max_i):
				row = data[i-pos.i]
				min_j = max(0, pos.j)
				max_j = min(self.m, pos.j+len(row))
				for j in range(min_j, max_j):
					color = row[j-pos.j]
					colors[i][j] = color

		return colors
