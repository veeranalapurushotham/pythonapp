from flask import Flask
from utils import greet

app = Flask(__name__)

@app.route('/')
def hello():
    return greet()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
