from flask import Flask, render_template, request, url_for, redirect
import pickle
import numpy as np
import pandas as pd
# import Health_predict as hp

# pd.options.mode.chained_assignment = None
# encoded_cols = hp.encoded_cols
# encoder = hp.encoder
# numeric_cols = hp.numeric_cols
# categorical_cols = hp.categorical_cols
# minscaler = hp.minscaler


app = Flask(__name__)

# model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("index.html")
    # return 'Hello, World!'


@app.route('/analysis')
def new_world():
    return render_template("analysis.html")


if __name__ == "__main__" :
    app.run(debug=True)
