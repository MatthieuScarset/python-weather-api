from mod_api import WeatherAPI

API_KEY = "38d423b88b9b7069"
country = 'canada'
state = 'quebec'
city = 'montreal'

def main():
  # country = str(input("What country do you want to forecast? ")).replace(" ", "+")
  # state = str(input("What state? ")).replace(" ", "+")
  # city = str(input("What city? ")).replace(" ", "+")
  try:
    _api = WeatherAPI(API_KEY)
    _api.query(country, state, city)
    _api.save()
  except Exception as e:
    print("Error on query: " + str(e))
  finally:
    print("Your data has been saved in 'data.json' for this search: ")
    print("country: " + country)
    print("state: " + state)
    print("city: " + city)
    print("")
    print("You can see the results online here: ")
    print(_api.url)

if __name__ == "__main__":
  main()
