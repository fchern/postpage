from flask import Flask
import pandas as pd
from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def show_summary_page():
    return 'this is the summary page for {0}'.format(datetime.datetime.today())


@app.route('/<content>/<year>/<month>/<date>')
def switch_by_content(content, year, month, date):
    if content == 'prod':
        html_data = pd.read_csv('/home/cheng/Downloads/biostats.csv').to_html()
        content = 'this is really really funny'
        funny_png_filename = 'prod/2018/10/19/funny.png'
        return render_template('postprod.html', **locals())


if __name__ == '__main__':
    app.run()
