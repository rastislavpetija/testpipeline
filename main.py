from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
	message = os.getenv('MESSAGE', default='Hello, World!')
	return render_template('index.html', message=message)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
