from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from dotenv import dotenv_values
config = dotenv_values(".env")

from assistive_functions import *

cross_origin() #Always goes before the decorator
@app.route("/gethash/", methods=["POST"])
def get_hash():

    data = request.get_json()
    # Extract company_email and client_email from the JSON data
    company_email = data.get('company_email')
    client_email = data.get('client_email')

    # Check if both company_email and client_email are provided
    if not company_email or not client_email:
        return jsonify({"error": "company_email and client_email are required"})
    
    return cyberyouth_get_hash(company_email, client_email) # THIS RETURNS A HASH

cross_origin()
@app.route("/upload/", methods=["POST"])
def upload_token(): 

    #Extract JSON data from the request
    data = request.get_json()

    # Extract 'hash' and 'client_token' from the JSON data
    hash = data.get('hash')
    client_token = data.get('client_token')

    # Validate the presence of 'hash'
    if not hash:
        return jsonify({"error": "hash is required"}), 400
    
    return cyberyouth_upload_token(hash, client_token)

@app.route("/gettoken/", methods=["POST"])
def get_token():

    data = request.get_json()
    hash = data.get("hash")
    
    if not hash:
        return jsonify({"error": "hash is required"}), 400
    
    return cyberyouth_get_token(hash)

if __name__ == "__main__":
    app.run(debug=True)
