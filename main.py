import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from google.appengine.ext import ndb

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=False,
    SECRET_KEY='wooyun',
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# define the data you want


class Attackdata(ndb.Model):
    types = ndb.StringProperty()
    url = ndb.StringProperty()


@app.route('/favicon.ico')
def favicon():
    abort(404)


@app.route('/webscan_360_cn.html')
def webscan():
    return render_template('webscan_360_cn.html')


@app.route('/admin-console/delall')
def delall():
    ndb.delete_multi(Attackdata.query().fetch(keys_only=True))
    return 'success'


@app.route('/admin-console/readall')
def readall():
    return render_template('nothing.html', data=Attackdata.query().fetch())


@app.route('/', methods=['GET', 'POST'])
def index():
    test = Attackdata(types=request.method, url=request.url)
    test.put()
    return "welcome-scanner"


@app.route('/<path:path>', methods=['GET', 'POST'])
def general(path):
    test = Attackdata(types=request.method, url=request.url)
    test.put()
    return "403-forbidden"
