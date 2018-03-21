from mod_api import WeatherAPI

API_KEY = "38d423b88b9b7069"

def main():
  country = str(input("What country do you want to forecast? ")).replace(" ", "+")
  state = str(input("What state? ")).replace(" ", "+")
  city = str(input("What city? ")).replace(" ", "+")
  try:
    _api = WeatherAPI(API_KEY)
    _raw = _api.query(country, state, city)
    try:
      _data = _raw['response']['results']
    except KeyError as e:
      print("Error in the response (" + str(e) + ")")
    else:
      _api.save(_data)
  except Exception as e:
    print("Error on query: " + str(e))
  finally:
    print('Done')

if __name__ == "__main__":
  main()