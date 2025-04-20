from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Initialize Gemini
genai.configure(api_key="AIzaSyDKy22Lnzza17VJGdZdqwBqVFyzLEmmgUw")
model = genai.GenerativeModel("gemini-1.5-pro")

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    user_input = data.get('user_input')

    try:
        response = model.generate_content(user_input)
        text_response = response.text
        return jsonify({"response": text_response})
    except Exception as e:
        print("Error:", e)
        return jsonify({"response": "Sorry, something went wrong."}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
