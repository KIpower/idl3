from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h2>Jeffri Temis Cueva Fernandez</h2>
    <img src="https://shorturl.at/hlvFM"  width="500" height="600">'


if __name__ == "__main__":
    app.run(debug=True)
