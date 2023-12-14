# pip install numpy
# pip install scipy
# pip install flask

import numpy as numpy
from scipy.linalg import solve 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def jacobi():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
