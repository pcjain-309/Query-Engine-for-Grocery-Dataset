from flask import Flask, request
from generator import get_answer
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>LLM API</h1>'''

@app.route('/generate', methods=['GET'])
def process_request():
    api = request.args.get('api')
    query = request.args.get('query')

    # Check if both parameters are present
    if query is None or api is None:
        return 'Error: Missing parameters. Please provide both api and query.'

    # Call the processing function
    result = get_answer(api, query)

    # Return the result as a response
    return result

if __name__ == '__main__':
    app.run(debug=True)
