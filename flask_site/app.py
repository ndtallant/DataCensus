from markdown import markdown
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask import Markup
# from db_models import DataSet, Researcher
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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
    #affiliation = request.form['user_affiliation']
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
