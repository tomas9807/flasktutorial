from . import app
from flask import render_template,flash,redirect,url_for
from .forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'author':{'username':'tomas'},
            'body':'i like tomatoes'
        },
        {
            'author':{'username':'juana'},
            'body':'i like cerezas'
        }
    ]
    return render_template('index.html',title='home',posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form  = LoginForm()
    if form.validate_on_submit():
        flash(f'Login request for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html',title='login',form=form)