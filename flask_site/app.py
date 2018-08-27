import os
from flask import Markup
from flask_nav import Nav
from markdown import markdown
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_nav.elements import Navbar, View
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, render_template, render_template_string

from flask_frozen import Freezer
from flask_flatpages import (
    FlatPages, pygmented_markdown, pygments_style_defs)

def prerender_jinja(text):
    """ Pre-renders Jinja templates before markdown. """
    prerendered_body = render_template_string(text)
    return pygmented_markdown(prerendered_body)

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_HTML_RENDERER = prerender_jinja
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.debug = True
bootstrap = Bootstrap(app)
nav = Nav()
pages = FlatPages(app)
freezer = Freezer(app)

@nav.navigation()
def mynavbar():
    return Navbar(
        'Data Census',
        View('Home', 'index'),
        View('About', 'about'),
        View('Snippets', 'snippets'),
        View('Contribute', 'contribute'),
    )
nav.init_app(app)

@app.route('/')
def index():
    datasets = DataSet.query.all()
    return render_template('index.html', datasets=datasets)

@app.route('/about')
def about():
    #with open('about.md', 'r') as f:
    #    about_block = markdown(f.read()) 
    return render_template('about.html')

@app.route('/snippets')
def snippets():
    #with open('snippets.md', 'r') as f: 
    #    content = Markup(markdown(f.read()))    
    return render_template('test_snippet_thing.html') #, content=content)

@app.route('/snippet/<name>')
def snippet_example(name):
    return name 

@app.route('/contribute', methods=['GET', 'POST'])
def contribute():
    #name = request.form['user_name'] 
    #department = request.form['user_department']
    #affliation = request.form['user_affiliation']
    #rv = f'Data Submission from {name}, {affiliation} at {department}'
    #print(rv) 
    return render_template('contribute.html')

class DataSet(db.Model):
    __tablename__ = 'datasets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    snippet = db.Column(db.Text)
    
    def __repr__(self):
        return 'DataSet: ' + self.name

class Researcher(db.Model):
    __tablename__ = 'researchers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    department = db.Column(db.String(64), nullable=False)
    affiliation = db.Column(db.String(64))
    
    def __repr__(self):
         return ('Researcher: ' + self.name + '\n' + 
                 self.affiliation + ' at ' + self.department)
