# MAIN METHOD FOR SHIA
#
#
import fileinput
import db
import readline

class MOD(object):
	def __init__(self, name):
		self.name = name
		self.objs = []
		self.cmds = []


def main():
	#Array of MOD Objects
	modules = []
	#modName holds the module current module being read in from config file
	modName = ""        
	for line in fileinput.input("Config.txt"):
		#Modules
		line = line.lower()
		if line[0] == '%':	 
			modName = line[1:]
			newMod = MOD(modName)
			modules.append(newMod)
		#Commands
		if line[0] == '$':
			indx = modules.index(newMod)
			modules[indx].cmds.append(line[1:])
		#Objects
		if line[0] == '#':
			indx = modules.index(newMod)
			modules[indx].objs.append(line[1:])
				
	#
	# Just for seeing the output sorted modules and their corresponding commands and objects
	# We may have to cut the new line characters out in each obj and cmd list but not sure if that is needed yet
	#

	tree = db.Tree()

	tree.createTree(modules)
	tree.printTree()
	loop = True
	while loop:
		cmds = userInput(tree)
		cross = validate(cmds)
		for x in cross:
			x.printNode()
			for k in cross[x]:
				k.printNode()

def userInput(tree):
	cmd = raw_input()
	cmd = cmd.split(" ")
	valid_cmds = []
	for i in cmd:
		found = tree.searchTree(i)
		if found != None:
			valid_cmds.append(found)
	return valid_cmds



def validate(arr):
	cmds = []
	objs = []
	valid = {}
	for i in arr:
		if i.name == "CMD":
			cmds.append(i)
		elif i.name == "OBJ":
			objs.append(i)
	for x in objs:
		for j in cmds:
			a = []
			if x.module == j.module:
				
				a.append(j)
		valid[x] = a

	return valid
		
			


		


if __name__ == "__main__": main()
