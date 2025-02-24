from flask import Flask, render_template
import pandas as pd

df = pd.read_csv('food_data.csv')

app = Flask(__name__)


@app.route("/")
def index():
    
    return render_template('index.html')


@app.route("/store_detail")
def store_detail():
    return render_template('store_detail.html')

if __name__=='__main__':
    app.run(debug=True, port=8000)