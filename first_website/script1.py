'''
The Flask class contains all the prototypes needed to
build webapps with Python.
'''
from flask import Flask

# Instantiating the Flask class
app = Flask(__name__)

@app.route('/')
def home():
    return "Website home page content goes here!"

@app.route('/about/')
def about():
    return "Website about page content goes here!"

if __name__ == "__main__":
    app.run(debug = True)
