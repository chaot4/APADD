#import dummy_display as display
import display
import defs
import scene
import time

d = display.Display()
n = defs.Color()
r = defs.Color(200, 0, 0, 20)
g = defs.Color(0, 200, 0, 20)
b = defs.Color(0, 0, 200, 20)

#for _ in range(10):
#	d.clearFrame()
#	d.setPixel(display.Pos(0,2), r)
#	d.setPixel(display.Pos(1,1), g)
#	d.setPixel(display.Pos(2,0), b)
#	d.update()
#	time.sleep(1)
#
#	colors = [ \
#	[ r, r, r, r, r, r, r, r, r, r, r, r, r ], \
#	[ r, g, g, g, g, g, g, g, g, g, g, g, r ], \
#	[ r, g, b, b, b, b, b, b, b, b, b, g, r ], \
#	[ r, g, b, n, n, n, n, n, n, n, b, g, r ], \
#	[ r, g, b, n, n, n, n, n, n, n, b, g, r ], \
#	[ r, g, b, n, n, n, n, n, n, n, b, g, r ], \
#	[ r, g, b, b, b, b, b, b, b, b, b, g, r ], \
#	[ r, g, g, g, g, g, g, g, g, g, g, g, r ], \
#	[ r, r, r, r, r, r, r, r, r, r, r, r, r ], \
#	]
#	d.setFrame(colors)
#	d.update()
#	time.sleep(1)
#
#	colors = [ \
#	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
#	[ r, r, r, n, n, n, n, n, n, n, n, n, n ], \
#	[ r, n, n, n, n, n, n, n, n, n, n, n, n ], \
#	[ r, n, n, n, n, r, n, n, n, n, n, n, r ], \
#	[ r, r, r, n, r, r, r, n, r, r, r, n, n ], \
#	[ n, n, r, n, n, r, n, n, r, n, r, n, r ], \
#	[ n, n, r, n, n, r, n, n, r, n, r, n, r ], \
#	[ r, r, r, n, n, r, n, n, r, r, r, n, r ], \
#	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
#	]
#	d.setFrame(colors)
#	d.update()
#	time.sleep(1)
#
#	colors = [ \
#	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
#	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
#	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
#	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
#	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
#	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
#	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
#	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
#	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
#	]
#	for i in range(39):
#		colors[0][(i-1)%13] = n
#		colors[0][i%13] = r
#		d.setFrame(colors)
#		d.update()
#		time.sleep(0.05)

d.clearFrame()
s = scene.Scene()
data = [ \
[ r, n, r], \
[ n, r, n], \
[ r, n, r] ]
obj = scene.SceneObject(data, defs.Pos(2,2))
s.addObjects([obj])
d.setFrame(s.render())
d.update()
time.sleep(1)
s.moveObject(0, (2,2))
d.setFrame(s.render())
d.update()
time.sleep(1)

d.close()
