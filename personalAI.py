
from __future__ import print_function 
import smtplib
import readline
import imaplib
import requests
import json
import re,requests
import difflib

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Restaurant(object):

	commands = ["info", "hour", "name", "price", "open", "rating"]

	def __init__(self, name, price, open_now, rating):
		self.name = name
		self.price = price
		self.open_now = open_now
		self.rating = rating
	
	def toString(self):
		s = "Restaurant: " + color.BOLD + color.PURPLE  + self.name + color.END + color.GREEN + "\n Price Range: " + color.END + str(self.price) + color.GREEN +"\n Open: " +color.END + str(self.open_now) + color.GREEN +"\n Rating: "+ color.END + str(self.rating)
		return s

	def getName(self):
		return  "Restaurant: " + self.name + "\n"

	def getPrice(self):
		return "Price Range: " + self.price + "\n"
	
	def getOpen(self):
		return "Open: " + self.open_now + "\n"
	
	def getRating(self):
		return "Rating: " + self.rating + "\n" 




#print("Hello, Who may I be speaking to?\n")
person = raw_input( "Hello, Who may I be speaking to?\n")

print('Hello, %s' %person)

loopingvar = True
places = {}
rests = []


def hungry():
	print("Why don't I find you somewhere to eat?")

def stoned():
	print("Heading to Kwik trip?")
	ans = raw_input()
	if ans == 'y':
		print("I'll check the weather")
		checkWeather()
	else:
		print("Shall I turn the lights off?\n")

def findLocation():
	response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=3+N+Randall,+Madison,+CA')
	resp_json_payload = response.json()
	lat = resp_json_payload['results'][0]['geometry']['location']['lat']
	lng = resp_json_payload['results'][0]['geometry']['location']['lng']
	print(lat)
	print(lng)
	return (lat, lng)

def interpret(arr1, arr2):
	set1 = []
	for i in arr1:
		for j in arr2:
			if SequenceMatcher(None, i, j) >0.80:
				set1.append(j)
	return set1

def placesListen():
	query = raw_input()	
	query = query.lower()
	split = query.split(" ")	
	s = "'s"
	for i in range(0, len(split)):
		if s in split[i]: 	
			split[i] =split[i][:-2]				
	set_restaurants = interpret(split, restaurants)
	set_instruct = interpret(split, Restaurant.commands)


def findRestaurants():
	lat, lng = findLocation()
	search_type = "restaurant"
	radius = 1000
	key = "AIzaSyBVU2iI94OgOpwk_GvxEBQroZ-ryM6Znpw"
	location = str(lat) + "," + str(lng)
	MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
           '?location=%s'
           '&radius=%s'
           '&types=%s'
           '&sensor=false&key=%s') % (location, radius, search_type, key)
	#grabbing the JSON result
	response = requests.get(MyUrl)
	json_dump = response.json()
	rest_list = json_dump["results"]
	
	k = 0
	for i in rest_list:
		temp_name = i["name"]
		if "price_level" in i:
			temp_price = i["price_level"]
		else:
			temp_price = "Price Range not available"
		if "opening_hours" in i:
			open_now = i["opening_hours"]["open_now"]
		else:
			open_now = "Hours not available"
		if "rating" in i:
			rating = i["rating"]
		else:
			rating = ("Rating not available")
		rest = Restaurant(temp_name, temp_price, open_now, rating)
		print(rest.toString())
		a = temp_name
		global rests
		rests.append(temp_name)
		
		if a in places:
			print(a)
			places[a].append(rest)
		else:
			print(a)
			places[a] = []
			places[a].append(rest)
		
	placesListen()
		



def checkWeather():
	#request and save the JSON request
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=4434663&APPID=9336d91494799de4c1a02efcf9c84368')
	feed = r.json()

	#save the weather summary
	weather_whole = feed["weather"][0]
	weather_summary = weather_whole["main"]
	#current temperature
	temp = feed["main"]["temp"]
	#temp = (temp * (9/5) - 459.67)

	#current description of weatheer
	description = weather_whole["description"]
	
	#current wind information
	wind_speed = feed["wind"]["speed"]

	# communication structure 
	listen = "true"
	iteration = 0;	
	while listen :
		command = ""
		if (iteration == 0):
			command = raw_input("How much of the information would you like?\n")
		elif iteration == -1:
			print("Sounds good!\n")
			break
		else:
			command = raw_input("Anything else?\n")
		command = command.lower()
		list_cmds = []
		werf = command.split(" ")
		print(werf)
		for x in werf:
			if x == "temp":
				list_cmds.append("temp")
				
			elif x == "summary":
				list_cmds.append("summary")
				
			elif x == "wind":
				list_cmds.append("wind")
				
			elif x in ["like", "description"]:
					print("fuck")
					print(x)
					list_cmds.append("description")
				
			elif x in ["nevermind", "nah", "nothing"]:
				list_cmds.append("exit")
				
			
		information = {
		'wind': "The wind speed is " + str(wind_speed),
		'temp': "The temperature is " + str(int(temp)),
		'description': "The description is " + description,
		'summary': "The summary is " + weather_summary,
}
		print(list_cmds)	
		for i in list_cmds:
			if i == "exit":
				iteration = -1
				break
			else:
				print(information[i])
			iteration = iteration + 1

	
def sendInfo():
	server = 'smtp.gmail.com'
	user = 'Cormicks.PA'
	password = 'CormicksPA123'

	recipients = ['cvhnilicka@wisc.edu', 'cormickhnilicka@gmail.com']
	sender = 'cormicks.pa@gmail.com'
	
	message = raw_input("Content: ")

	session = smtplib.SMTP(server)
	session.ehlo()
	session.starttls()
	session.login(user, password)
	session.sendmail(sender, recipients, message)
	

def exit():
	loopingvar = False
	print(loopingvar)	

commands = {
	0 : hungry,
	1 : stoned,
	2 : sendInfo,
	3 : checkWeather,
	4 : findLocation,
	5 : findRestaurants,
	6 : exit, 


}

while loopingvar:

	cmd = input("What would you like me to do?\n")
	
	commands[cmd]()
	print(loopingvar)
	if loopingvar == False:
		break
