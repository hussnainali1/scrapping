import subprocess
from daily_news_Scraping.runScrapping import main;
from scholarship_news.hec_eduvision import main as main2;
from flask import Flask, request, jsonify


app = Flask(__name__)
@app.route('//')
def index():
   main();
   main2();
   return "python server is running and all data is scrapped "
app.run(debug=True, host='localhost', port=5000)