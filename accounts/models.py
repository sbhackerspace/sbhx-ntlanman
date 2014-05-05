#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2014.05.04

from flask import Flask
app = Flask(__name__)

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # FIXME: Just grab from users.card_id instead of storing here?
    card_id = db.Column(db.String(64), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.usr_id'))
    balance_in_cents = db.Column(db.Integer, nullable=False)

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime,
                           default=db.func.now(),
                           onupdate=db.func.now())

    def __init__(self, card_id, user_id):
        self.card_id = card_id
        self.user_id = user_id
        self.balance_in_cents = 0

    def __repr__(self):
        return '<Card %r for User %r>' % (self.card_id, self.user_id)
