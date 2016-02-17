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
	def __init__(self, name):
		self.name = name
		self.commands = ObjectNode("CMD", name)
		self.objects = ObjectNode("OBJ", name)
	
	def addCmd(self, cmdtoadd):
			self.commands.addToArray(cmdtoadd)
		
	def addObj(self, objtoadd):
			self.objects.addToArray(objtoadd)

	def search(self, string):
			self.commands.checkValidity(string)
			self.objects.checkValidity(string)

class RootNode(object):
	def __init__(self):
		self.modules = ["a", "b", "x", "z"]
		
		def addModule(self, moduleName, cmdarr, objarr):
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
		self.head = RootNode()
		print(self.head.modules)

		def	createTree(self, modulearr, cmdarr, objarr):
			modulearr.sort()
				
			for i in modulearr:
				self.head.addModule(i, cmdarr, objarr)
					
	def searchTree(self, string):
		string.lower()
 		firstChar = string[:1]
		charAscii = ord(firstChar)
		modules_to_search = []
		if 110 <= charAscii < 123:
			modules_to_search = self.head.modules[len(self.head.modules)/2:]
		elif 97 <= charAscii < 110:
			modules_to_search = self.head.modules[:len(self.head.modules)/2]
		else:
			print("not a valid string")
		for i in modules_to_search:
			i.search(string)
		print(modules_to_search)
a = Tree()
a.searchTree("r")
