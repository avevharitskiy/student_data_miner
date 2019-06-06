# -*- coding: utf-8 -*-
from server import server
from flask import render_template, request, redirect, url_for
from api.login import get_login_uri

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
    return "This is user page: " + request.args.get('code')

import vk

vk.AuthSession()