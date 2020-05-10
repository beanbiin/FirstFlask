# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash, Markup

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, IntegerField, TextField,\
    FormField, SelectField, FieldList
from wtforms.validators import DataRequired, Length
from wtforms.fields import *
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch

app = Flask(__name__)


app.config.update(
    DEBUG=True,
    SQLALCHEMY_DATABASE_URI='sqlite:///:memory:',
    SECRET_KEY='James Bond',
    SECURITY_REGISTERABLE=True,
)

bootstrap = Bootstrap(app)

es = Elasticsearch('192.168.234.134:9200')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def test_form():
    form = HelloForm()
    return render_template('form.html', form=form, telephone_form=TelephoneForm(), contact_form=ContactForm(), im_form=IMForm(), button_form=ButtonForm(), example_form=ExampleForm())


@app.route('/nav', methods=['GET', 'POST'])
def test_nav():
    return render_template('nav.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = HelloForm
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template('logout.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        return redirect(url_for('search_result', keywords=request.values['keyword']))
    return render_template('search.html')


@app.route('/search/search_result/<keywords>')
def search_result(keywords):
    data = {'query': {'match': {'judge_content': keywords}}}
    results = es.search(index='judicial_test', body=data)['hits']['hits'][0:3]
    # return jsonify(results)
    return render_template('search_result.html', results=results)


@app.route('/win_lose')
def win_lose():
    return render_template('win_lose.html')


@app.route('/statistic_keywords')
def statistic_keywords():
    return render_template('statistic_keywords.html')


@app.route('/statistic_laws')
def statistic_laws():
    return render_template('statistic_laws.html')


@app.route('/statistic_locations')
def statistic_locations():
    return render_template('statistic_location.html')




if __name__ == '__main__':
    app.run(debug=True)
