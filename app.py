from flask import Flask
app = Flask(__name__)

@app.route('/index',, methods=['GET', 'POST'])
def hello_geek():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run(debug=True)
