import dummy_display as display
import time

d = display.Display()
n = display.Color()
r = display.Color(200, 0, 0, 20)
g = display.Color(0, 200, 0, 20)
b = display.Color(0, 0, 200, 20)

for _ in range(10):
	d.clearFrame()
	d.setPixel(display.Pos(0,2), r)
	d.setPixel(display.Pos(1,1), g)
	d.setPixel(display.Pos(2,0), b)
	d.update()
	time.sleep(1)

	colors = [ \
	[ r, r, r, r, r, r, r, r, r, r, r, r, r ], \
	[ r, g, g, g, g, g, g, g, g, g, g, g, r ], \
	[ r, g, b, b, b, b, b, b, b, b, b, g, r ], \
	[ r, g, b, n, n, n, n, n, n, n, b, g, r ], \
	[ r, g, b, n, n, n, n, n, n, n, b, g, r ], \
	[ r, g, b, n, n, n, n, n, n, n, b, g, r ], \
	[ r, g, b, b, b, b, b, b, b, b, b, g, r ], \
	[ r, g, g, g, g, g, g, g, g, g, g, g, r ], \
	[ r, r, r, r, r, r, r, r, r, r, r, r, r ], \
	]
	d.setFrame(colors)
	d.update()
	time.sleep(1)

	colors = [ \
	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
	[ r, r, r, n, n, n, n, n, n, n, n, n, n ], \
	[ r, n, n, n, n, n, n, n, n, n, n, n, n ], \
	[ r, n, n, n, n, r, n, n, n, n, n, n, r ], \
	[ r, r, r, n, r, r, r, n, r, r, r, n, n ], \
	[ n, n, r, n, n, r, n, n, r, n, r, n, r ], \
	[ n, n, r, n, n, r, n, n, r, n, r, n, r ], \
	[ r, r, r, n, n, r, n, n, r, r, r, n, r ], \
	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
	]
	d.setFrame(colors)
	d.update()
	time.sleep(1)

	colors = [ \
	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
	[ n, n, n, n, n, n, n, n, n, n, n, n, n ], \
	]
	for i in range(39):
		colors[0][(i-1)%13] = n
		colors[0][i%13] = r
		d.setFrame(colors)
		d.update()
		time.sleep(0.05)

d.close()
