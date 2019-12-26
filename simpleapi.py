import flask
from flask import request, jsonify
import CollatzSequence 

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Test Web Service</h1>
<p>A prototype Web service without database for Cyberlink</p>'''


@app.route('/resources/collatz', methods=['GET'])
def api_collatz():
    if 'num' in request.args:
    	if request.args['num'] == '' or  request.args['num'] ==' ' :
    		return jsonify("not number provided, please entire a number")
    	else:
    		try:
        		num = int(request.args['num'])
        	except:
        		return jsonify("not number provided, please entire a number")
    else:
        return jsonify("Error  No number field provided. Please specify a number field.")

    if int(request.args['num']) == 0 :
    	return jsonify("Error Not valid number field provided. Please specify an entire number.")

    results = CollatzSequence.collatz_sequence(num)
    return jsonify(results)

app.run()
