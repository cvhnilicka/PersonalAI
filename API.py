
import requests

class API:
	
	underground_key = "9336d91494799de4c1a02efcf9c84368"
	google_api_key = "AIzaSyBVU2iI94OgOpwk_GvxEBQroZ-ryM6Znpw"

	validAPIs = {
	"weather" : None

}
	@staticmethod
	def weatherApi(string):
		idnum = 4434663 #madison, wi
		if string != None:
			city = string
			cities = eval(open('cities_dict.txt', 'r').read())
			if city in cities: 
				idnum = cities[city]
		 
		api = ('http://api.openweathermap.org/data/2.5/weather?''id=%s''&APPID=9336d91494799de4c1a02efcf9c84368') % (idnum) 

		r = requests.get(api)
        	feed = r.json()

        	#save the weather summary
        	weather_whole = feed["weather"][0]
        	weather_summary = weather_whole["main"]
        	#current temperature
        	temp = feed["main"]["temp"]
        	temp = (temp * (9/5) - 459.67)

        	#current description of weatheer
        	description = weather_whole["description"]

        	#current wind information
	        wind_speed = feed["wind"]["speed"]

		print temp
API.weatherApi(None)
