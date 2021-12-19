import numpy as np
import pandas as pd
import csv


convertData = ['cast', 'crew', 'keywords', 'genres']

def getSupervisor(crew):
  for member in crew:
    if member['job'] == 'Visual Effects Supervisor':
        return member['name']
        return np.nan

def getList(x):
    if isinstance(x, list):
        name = [i['name'] for i in x]
        if len(name) > 4:
            return name
    return name



def cleanData(data):
    if isinstance(data, list):
      return [str.lower(x.replace(" ", "")) for x in data]
    else:
        if isinstance (data, str):
          return str.lower(data.replace("", ""))
        else:
            return ''


print(getSupervisor('Visual Effects Supervisor'))