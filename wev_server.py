from flask import  Flask, render_template
from templates import final_v21 as stock

app = Flask(__name__)
"""
@app.route('/')
def hello_world():
    return  'Hello Green Serve'
"""


@app.route('/')
def main():
    return render_template('index.html')

@app.route("/game1")
def hello():
    return render_template("test.html")

@app.route("/func0")
def func0():
    v19 = stock()
    v19.reserve_stock()


if __name__ == '__main__':
    app.run()