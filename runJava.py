from flask import Flask
from flask import render_template
import os


app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/run1')
def run1():
    executeI1="java -jar tessetactCode.jar"
    outputI1=os.system(executeI1)
    return render_template('done.html',outputI=outputI1)

@app.route('/run2')
def run2():
    executeI2="java -jar schedulerCode.jar"
    outputI2=os.system(executeI2)
    return render_template('done.html',outputI=outputI2)