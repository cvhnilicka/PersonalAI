# MAIN METHOD FOR SHIA
#
#
import fileinput
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
	print '\n'
	for i in modules:
		print i.name
		print i.objs
		print i.cmds
		print '\n'		

if __name__ == "__main__": main()
