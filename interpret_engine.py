from __future__ import print_function
import readline
import json
import difflib


#User Input vs Accepted objects(keys)
#Returns array of Input words that match certain keys
def interpret1( arr1, arr2):
	print(arr1) #INPUT	
	print(arr2) #Keys
	resp = []
	for i in arr1:
		for x in arr2:
			diff = difflib.SequenceMatcher(None, i, x).ratio()
			#print(diff)
			if difflib.SequenceMatcher(None, i, x).ratio() > .85:
				resp.append(x)	
	return resp


#Global Commands vs Accepted Input 
def interpret2(arr1, arr2):
	arr3 = interpret1(arr1, arr2)
	set1 = set(arr3)
	set2 = set(arr2)
	set3 = set.intersection(set1, set2)
	return list(set3)

inputs = ["subway", "hour", "butter", "pen", "temp", "ratings"]
subject = ["subway", "Tony's bistro", "Pizza"]                   #objects 
cmds  = ["hour", "rating", "temp"]				 #all accepted commands



subjects = interpret2(inputs, subject)
commands = interpret2(inputs, cmds)
print(subjects)
print(commands)


