class world:
	def __init__(self, win, objs):
		self.win = win
		self.objs = objs
		
	def update(self):
		for obj in self.objs:
			obj.update()

	def draw(self):
		for obj in self.objs:
			obj.draw(self.win)

class object:
	def __init__(self, shape, type="free"):
		self.shape = shape
		self.type = type

	def update(self):
		if self.type == "free":
			self.shape.update()
		if self.type == "static":
			pass

	def draw(self, win):
		self.shape.draw(win)


class circle:
	def __init__(self, 
							 pos, 
							 r, 
							 color, 
							 origin=None, 
							 rad=None):
		self.pos = pos
		self.r = r
		self.color = color
		self.origin = origin
		self.rad = rad

	def update(self):
		if self.origin:
			self.pos = self.origin()
		if self.rad:
			self.r = self.rad()

	def draw(self, win):
		win.draw_circle(self.color, self.pos, self.r, False)


class rect:
	def __init__(self,
							p1,
							p2,
							color,
							p1_or=None,
							p2_or=None):
		self.p1 = p1
		self.p2 = p2
		self.color = color
		self.p1_or = p1_or
		self.p2_or = p2_or

	def update(self):
		if self.p1_or:
			self.p1 = self.p1_or()
		if self.p2_or:
			self.p2 = self.p2_or()

	def draw(self, win):
		win.draw_rect(self.color, (self.p1,self.p2), True)