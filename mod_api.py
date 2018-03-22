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
    self.conditions = {
      'country': country,
      'state': state,
      'city': city
    }
    for k,v in self.conditions.items():
      if not v:
        raise QueryMissingParametersError(k)
        # @todo get current location
  
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
    try:
      _results = self.data['response']['results']
    except KeyError as e:
      print("No results for your search. Try something else.")
    else:
      f = open('data.json', 'w')
      json.dump(_results, f, indent=2)

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
