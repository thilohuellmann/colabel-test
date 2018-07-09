#!/usr/bin/env python
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging

app = Flask(__name__)

# Index
@app.route('/', methods=['GET', 'POST'])
def index():
        return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = os.environ['APP_SECRET_KEY']
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
