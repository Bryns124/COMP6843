from flask import Flask, render_template, make_response, request, redirect, url_for
import sqlite3
import requests

app = Flask(__name__)
conn = sqlite3.connect('database.db')

@app.route('/')
def home():
    return make_response(render_template('home.html'))

@app.route('/user/<name>')
def user(name):
    if name in db:
        return make_response(render_template('user.html', name=name))
    else:
        return make_response(render_template('error.html', message="User not found"), 400)

@app.route('/login')
def login():
    return make_response(501)

@app.route('/profile_picture')
def profile_pic():
    return make_response(501)

@app.route('files/list')
def file_listing():
    return make_response(501)

@app.route('files/<filename>')
def file(filename):
    return make_response(501)

if __name__ == '__main__':
    curr = conn.cursor()
    curr.execute("DROP TABLE IF EXISTS users;")
    curr.execute("CREATE TABLE users (id INT, username TEXT, password TEXT, info TEXT);")
    curr.execute("DROP TABLE IF EXISTS users;") 
    curr.execute("DROP TABLE IF EXISTS users;")
    curr.execute("DROP TABLE IF EXISTS users;")
    