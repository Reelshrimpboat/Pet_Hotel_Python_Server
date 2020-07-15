from flask import Flask, request, jsonify # imports items from Flask for CRUD functions
app = Flask(__name__) # defines app as flask object
import psycopg2 # imports psycopg2 for database queries

@app.route("/")
def home():
    return "Hello, Flask!"

# GET ROUTE for PET TABLE
@app.route("/pets", methods=['GET'])
def pets_get():
    #  GET occurs here:
    try:
        # connect to database
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="pet_hotel"
        )
        cursor = connection.cursor()  # create cursor to interact with database

        get_query = "select * from pets"  # defines query for GET request

        cursor.execute(get_query)  # sends query to the database
        # logs that query has been sent to database
        print("Selecting rows from pets")

        pets = cursor.fetchall()  # defines list 'pets' as what returns from database
        print("pets: ", pets)  # logs what was defined in pets

        return jsonify(pets)  # returns data as JSON string

    except (Exception, psycopg2.Error) as error:  # error catching
        print("Error while fetching data from PostgreSQL", error)  # logs error

    # ending tag/ to do after error
    finally:
        if(connection):  # if for when connection remains open
            cursor.close()  # closes cursor
            connection.close()  # closes database connection
            # logs that connection is closed
            print("PostgreSQL connection is closed")
# END GET ROUTE for PET TABLE
