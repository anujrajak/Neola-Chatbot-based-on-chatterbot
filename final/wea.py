from weather import Weather, Unit

def weather(loc='jabalpur'):
	print(loc)
	weather = Weather(unit=Unit.CELSIUS)
	location = weather.lookup_by_location(loc)
	condition = location.condition
	fi = condition.text
	se = condition.temp
	report = str("It is a"+fi+"with "+se+" degree celsius temperature")
	print("Weather : "+report)
	return report

# print(weather())
