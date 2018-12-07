from flask import request, jsonify
from meep import app
from .core import *
from .utils import *

@app.route('/api/login', methods=["POST"])
def login():
    submitData = request.json;
    username = submitData.get("username")
    password = submitData.get("password")

    return validateUserLogin(username, password) # return either true or false
                                          # if false... try again + give option of creating account as a guest user?

@app.route('/api/register', methods=["post"])
def post():
    submitData = request.json;
    username = submitData.get("username")
    password = submitData.get("password")
    interests = submitData.get("interests")

    return validateRegistration(username, password, interests) #hmm...

@app.route('/api/users', methods=["GET"])
def users():
    returnUsers = []

    for user in allUsers:
        userData = {
            "id" : user._id,
            "name": user._username,
            "type": user._membership
        }
        returnUsers.append(userData)

    return jsonify(returnUsers)

@app.route('/api/documents', methods=["GET"])
def documents():
    # Return list of all public documents
    returnDocs = []

    for doc in allDocuments:
        # Map object properties to a Python dictionary for JSON conversion
        docData = {
            "doc_id" : "",
            "doc_title" : doc._documentName,
            "doc_owner" : doc._owner
        }
        returnDocs.append(docData)

    return jsonify(returnDocs);

@app.route('/api/doc/:doc_id', methods=["GET"])
def get_doc():
    # Retrieve a specific document from the server
    return jsonify("Your document here")

@app.route('/api/doc/:doc_id', methods=["POST"])
def post_doc():
    # Save a specific document to the server
    return jsonify("placeholder")
