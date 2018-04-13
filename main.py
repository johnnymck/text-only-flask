import bs4 as bs
import flask

from urllib.request import urlopen
from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/view', methods=['GET', 'POST'])
def view():
  if flask.request.method == 'GET':
    return redirect('/')
  else:
    url = flask.request.values.get('url')
    return render_template("view.html", url=url)

if __name__ == '__main__':
  app.run()
