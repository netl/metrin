import os
import copy
import json

def getAlcoholics(homedir = os.getcwd()):
   os.chdir(homedir)
   path, dirs, files = next(os.walk(homedir))

   #generate global with values that are to be compared
   alcoholics = {
   0:{
      "name":"global",
      "count":0,
      "last":{"time":0},
      },
   }

   #count drinks for each user
   identifier = 1
   for alcoholic in dirs:
      p, d, f = next(os.walk(homedir + "/" + alcoholic))
      count = len(f)
      os.chdir(p)

      #find newest file
      newest = max(f, key = os.path.getctime)
      alcoholics[identifier]={
         "name":alcoholic,
         "count":count,
         "last":{
            "time": os.path.getctime(newest),
            "file": newest,
         },
      }
      alcoholics[0]["count"]+=count
      identifier += 1

   #find the globally newest file
   newest = {"time":0}
   for key, value in alcoholics.items():
      if value["last"]["time"] > newest["time"]:
         newest = value["last"].copy()
         newest["by"] = key
   alcoholics[0]["last"] = newest

   return alcoholics     

if __name__ == "__main__":
   print(json.dumps(getAlcoholics()))
