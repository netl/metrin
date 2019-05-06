from flask import Flask
from flask import render_template
from count import getAlcoholics
from operator import itemgetter
import json
app = Flask(__name__)

drinksPath = "/var/local/ftp/alkometri"

@app.route('/alkometri')
def frontpage():
   alcoholics = getAlcoholics(drinksPath)

   #sort by newest
   scores = sorted(alcoholics, key = lambda x: x['last']['time'], reverse = True)

   #count total
   total = 0
   for a in alcoholics:
      total += a["count"]

   #find who has the newest entry
   newest = {"last":{"time":0}}
   for a in alcoholics:
      if a["last"]["time"] > newest["last"]["time"]:
         newest = a
   newestPic =  "/static/alkometri/" + newest["name"] + "/" + newest["last"]["file"]

   return render_template('alkometri.html', total = total, newest = newestPic, scores = scores)

@app.route('/alkometri/api')
def api():
    return json.dumps(getAlcoholics(drinksPath))
