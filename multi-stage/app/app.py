import sys
import flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        "python_version": sys.version.split()[0],
        "flask_version": flask.__version__
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
