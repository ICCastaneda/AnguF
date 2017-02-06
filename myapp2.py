#!/usr/bin/python
import pdb
import sys
sys.dont_write_bytecode = True
import json
from flask import Flask, session, redirect, url_for, escape, request
from flask import jsonify, send_file
#import CONS
import funcs

tf_port = int(5004)
app = Flask(__name__, static_folder='www', template_folder='www')

# set the secret key.  keep this really secret:
app.secret_key = 'keep_session_in_cokies'


@app.route('/')
def main_index_html():
    # req = request     # debug only
    print 'zzzzzzzzz'
    return send_file("www/templates/pathtable.html")
    #return send_file("www/templates/angp1.html")
    #return send_file("www/templates/index.html")

@app.route('/customers.html', methods=['GET', 'POST'])
def cutomers_table():
    print 'aaaaaaaaa'
    json_customers = funcs.bld_json_customers()
    print json_customers
    sj = jsonify(json_customers)

    return sj
    #return redirect(url_for('index'))

@app.route('/login')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    """
    targil1 flask server, main
    """
    tf_port = int(5004)
    ms1 = "port number is {}".format(tf_port)
    print ms1    # will be converter to use python logging

    app.run(host="0.0.0.0",
            threaded=True,
            debug=True,
            use_reloader=False,
            use_debugger=False,
            port=tf_port)
