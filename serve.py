from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    message = "The Golf Shop"
    return render_template('index.html', message=message)

@app.route("/low-handicap")
def low_handicap():
    message = "Low Handicap Recommendations"
    return render_template('low_handicap.html', message=message)

@app.route("/mid-handicap")
def mid_handicap():
    message = "Mid Handicap Recommendations"
    return render_template('mid_handicap.html', message=message)

@app.route("/high-handicap")
def high_handicap():
    message = "High Handicap Recommendations"
    return render_template('high_handicap.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)
