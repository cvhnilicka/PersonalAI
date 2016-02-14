# ::: CHANGES ::::
#  
# I was confused why you were importing Resturants and the commands in the addCmd and addObj defs in
# Tree class. 
#
# In createTree() I added cmdArr and objArr parameters that will be the lists we make from parsing our config file.
# I also added the same parameters to addModule() so that we can pass those arrays through and add commands and objects to 
# the module from within the add module function. addObj() and addCmd() then call addToArray() with the correct string values
# from the cmdArr and objArr 
# lists that were passes as parameters earlier.  
#




#import Restaurant

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
		
		def addModule(self, moduleName, cmdarr, objarr): # CHANGED PARAMETERS HERE
			newMod = ModuleNode(moduleName)
			for i in cmdarr:
				addCmd(i)                       #Fills the module node's commands array 
			for j in objarr:			
				addObj(j)			#Fills the module node's obj array 		
			self.modules.append(newMod)
			
	
		def searchModule(self, moduleName):
			for i in self.modules:
				if i.name == moduleName:
					return i

class Tree(object):

	def __init__(self):
		self.head = RootNode

		def	createTree(self, modulearr, cmdarr):
			for i in modulearr:
				self.head.addModule(i)
				

		def addCmds(self, cmdarr):
			for w in cmdarr:
				for i in self.head.modules:
					for x in Restaurant.commands:
						if 	x == w:
							i.addCmd(x)

		def addObjs(self, objarr, objs):
			for w in objarr:
				for i in head.modules:
					for x in ojbs:
						if 	x == w:
							i.addCmd(x)
		

arrb = Restaurant.commands
print(arrb)

