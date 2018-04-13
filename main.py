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
  #if users browse here by themselves, get them back to the homepage
  if flask.request.method == 'GET':
    return redirect('/')
  else:
    url = flask.request.values.get('url')
    #not sure why the negation here works, but it just does, so I'll leave it :)
    if not url.find("https://") or not url.find("http://"):
      return render_template("view.html", url=url)
    else :
      url = "https://" + url
      return render_template("view.html", url=url)

if __name__ == '__main__':
  app.run()
