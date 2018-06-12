import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify

# db configuration
DATABASE = 'pythonchitter.db'
DEBUG = True
SECRET_KEY = 'python'
USERNAME = 'admin'
PASSWORD = 'password'

# create and initialise app
app = Flask(__name__)
app.config.from_object(__name__)

if __name__ == '__main__':
    app.run()
