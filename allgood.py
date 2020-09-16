import requests
import datetime
import flask
import yaml

app = flask.Flask(__name__)
config = 'sites.yml'
refresh = 60


with open(config, 'r') as stream:
    try:
        sites = (yaml.safe_load(stream))
    except Exception as exc:
        print (exc)


codes = {}
for site in sites:
  req = requests.get(site)
  codes[site] = req.status_code


@app.route('/')
def home():
  html = '<html><head><meta http-equiv=refresh content=' + str(refresh) + '>' + \
         '<title>allgood</title></head><body>' + str(datetime.datetime.now()) + '<p><table>'
  for site, code in codes.items():
    html += '<tr><td>' + site + '</td><td>' + str(code) + '</td></tr>'
  html += '</table></body></html>'
  return html


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=9999, debug=True)
