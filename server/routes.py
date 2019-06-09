# -*- coding: utf-8 -*-
from server import server
from flask import render_template, request, redirect, url_for
from api.login import get_login_uri


import api.test as test



@server.route('/')
def main_page():
    if 'user_token' in request.cookies:
        return request.cookies.get('user_token')
    else:
        return redirect(url_for('login'))


@server.route('/login', methods=['GET', 'POST'])
def login():
    login_link = get_login_uri(server.config.get('VK_APP_ID'), server.config.get('SERVICE_URI'))
    return render_template('login.html', login_link=login_link)


@server.route('/user_page')
def user_page():
    user_info = test.get_user_info()
    friends_list = test.get_friends_list()
    return render_template('user_page.html', user_info=user_info, friends_list=friends_list)