
import difflib

class ObjectNode(object):
	def __init__(self, typ, module):
		self.module = module
		self.typ = typ
		self.validarr = []	#We could maybe think of new way to create tree. IMO, right now an ObjectNode is carrying too much baggage for its purpose. Ideally, we want the Object node to hold a value for a certian subject or command, as well as its corresponding module. But right now, the objectNode is also carrying a large array of commands or subjects.If we remove the array from the object node and instead create an array of commands and subjects for a moduleNode, we wouldn't have to return a list of large objectNodes with large arrays in searchTree(). That way, each valid command that we find and use in the main will be much lighter. Let me know what you think.    
		self.valueStr = ""

  	def addToArray(self, name):
		self.validarr.append(name)

	def checkValidity(self, namestring):
		for i in self.validarr:
			if difflib.SequenceMatcher(None, i, namestring).ratio() > .80:
				self.valueStr = namestring
	
				return self
		return -1

	def printNode(self):
		print self.module
		print self.typ
		print "Value:", self.valueStr

class ModuleNode(object):
	def __init__(self, name):
		self.name = name
		self.commands = ObjectNode("CMD", name) #Could change this into a list of Object nodes instead of each object node holding an array
		self.subjects = ObjectNode("SBJ", name)
	
	def addCmd(self, cmd_add):
			self.commands.addToArray(cmd_add) #replace addToArray with append 
		
	def addSbj(self, subject_add):
			self.subjects.addToArray(subject_add)#same here

	def search(self, string):
			chk_cmds = self.commands.checkValidity(string) #Would have to do some traversal here but not to big of a deal
			chk_subj = self.subjects.checkValidity(string)
			if chk_cmds != -1:
				return chk_cmds
			if chk_subj != -1:
				return chk_subj

	def printObjs(self):
		for i in self.commands.validarr: #Just traverse through each list instead of each ObjectNode's list
			print "--|-- CMD: --", i
		for x in self.subjects.validarr:
			print "--|-- OBJ: --", x

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
			
	
	def searchModule(self, moduleName): #Do we use this?
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
