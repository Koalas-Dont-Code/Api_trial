from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load the data from the JSON file
with open(r'C:\Users\Shrinjita\Downloads\q-vercel-python.json', 'r') as file:
    marks_data = json.load(file)


@app.route('/api', methods=['GET'])  # Fixed the method to GET
def get_marks():
    # Get the list of names from the query parameters
    names = request.args.getlist('name')

    # Retrieve the marks for each name, or return "Not Found" if the name is not in the data
    result = {"marks": [marks_data.get(name, "Not Found") for name in names]}

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
