from __future__ import print_function
import readline
import json
import difflib



def interpret1( arr1, arr2):
	print(arr1)
	print(arr2)
	resp = []
	for i in arr1:
		for x in arr2:
			diff = difflib.SequenceMatcher(None, i, x).ratio()
			print(diff)
			if difflib.SequenceMatcher(None, i, x).ratio() > .85:
				resp.append(x)	
	return resp


def interpret2(arr1, arr2):
	arr3 = interpret1(arr1, arr2)
	set1 = set(arr3)
	set2 = set(arr2)
	set3 = set.intersection(set1, set2)
	return list(set3)

inputs = ["subway", "hour", "butter", "pen", "temp", "ratings"]
subject = ["subway", "Tony's bistro", "Pizza"]
cmds  = ["hour", "rating", "temp"]



subjects = interpret2(inputs, subject)
commands = interpret2(inputs, cmds)
print(subjects)
print(commands)


