from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/student-details')
def student():
    return jsonify({
        "name": "Pragatheesh M",
        "roll": "2023BCS0008",
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)