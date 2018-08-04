from markdown import markdown
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask import Markup
from models import DataSet, Researcher

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
    datasets = test_content()
    return render_template('index.html', datasets=datasets)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/snippets')
def snippets():
    with open('snippets.md', 'r') as f: 
        content = Markup(markdown(f.read()))    
    return render_template('snippets.html', content=content)

def test_content():
    hrs = DataSet(name='Health and Retirement Study'
                , description=('Longitudinal survey of adults aged 50+ and '
                           'their spouses from 1996 to 2014.')) 
    fbi = DataSet(name='FBI Crime Data thing'
                , description=('Data obtained from FBI API'))
    
    others = [DataSet(name=('Thing {}'.format(i))
                , description=('OK **hello**') 
                , snippet=('x = 5')) for i in range(1, 31)]
    return [hrs, fbi] + others

