


class ObjectNode(object):
    def __init__(self, name, module):
		self.module = module
        self.name = name
        self.validarr = []
		self.objname = ""

  
	def addToArray(self, name):
		self.validarr.append(name)

	def checkValidity(self, namestring ):
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



class Tree(object):
	
	def	createTree(self, modulearr, objarr, cmdarr):
		head = RootNode
		for i in modulearr:
			for o in objarr:
				

		
