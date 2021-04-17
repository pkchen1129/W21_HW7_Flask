from flask import Flask, render_template
import requests
import secrets
import json

class Headline_class:
    def __init__(self, topic, url, thumbnails) -> None:
        self.topic = topic
        self.url = url
        self.thumbnails = thumbnails


app = Flask(__name__)

@app.route('/')
def index():     
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def name(nm):
    return render_template('name.html', name=nm)

# Input type and name
@app.route('/<type>/<nm>')
def headlines_result(type, nm):
    url = "https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={}".format(secrets.api_key)
    
    headlines_result = requests.get(url).json()
    headline_list = []
    for i in range(5):
        head = headlines_result['results'][i]
        tmp = Headline_class(head['title'], head['url'], head['multimedia'][1]["url"])
        headline_list.append(tmp)
    # Could enter links, headline
    template_name = type + '.html'
    return render_template(template_name, name=nm, headlines_result=headline_list)


if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    ## Download json file
    # url = "https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={}".format(secrets.api_key)
    # headlines_result = requests.get(url).json()
    # dumped_json_cache = json.dumps(headlines_result,sort_keys=True, indent=4)
    # fw = open("Hi.json","w")
    # fw.write(dumped_json_cache)
    # fw.close() 

    # Run app
    app.run(debug=True)