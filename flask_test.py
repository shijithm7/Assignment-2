from flask import Flask, render_template
from flask import request, redirect
from interview_qualification_analyser import *



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('intro.html')


@app.route('/signup', methods = ['POST'])
def signup():

    return (final_result())




    

    



if __name__ == '__main__':
        app.run(debug=True)
