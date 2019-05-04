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
   newestID = alcoholics[0]["last"]["by"]
   newest =  "/static/alkometri/" + alcoholics[newestID]["name"] + "/" + alcoholics[0]["last"]["file"]
   scores = []
   for key, value in alcoholics.items():
      scores.append([value['name'], value['count']])
   scores = sorted(scores, key = itemgetter(1), reverse = True)
   return render_template('alkometri.html', newest = newest, scores = scores)

@app.route('/alkometri/api')
def api():
    return json.dumps(getAlcoholics(drinksPath))
