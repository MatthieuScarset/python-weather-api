class QueryMissingParametersError(Exception):
  def __init__(self, param):
    self.param = param
    
  def __str__(self):
    return "Insufficient query parameters (missing {0})".format(self.param)
