import Restaurant


class ObjectNode(object):
    def __init__(self, name, module):
		self.module = module
		self.name = name
		self.validarr = []
		self.objname = ""

  
		def addToArray(self, name):
			self.validarr.append(name)

		def checkValidity(self, namestring):
			for i in self.validarr:
				if i == namestring:
					i.ojbname = namestring
					return self



class ModuleNode(object):
	options = ["CMD", "OBJ"]

	def __init__(self, name):
		self.name = name
		self.commands = ObjectNode("CMD", name)
		self.objects = ObjectNode("OBJ", name)
	
		def addCmd(self, cmdtoadd):
			self.commands.addToArray(cmdtoadd)
		
		def addObj(self, objtoadd):
			self.objects.addToArray(objtoadd)


class RootNode(object):
	def __init__(self):
		self.modules = []
		
		def addModule(self, moduleName):
			newMod = ModuleNode(moduleName)
			self.modules.append(newMod)
	
		def searchModule(self, moduleName):
			for i in self.modules:
				if i.name == moduleName:
					return i

class Tree(object):
	
	def	createTree(self, modulearr, cmdarr):
		head = RootNode
		for i in modulearr:
			head.addModule(i)

	def addCmds(head, cmdarr):
		for w in cmdarr:
			for i in head.modules:
				for x in Restaurant.commands:
					if 	x == w:
						i.addCmd(x)

	def addObjs(head, objarr, objs):
		for w in objarr:
			for i in head.modules:
				for x in ojbs:
					if 	x == w:
						i.addCmd(x)

	
arrb = Restaurant.commands
print(arrb)
	
