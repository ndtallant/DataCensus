from markdown import markdown
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask import Markup

app = Flask(__name__)
app.debug = True
bootstrap = Bootstrap(app)
nav = Nav()

@nav.navigation()
def mynavbar():
    return Navbar(
        'Data Census',
        View('Home', 'index'),
        View('About', 'about'),
        View('Snippets', 'snippets'),
    )
nav.init_app(app)

@app.route('/')
def index():
    hrs = DataSet(name='Health and Retirement Study (HRS)'
            , description=('Longitudinal survey of adults aged 50+ and '
                           'their spouses from 1996 to 2014.')) 
    return render_template('index.html', datasets=[hrs])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/snippets')
def snippets():
    with open('snippets.md', 'r') as f: 
        content = Markup(markdown(f.read()))    
    return render_template('snippets.html', content=content)

class DataSet:
    def __init__(self, name, description, snippet=None):
        self.name = name
        self.description = description
        self.snippet = snippet
