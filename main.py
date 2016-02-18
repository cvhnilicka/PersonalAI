# MAIN METHOD FOR SHIA
#
#
import fileinput
import db
import readline

class MOD(object):
	def __init__(self, name):
		self.name = name
		self.subjs = []
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
			modName = line[1:].rstrip('\n')
			newMod = MOD(modName)
			modules.append(newMod)
		#Commands
		if line[0] == '$':
			indx = modules.index(newMod)
			modules[indx].cmds.append(line[1:])
		#Objects
		if line[0] == '#':
			indx = modules.index(newMod)
			modules[indx].subjs.append(line[1:])
				
	#Database creation from config
	tree = db.Tree()
	tree.createTree(modules)
	tree.printTree()
	
	#Main program flow -- Module executions will be called in here 
	while True:
		cmds = userInput(tree)
		crossRef = crossReference(cmds)
		#TESTING
		for x in crossRef:
			print "Subject: ", x.printNode()
			for k in crossRef[x]:
				print "Command: ", k.printNode()
		#END TESTING
		#CREATE EXECUTION HERE??
		#

#
# Recognize user input against DB Values
#  
def userInput(tree):
	user_cmd = raw_input()
	user_cmd = user_cmd.split(" ")
	valid_cmds = []
	for i in user_cmd:
		found = tree.searchTree(i)
		if found != None:
			valid_cmds.append(found)
	return valid_cmds

#
# Match valid subjects with their commands
# Form an execution  
#
def crossReference(valid_input):
	cmds = []
	subjs = []
	execute = {}
	#Sort valid input into subj/cmd
	for i in valid_input:
		if i.typ == "SBJ":
			cmds.append(i)
		elif i.typ == "CMD":
			subjs.append(i)
	#Cross Reference
	for x in subjs:
		for j in cmds:
			a = []
			if j.module == x.module:
				a.append(j)
		execute[x] = a
	
	return execute	
		

if __name__ == "__main__": main()
