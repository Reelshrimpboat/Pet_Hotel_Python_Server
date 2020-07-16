from flask import Flask, request, jsonify # imports items from Flask for CRUD functions
app = Flask(__name__) # defines app as flask object
import psycopg2 # imports psycopg2 for database queries
import pets

@app.route("/")
def home():
    return "Hello, Flask!"

# GET/POST ROUTE for PET TABLE
@app.route("/pets", methods=['GET', 'POST'])
def pets_route() :
    if request.method == 'GET':  # checks method to see if GET
        return pets.pets_get()
    elif request.method == 'POST':  # checks method to see if POST
        return pets.pets_post()


@app.route('/pets', methods=[ 'PUT', 'DELETE'])
def pet_route():
    if request.method == 'PUT':  # checks method to see if PUT   
        return pets.pet_check_in()
