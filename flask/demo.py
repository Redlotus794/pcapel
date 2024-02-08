"""
这是一个 web 应用的例子 
"""
from flask import Flask, jsonify
import logging

app = Flask('my demo')

logging.basicConfig(level=logging.INFO)

@app.route('/<name>')
def hello_world(name):
    logging.info('用户输入: ' + name) 
    return jsonify({'message': 'Hello, World! ' + name})


if __name__ == '__main__':
    app.run(debug=True)