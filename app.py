from flask import Flask, flash, redirect, render_template, request, json
import os
import urllib.request
from jinja2 import ext
from datetime import datetime

app = Flask(__name__)

with urllib.request.urlopen("http://apis.is/petrol") as url:
    gogn = json.loads(url.read().decode())
    li = gogn['results']

app.jinja_env.add_extension(ext.do)

date = gogn["timestampPriceCheck"]
def inttomon(i):
    gogn = {
        "01": "janúar",
        "02": "febrúar",
        "03": "mars",
        "04": "apríl",
        "05": "maí",
        "06": "júní",
        "07": "júlí",
        "08": "ágúst",
        "09": "september",
        "10": "október",
        "11": "nóvember",
        "12": "desember"
    }
    return gogn[i]

date = gogn["timestampPriceCheck"]
def getdate(values, date=date):
    obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    values = values
    return obj.strftime(f"%d {inttomon(obj.strftime('%m'))} %Y %H:%M")

app.jinja_env.filters['getdate'] = getdate

def min():
    cheapest = {"bensin":10000,"bensin-nafn":None,"diesel":10000,"diesel-nafn":None}
    for x in li:
        if x["bensin95"] < cheapest["bensin"]:
            cheapest["bensin"] = x["bensin95"]
            cheapest["bensin-nafn"] = x["company"]
            cheapest["nafnbensinstodvar"] = x["name"]
        if x["diesel"] < cheapest["diesel"]:
            cheapest["diesel"] = x["diesel"]
            cheapest["diesel-nafn"] = x["company"]
            cheapest["nafndieselstodvar"] = x["name"]
    return cheapest


#---------------------routes---------------------

@app.route("/")
def index():
    oneco = []
    for x in li:
        if x['company'] not in oneco:
            oneco.append(x['company'])
    cheapest = min()
    return render_template("index.tpl",oneco = oneco, nafnbensinstodvar = cheapest["nafnbensinstodvar"], nafndieselstodvar = cheapest["nafndieselstodvar"], minbensin = cheapest["bensin"], mindiesel = cheapest["diesel"], bensinnafn = cheapest["bensin-nafn"], dieselnafn = cheapest["diesel-nafn"])

@app.route("/company/<nafn>")
def fyrirtaeki(nafn):
    stodvar = []
    for x in li:
        if x["company"] == nafn:
            stodvar.append(x)
    x = len(stodvar)
    return render_template("company.tpl", stodvar = stodvar, fjoldi = x)

@app.route("/<company>/<nafn>")
def moreinfo(company,nafn):
    stod = {}
    for x in li:
        if x["name"] == nafn:
            stod = x
            break
    return render_template("moreinfo.tpl", soluadili = company, nafn = nafn, bensin = stod["bensin95"], diesel = stod["diesel"], lat = stod["geo"]["lat"], lon = stod["geo"]["lon"])
    
#-------------------run---------------------

@app.errorhandler(404)
def error404(error):
	return render_template("404.tpl"),404

if __name__ == "__main__":
	app.run(debug=True)