from flask import Flask, request, jsonify # imports items from Flask for CRUD functions
app = Flask(__name__) # defines app as flask object
import psycopg2 # imports psycopg2 for database queries
import pets

@app.route("/")
def home():
    return "Hello, Flask!"

# GET/POST/PUT/DELETE ROUTE for PET TABLE
@app.route("/pets", methods=['GET', 'POST', 'PUT', 'DELETE'])
def pets_route() :
    if request.method == 'GET':  # checks method to see if GET
        return pets.pets_get()
    elif request.method == 'POST':  # checks method to see if POST
        return pets.pets_post()
    elif request.method == 'PUT':  # checks method to see if PUT
        return pets.pet_check_in()
    elif request.method == 'DELETE':  # checks method to see if DELETE
        return pets.pet_delete()


# @app.route('/pets/<int:index>', methods=['PUT', 'DELETE'])
# def pet_route():
#     if request.method == 'PUT':  # checks method to see if PUT   
#         return pets.pet_check_in()
