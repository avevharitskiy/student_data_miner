# -*- coding: utf-8 -*-
from server import server
from flask import render_template
from server.forms import LoginForm


@server.route('/')
def main_page():
    return render_template('login.html', title='Auth')


@server.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
