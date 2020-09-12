

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import Session
import sqlite3
import pandas as pd
import os
import psycopg2
app = Flask(__name__)
# DATABASE_URL = os.environ['postgresql://postgres:Aqrt3456@localhost:5432/Texas']
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')


# app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///executions.sqlite"

db = SQLAlchemy(app)

# from .models import Songs, Features


class County(db.Model):
    __tablename__ = 'county'

    Index = db.Column(db.Integer)
    County = db.Column(db.String, primary_key=True)
    Count = db.Column(db.Integer)

    def __repr__(self):
        return '<County %r>' % (self.Index)


class Offender(db.Model):
    __tablename__ = 'offender'

    Index = db.Column(db.Integer)
    Execution = db.Column(db.Integer, primary_key=True)
    Link = db.Column(db.String)
    Last_Name = db.Column(db.String)
    First_Name = db.Column(db.String)
    TDCJ = db.Column(db.Integer)
    Age = db.Column(db.Integer)
    Date = db.Column(db.Date)
    Race = db.Column(db.String)
    County = db.Column(db.String)

    def __repr__(self):
        return '<Offender %r>' % (self.Index)


class Words(db.Model):
    __tablename__ = 'words'

    Index = db.Column(db.Integer, primary_key=True)
    Most_Spoken_Words = db.Column(db.String)
    Count_of_Words = db.Column(db.Integer)

    def __repr__(self):
        return '<Songs %r>' % (self.Index)


# os.environ.get(
   # 'DATABASE_URL', 'postgresql://postgres:Aqrt3456@localhost:5432/Texas')
#conn = psycopg2.connect(DATABASE_URL, sslmode='require')


# 'postgresql://postgres:Aqrt3456#ec2-50-17-178-87.compute-1.amazonaws.com:5432/d5h9p1h0rke9bu?sslmode=require'


# 'postgresql://postgres:Aqrt3456@localhost:5432/Texas'


# "postgresql+psycopg2://kfgriimpfjecsv:Bk1*******G#ec2-23-21-215-184.compute-1.amazonaws.com:5432/dd71doth8gopgh?sslmode=require"

# postgres://hfkztmzclzhkob:ea9192818d18bcb07e2e383229835c7edffd02a3de217c1d2f1417d8648c59d5@ec2-50-17-178-87.compute-1.amazonaws.com:5432/d5h9p1h0rke9bu
# os.environ.get(
# 'DATABASE_URL', 'postgresql://postgres:Aqrt3456@localhost:5432/Texas')
db = SQLAlchemy(app)


@app.route("/",  methods=["GET"])
def pie():
    import random
    offender_df = pd.read_sql_table(
        'offender', 'sqlite:///executions.sqlite')

    global offender_dictionary
    offender_dictionary = offender_df.to_dict('index')
    random_offender = random.choice(list(offender_dictionary.values()))

    return render_template('pie.html', random_offender=random_offender)


@app.route("/words")
def words():

    words_df = pd.read_sql_table(
        'words', 'sqlite:///executions.sqlite')

    # words_df.head()

    list_of_words = words_df['Most_Spoken_Words'].to_list()
    count_of_words = words_df['Count_of_Words'].to_list()

    words_dictionary = {"Most_Spoken_Words": list_of_words,
                        "Count_of_Words": count_of_words}

    return jsonify(words_dictionary)


@app.route("/county")
def county():
    county_df = pd.read_sql_table(
        'county', 'sqlite:///executions.sqlite')
    county_df = county_df.drop(['index'], axis=1)

    county_dictionary = county_df.to_dict('records')

    return jsonify(county_dictionary)


@app.route("/offenders")
def index():

    offender_df = pd.read_sql_table(
        'offender', 'sqlite:///executions.sqlite')

    offender_df.head()
    global offender_dictionary
    offender_dictionary = offender_df.to_dict('index')

    return jsonify(offender_dictionary)


if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    #port = int(os.environ.get('PORT', 5432))
    # app.run(threaded=True, port=5000)
    #app.run(debug=True, host='0.0.0.0')
    # (host='127.0.0.1', port=port)
    #app.run(debug=True, host='127.0.0.1', port=5432)
    app.run()
    # app.run(threaded=True, port=5000)
