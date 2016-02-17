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
import difflib

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
			if difflib.SequenceMatcher(None, i, namestring).ratio() > .80:
				self.objname = namestring
	
				return self
		return -1

	def printNode(self):
		print self.module
		print self.name
		print self.objname

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
			ret1 = self.commands.checkValidity(string)
			ret2 = self.objects.checkValidity(string)
			if ret1 != -1:
				return ret1
			if ret2 != -1:
				return ret2

	def printObjs(self):
		for i in self.commands.validarr:
			print "--|-- CMD: --", i
		for x in self.objects.validarr:
			print "--|-- OBJ: --", x

class RootNode(object):
	def __init__(self):
		self.modules = []
		
	def addModule(self, moduleName, cmdarr, objarr):
		newMod = ModuleNode(moduleName)
		for i in cmdarr:
			newMod.addCmd(i)                       #Fills the module node's commands array 
		for j in objarr:			
			newMod.addObj(j)			#Fills the module node's obj array 		
		self.modules.append(newMod)
			
	
	def searchModule(self, moduleName):
		for i in self.modules:
			if i.name == moduleName:
				return i

class Tree(object):

	def __init__(self):
		self.head = RootNode()
	

	def	createTree(self, modulearr):
		modulearr.sort(key = lambda x: x.name)
				
		for i in modulearr:
			self.head.addModule(i.name, i.cmds, i.objs)
					
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
		
		for i in self.head.modules:
			found = i.search(string)
			if found != None:
				break
		found.printNode()

	def printTree(self):
		print "ROOT"
		for i in self.head.modules:
			print "|-", i.name
			i.printObjs()
