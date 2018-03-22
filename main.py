import json
from mod_api import WeatherAPI

# Please use your own key!
# API_KEY = 38d423b88b9b7069

def main():
  try:
    f = open('key.json')
    _content = json.load(f)
    API_KEY = _content['key']
  except Exception as e:
    print("Key file not found.")
    print("Type your API key below.")
    print("Hint: You can copy and rename 'key.example' file.")
    print("")
    API_KEY = str(input("API_KEY: "))

  if not API_KEY:
    print("You need an API key to use this service.")
    print("Create one for free here:")
    print("https://www.wunderground.com/weather/api/")
    return

  print("Where do you live?")
  country = str(input("Country: ")).replace(" ", "+")
  state = '' # optionnal.
  # state = str(input("State: ")).replace(" ", "+")
  city = str(input("City: ")).replace(" ", "+")
  try:
    _api = WeatherAPI(API_KEY)
    _api.query(country, state, city)
    _api.save()
  except Exception as e:
    print("Error on query: " + str(e))
  else:
    print("Your data has been saved in 'data.json' for this search: " + country + ", " + state + " " + city)
    print("")
    print("You can see the results online here: ")
    print(_api.url)

if __name__ == "__main__":
  main()
