from . import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    context = {'title':'microlog','user':'tomas'}
    return render_template('index.html',**context)