from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SAGEMAKER_ENDPOINT = 'http://localhost:5005/webhooks/rest/webhook'

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_message = data.get('message')
    print(f"User message: {user_message}")
    # Call the Rasa endpoint
    response = requests.post(SAGEMAKER_ENDPOINT, json={'message': user_message})
    response_json = response.json()
    print(f"Bot response: {response_json}")
    return jsonify(response_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
