import bs4 as bs
import flask
import requests

from flask import Flask, render_template, redirect, url_for
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
      html = requests.get(url).text
      soup = bs.BeautifulSoup(html, 'html.parser')
      body = soup.find('body')
      all_el= body.findChildren()
      [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
      visible_text = soup.find_all(['h1', 'h2', 'h3', 'a','p', 'img'])
      return render_template("view.html", html=visible_text)

if __name__ == '__main__':
  app.run()
