from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Student marks data
MARKS_DATA = [{"name":"mYDM","marks":81},{"name":"2","marks":3},{"name":"A6yiGBVs2v","marks":30},{"name":"R98Q","marks":60},{"name":"4pYnMN","marks":77},{"name":"6","marks":84},{"name":"6Z4","marks":77},{"name":"e","marks":18},{"name":"5Lku5","marks":66},{"name":"D6riHr","marks":35},{"name":"JeYEPh","marks":86},{"name":"S0LNm7gY75","marks":81},{"name":"iEgcPq0Dth","marks":90},{"name":"ClrtYape","marks":29},{"name":"rTZnkWeq","marks":76},{"name":"Bz0k5bYwaF","marks":84},{"name":"eI","marks":91},{"name":"Y08EYw","marks":74},{"name":"lZmN","marks":13},{"name":"iOTdDrF2","marks":32},{"name":"9IzjO8O","marks":57},{"name":"e","marks":13},{"name":"tf","marks":70},{"name":"Vpokvj","marks":10},{"name":"DIYtiny2H","marks":16},{"name":"YwSl1T9","marks":11},{"name":"0FTM7k7uGO","marks":60},{"name":"MwZ4pM","marks":67},{"name":"8ei4","marks":71},{"name":"9SM4JNgWpp","marks":12},{"name":"Cd","marks":39},{"name":"9PAavQSF","marks":8},{"name":"Z2agGorbmA","marks":71},{"name":"2F","marks":92},{"name":"1uRVQc4Ty","marks":64},{"name":"ygRKXYo","marks":69},{"name":"XSU2","marks":45},{"name":"14SHaYuoB","marks":3},{"name":"HPZqLk4SSF","marks":98},{"name":"l1ZTO0r8F","marks":17},{"name":"eLQll","marks":95},{"name":"Kvlusr","marks":98},{"name":"pzciiT69g","marks":72},{"name":"ao5TeK","marks":44},{"name":"1D65","marks":40},{"name":"GHVb0q","marks":16},{"name":"0","marks":14},{"name":"hP1nRZ","marks":62},{"name":"4AMJN3OD","marks":53},{"name":"zrG","marks":13},{"name":"E6lIor","marks":1},{"name":"Dr8yf","marks":39},{"name":"J0VaUCi1","marks":34},{"name":"JvKxLc","marks":25},{"name":"DRNXHb7","marks":0},{"name":"v","marks":93},{"name":"jK8pLNdYdg","marks":55},{"name":"1lP6wR","marks":39},{"name":"iHYd7QDF5l","marks":17},{"name":"ao","marks":12},{"name":"RV","marks":44},{"name":"5","marks":77},{"name":"Tdi3h43","marks":8},{"name":"cE6dBHkgNw","marks":67},{"name":"rRX","marks":48},{"name":"xrQ","marks":59},{"name":"2","marks":79},{"name":"X","marks":2},{"name":"t4IwJ6","marks":76},{"name":"NhkTHJH6","marks":10},{"name":"DOt","marks":31},{"name":"dw4ZkSK88","marks":95},{"name":"qb6","marks":24},{"name":"EFJ","marks":12},{"name":"K3uh0RDEg","marks":97},{"name":"tXNFgM","marks":49},{"name":"o","marks":31},{"name":"ohZQV9707o","marks":0},{"name":"5smD2","marks":79},{"name":"1s3AzP52us","marks":58},{"name":"CGr2sIy8Qk","marks":89},{"name":"jB6JFDy7Fy","marks":31},{"name":"7ov","marks":6},{"name":"5DtcsC","marks":17},{"name":"F2U","marks":20},{"name":"XO6","marks":33},{"name":"QD7lP6DEWQ","marks":77},{"name":"Y7hd84ke","marks":51},{"name":"w","marks":3},{"name":"3KjkIMZg0g","marks":44},{"name":"omr4T2rz","marks":55},{"name":"EzY","marks":71},{"name":"ywFHd","marks":30},{"name":"UzVE","marks":76},{"name":"J0","marks":37},{"name":"eSO6ok7gg","marks":24},{"name":"PTk","marks":6},{"name":"Sv8ED0","marks":87},{"name":"Pgv0","marks":22},{"name":"g","marks":46}]

@app.route('/api', methods=['GET'])
def get_marks():
    # Get all name parameters from the query string
    names = request.args.getlist('name')
    
    # Find marks for requested names
    marks = []
    for name in names:
        # Find student with matching name
        for student in MARKS_DATA:
            if student['name'] == name:
                marks.append(student['marks'])
                break
        else:
            # If student not found, append None or 0
            marks.append(0)
    
    return jsonify({'marks': marks})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
