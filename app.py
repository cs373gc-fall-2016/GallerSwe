import os

from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/artists')
def artists():
    return app.send_static_file('andywarhol.html')

if __name__ == "__main__":
    app.run()
