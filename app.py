import os

from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/books')
def books():
    return "This is the books page"

if __name__ == "__main__":
    app.run()
