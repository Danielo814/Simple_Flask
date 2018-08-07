"""
imports Flask class from flask module
to route pieces of HTML to their designated
endpoints
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the homepage'

@app.route('/about')
def about():
    return 'About section'

if __name__ == "__main__":
    app.run()
