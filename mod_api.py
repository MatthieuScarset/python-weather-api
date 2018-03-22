import requests
import json
from mod_errors import QueryMissingParametersError

API_HTTP = "http://"
API_URL = "api.wunderground.com"
API_PATH = "/api/"

class WeatherAPI:
  def __init__(self, API_KEY):
    self.protocol = "http://"
    self.url = API_URL
    self.path = API_PATH
    self.key = API_KEY
  
  def buildUrl(self):
    _conditions = []
    for k,v in self.conditions.items():
      if not v:
        raise QueryMissingParametersError(k)
      else:
        _conditions.append(v)
    self.url = self.protocol + self.url + self.path + self.key + "/conditions/q/" + '/'.join(_conditions) + ".json"
    return self.url

  def query(self, country, state, city):
    self.conditions = {
      'country': country,
      'state': state,
      'city': city
    }
    try:
      data = {}
      json_url = self.buildUrl()
      r = requests.get(json_url)
      data = r.json()
    except Exception as e:
      print("Error during query: " + str(e))
    else:
      pass
    finally:
      pass
    return data

  def save(self, data, filename = 'data.json'):
    f = open('data.json', 'w')
    json.dump(data, f, indent=2)
