from flask import Flask, render_template, request
from textblob import TextBlob
import re

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def index():
    if request.method == 'POST': 
        url = request.form['url']
        remove = url.replace(('-'),' ')
        change = r"https?://(www\.)?"
        text = re.sub(change, ' ', remove)
        sentimen = TextBlob(text).sentiment.polarity
        print (sentimen)
        
        if sentimen < 0:
            analy = "Bad"
        elif sentimen == 0:
            analy = "Netral"
        else:
            analy = "Good"
        return render_template('index.html', url=url, sentimen=sentimen, analy=analy)
    return render_template('home.html')
if __name__ == "__main__":
    app.run(debug=True)