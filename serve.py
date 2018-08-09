"""
serve module that uses Flask to route functions to their
designated HTML pages
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    """
    Serves as the home page for this simple web application
    """
    message = "The Golf Shop"
    return render_template('index.html', message=message)

@app.route("/low-handicap")
def low_handicap():
    """
    Serves as the HTMl page for low handicap golf club recommendations
    , will run in browser with /low-handicap endpoint
    """
    message = "Low Handicap Recommendations"
    return render_template('low_handicap.html', message=message)

@app.route("/mid-handicap")
def mid_handicap():
    """
    serves as the HTML page for mid handicap golf club recommendations
    , will run in browser with /mid-handicap endpoint
    """
    message = "Mid Handicap Recommendations"
    return render_template('mid_handicap.html', message=message)

@app.route("/high-handicap")
def high_handicap():
    """
    Serves as the HTML page for high handicap golf club recommendations
    , will run in browser with high-handicap endpoint
    """
    message = "High Handicap Recommendations"
    return render_template('high_handicap.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)
