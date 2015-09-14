# -*- coding: utf-8 -*-
from flask import render_template,flash,redirect
from app import app
from .forms import LoginForm
from flask.ext.bootstrap import Bootstrap
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template("welcome.html")

@app.route('/index')
def passage_list():
    user = { 'nickname': 'Reader' } # fake user
    posts = ['this is the first passage','this is the second passage','this is the third passage','this is the forth passage','this is the fifth passage','this is the sixth passage']
    return render_template("index.html",user = user, posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form)
