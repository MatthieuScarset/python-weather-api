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
  
  def prepareQuery(self, country, state, city):
    # All keys required.
    #for k,v in self.conditions.items():
    #  if not v:
    #    raise QueryMissingParametersError(k)
    # 
    # Only Country and City are required.
    if not country:
      raise QueryMissingParametersError('city')
    elif not city:
      raise QueryMissingParametersError('city')
    else:
      self.conditions = {
        'country': country,
        'state': state,
        'city': city
      }
  
  def buildUrl(self):
    self.url = self.protocol + self.url + self.path + self.key + "/conditions/q/" + '/'.join(self.conditions.values()) + ".json"
    return self.url

  def query(self, country = '', state = '', city = ''):
    try:
      self.prepareQuery(country, state, city)
      self.buildUrl()
      self.call()
    except Exception as e:
      print("Error during query: " + str(e))
    return self.data

  def save(self, filename = 'data.json'):
    self.results = None
    try:
      self.results = self.data['results']
    except KeyError:
      try:
        self.results = self.data['current_observation']
      except KeyError:
        print("No results for your search. Try something else.")

    if self.results:
      f = open('data.json', 'w')
      json.dump(self.results, f, indent=2)

  def call(self):
    if not self.url:
      raise QueryMissingParametersError('self.url')
    try:
      r = requests.get(self.url)
      self.data = r.json()
    except Exception as e:
      print("Error in API call " + str(e))
    else:
      return self.data

  def search(self):
    pass
