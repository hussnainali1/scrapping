import subprocess
import os
from daily_news_Scraping.runScrapping import main
from scholarship_news.hec_eduvision import main as main2
from flask import Flask, request, jsonify
Port = int(os.environ.get("PORT", 9000))

app = Flask(__name__)


@app.route('/')
def index1():
    return "welcome to Newsbuzz-Scrapper     https://newzbuzz-scrapper.herokuapp.com/scrap  for starting scrapping "


@app.route('/scrap1')
def index():
    main()
    return "python server is running and all data is scrapped "


@app.route('/scrap2')
def index2():
    main2()
    return "python server is running and all data is scrapped "


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=Port)
