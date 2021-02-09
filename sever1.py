from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hfaker11111111'

@app.route('/hallo')
def hallo():
	return str(1+1)

if __name__ == "__main__":
	app.run(debug=True)