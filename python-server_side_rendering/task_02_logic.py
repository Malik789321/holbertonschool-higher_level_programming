#!/usr/bin/python3
"""
Flask app with dynamic template rendering.
"""

from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)

    return render_template(
        'items.html',
        items=data.get('items', [])
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
