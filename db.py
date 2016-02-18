
import difflib

class ObjectNode(object):
	def __init__(self, typ, module, value):
		self.module = module
		self.typ = typ
		self.validarr = []	#We could maybe think of new way to create tree. IMO, right now an ObjectNode is carrying too much baggage for its purpose. Ideally, we want the Object node to hold a value for a certian subject or command, as well as its corresponding module. But right now, the objectNode is also carrying a large array of commands or subjects.If we remove the array from the object node and instead create an array of commands and subjects for a moduleNode, we wouldn't have to return a list of large objectNodes with large arrays in searchTree(). That way, each valid command that we find and use in the main will be much lighter. Let me know what you think.    
		self.valueStr = value


	def printNode(self):
		print self.module
		print self.typ
		print "Value:", self.valueStr

class ModuleNode(object):
	def __init__(self, name):
		self.name = name
		self.commands = [] #Could change this into a list of Object nodes instead of each object node holding an array
		self.subjects = []
		###### CHANGED #############
	def addCmd(self, cmd_add):
		newN = ObjectNode("CMD", self.name, cmd_add)	
		self.commands.append(newN) #replace addToArray with append 
		######### CHANGED ################	
	def addSbj(self, subject_add):
		newN = ObjectNode("OBJ", self.name, subject_add)	
		self.subjects.append(newN)#same here
		########### CHANGED ###############
	def search(self, string):
			for i in self.commands:
				if i.valueStr == string:
					return i
			for j in self.subjects:
				if j.valueStr == string:
					return j

	def printObjs(self):
		for i in self.commands: 
			print "--|-- CMD: --"
			i.printNode()
		for x in self.subjects:
			print "--|-- OBJ: --"
			x.printNode()

class RootNode(object):
	def __init__(self):
		self.modules = []
		
	def addModule(self, moduleName, cmdarr, objarr):
		newMod = ModuleNode(moduleName)
		for i in cmdarr:
			newMod.addCmd(i)                       #Fills the module node's commands array 
		for j in objarr:			
			newMod.addSbj(j)			#Fills the module node's obj array 		
		self.modules.append(newMod)
			
	
	def searchModule(self, moduleName): #Do we use this?   # not right now but im sure we will have to in the future....
		for i in self.modules:
			if i.name == moduleName:
				return i

class Tree(object):

	def __init__(self):
		self.head = RootNode()
	

	def createTree(self, modulearr):
		modulearr.sort(key = lambda x: x.name)
		
		for i in modulearr:
			self.head.addModule(i.name, i.cmds, i.subjs)
					
	def searchTree(self, string):
		string.lower()		

		for i in self.head.modules:
			found = i.search(string)
			if found != None:
				break
		return found		
 
	def printTree(self):
		print "ROOT"
		for i in self.head.modules:
			print "|-", i.name
			i.printObjs()
