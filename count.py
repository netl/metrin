import os
import copy
import json

def getAlcoholics(homedir = os.getcwd()):
   os.chdir(homedir)
   path, dirs, files = next(os.walk(homedir))

   alcoholics = [
   ]
   #count drinks for each user
   identifier = 0
   for alcoholic in dirs:
      #get uploads
      p, d, f = next(os.walk(homedir + "/" + alcoholic))
      count = len(f)

      #find newest file
      os.chdir(p)
      newest = max(f, key = os.path.getctime)

      #create entry
      alcoholics.append({
         "name":alcoholic,
         "id":identifier,
         "count":count,
         "last":{
            "time": os.path.getctime(newest),
            "file": newest,
         },
      })
      identifier += 1

   return alcoholics     

if __name__ == "__main__":
   print(json.dumps(getAlcoholics()))
