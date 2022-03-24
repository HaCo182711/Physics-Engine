import PyGUIgame.PyGUIgame as pgg
import PhysicsEngine as phe

win = pgg.init(256,256,"Physics stuff")


ball = phe.circle((0,0), 10, pgg.RED, origin=win.getMousePos)

world = phe.world(win, [ball])

run = True
while run:
	win.update()
	world.update()
	world.draw()

	if win.isKeyDown("Escape"):
		run = False