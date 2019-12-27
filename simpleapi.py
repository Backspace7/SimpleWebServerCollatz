import flask
from flask import request, jsonify
import CollatzSequence 

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Test Web Service</h1>
<p>A prototype Web service without database for Sixbell</p>'''

@app.route('/resources/collatz', methods=['GET'])
def api_collatz():
	try: 
		if request.args['num'] == '' or  request.args['num'] ==' ' :
			return jsonify("Value is not a number please enter a number")
		else:
			try:
				num = int(request.args['num'])
			except:
				return jsonify("Value is not a number please enter a number")
	except:
		return jsonify("No number field provided. Please specify a number field.")

	if int(request.args['num']) == 0 or int(request.args['num']) <= -1:
		return jsonify("Number is not valid, please enter a positive divisible number")

	results = CollatzSequence.collatz_sequence(num)
	return jsonify(results)

app.run()
