# -*- coding: utf-8 -*-
from server import server
from flask import render_template, request, redirect, url_for, make_response
from api import auth
from api import user
import api.analyse as network_enviroment


@server.route('/')
def main_page():
    if 'access_token' in request.cookies and auth.validate_access_token(request.cookies.get('access_token')):
        return redirect(url_for('user_page'))
    else:
        return redirect(url_for('login'))


@server.route('/login', methods=['GET', 'POST'])
def login():

    if 'code' in request.args:
        access_token = auth.get_access_token(request.args['code'])
        response = make_response(redirect(url_for('user_page')))
        response.set_cookie('access_token', access_token)
        return response

    return render_template('login.html', error=request.args.get('error_description', None))


@server.route('/user_page')
def user_page():
    if 'access_token' in request.cookies and auth.validate_access_token(request.cookies.get('access_token')):
        access_token = request.cookies.get('access_token')
        user_info = user.get_info(access_token, fields=['bdate', 'photo_200_orig', 'city', 'country'])
        friend_list = user.get_friends(access_token, fields=['photo_200_orig'], order='hints')
        return render_template('user_page.html', user_info=user_info, friends_list=friend_list)
    else:
        return redirect(url_for('login'))
    
@server.route('/analyse')
def analyse():
    if 'access_token' in request.cookies and auth.validate_access_token(request.cookies.get('access_token')):
        access_token = request.cookies.get('access_token')
        prepared_data = network_enviroment.prepare_data(access_token, request.args.get('analyse_id', None))
    else:
        return redirect(url_for('login'))
    