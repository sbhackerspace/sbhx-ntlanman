#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2014.05.04

import os

config = {
    'DEBUG': True,
    'MYSQL_DATABASE_HOST': '192.168.16.20',
    'MYSQL_DATABASE_USER': 'accounts_app',
    'MYSQL_DATABASE_PASSWORD': os.getenv('MYSQL_DATABASE_PASSWORD'),
    'MYSQL_DATABASE_DB': 'radius',
}

config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%(MYSQL_DATABASE_USER)s:%(MYSQL_DATABASE_PASSWORD)s@%(MYSQL_DATABASE_HOST)s:3306/%(MYSQL_DATABASE_DB)s' % config
