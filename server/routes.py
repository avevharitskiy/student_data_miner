# -*- coding: utf-8 -*-
import urllib.parse as url

from flask import make_response, redirect, render_template, request, url_for

import api.analyse as network_enviroment
from api import auth, user
from server import server


@server.route('/')
@auth.decorator
def main_page():
    return redirect(url_for('user_page'))


@server.route('/login', methods=['GET', 'POST'])
@auth.login
def login():

    if 'code' in request.args:
        access_token = auth.get_access_token(request.args['code'])
        response = make_response(redirect(url_for('user_page')))
        response.set_cookie('access_token', access_token)
        return response

    return render_template(
        'login.html',
        error=request.args.get('error_description', None),
        app_id=url.quote(server.config.get('VK_APP_ID'),safe=''),
        service_url=url.quote(server.config.get('SERVICE_URL'), safe='')
        )


@server.route('/user_page')
@auth.decorator
def user_page():
    access_token = request.cookies.get('access_token')
    user_info = user.get_info(access_token, fields=['bdate', 'photo_200_orig', 'city', 'country'])
    friend_list = user.get_friends(access_token, fields=['photo_200_orig'], order='hints')
    return render_template('user_page.html', user_info=user_info, friends_list=friend_list)


@server.route('/analyse')
@auth.decorator
def analyse():
    access_token = request.cookies.get('access_token')
    model = network_enviroment.build_model(access_token, request.args.get('analyse_id', None))
