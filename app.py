from flask import Flask,url_for,render_template,request
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
import re
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


app=Flask(__name__)



@app.route("/",methods=['GET','POST'])
def home():
    if request.method=="GET":
        return render_template("home.html")
    else:
        input_text=request.form['user_input'] 
        return render_template("home.html",ans=input_text)


if __name__=="__main__":
    app.run(debug=True)