

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import Session
import sqlite3
import pandas as pd
import os
import psycopg2
app = Flask(__name__)


# create SQLlite connection
# app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///executions.sqlite"

db = SQLAlchemy(app)

# Create DB classes for SQLAlchemy


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
        return '<Words %r>' % (self.Index)


db = SQLAlchemy(app)

# create Flask Routes
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

    app.run()
