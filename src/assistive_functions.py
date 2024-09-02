import hashlib
import firebase_admin
from dotenv import dotenv_values
from firebase_admin import credentials,firestore

h = hashlib.sha3_512()
config = dotenv_values(".env")
backend_salt = config["SALT_TOKEN"]
validating_json_path = "./cyberyouth-fire-1.json"
collection_name = 'hash-storage'

"""
    FIREBASE TIME
"""

cred = credentials.Certificate(validating_json_path)

firebase_admin.initialize_app(cred)
db = firestore.client()

def cyberyouth_get_hash(company_email:str, client_email:str):

    new_word = backend_salt + company_email + client_email
    new_word = new_word.encode()
    h.update(new_word)
    my_new_hash = str(h.hexdigest())

    return my_new_hash

def cyberyouth_upload_token(hash:str, client_token:str=None): 
    
    doc_ref = db.collection(collection_name).document(hash) #COLLECTION NAME NEEDS TO BE THE ACTUAL COLLECTION NAME, NOT THE DATABASE NAME!!!
    doc_ref.set({
        'token': client_token
    })

    return client_token

def cyberyouth_get_token(hash:str):

    doc_ref = db.collection(collection_name).document(hash)
    doc = doc_ref.get()

    if doc.exists:
        # Return the token from the document
        return doc.to_dict().get('token')
    else:
        return None
