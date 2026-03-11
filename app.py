from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/produk")
def produk():

    data = [
        {"nama": "mie instan", "harga": 3000},
        {"nama": "kopi", "harga": 2000}
    ]

    return jsonify(data)

app.run(debug=True)