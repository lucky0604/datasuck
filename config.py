# coding: utf-8

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:lovezt520@localhost:3306/flaskmega?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
