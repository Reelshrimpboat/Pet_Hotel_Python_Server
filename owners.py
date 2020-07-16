#create a post request to enter owners into the database and then
#create a Get request to fetch owners from the database.

from flask import Flask, request, jsonify
app = Flask(__name__)
import psycopg2 # imports psycopg2 for database queries




#write GET request to get owners and print to web page
def owners_get():
    try:
        # connect to database
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="pet_hotel"
        )
        cursor = connection.cursor()

        get_query ='''SELECT * FROM "owners"''' #defines query for GET request

        cursor.execute(get_query) #sends query to the database
        # logs that query has been sent to the database
        print("selecting rows from owners")
        owners = cursor.fetchall()
        return jsonify(owners)  # return data as a JSON string
    
    except (Exception, psycopg2.Error) as error: #error catching
        print("Error while fetching data from PostgreSQL", error) #logs error

    #ending tag executed after everything is done.
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
#End of GET request



def owners_post():  #need to write a way to reccieve owner name, write in a variable to recieve owner name
    # write Post route here
    try:
        owner = request.values #sets owner as incoming JSON object

        # connect to database
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="pet_hotel"
        )
        cursor = connection.cursor()  # create cursor to interact with database

        #post_query = ()
        #post_values = () # post values are equal to owner_name being passed into 
        post_query = '''INSERT INTO "owners" (name) VALUES ('%s');'''
        post_values = (owner["name"])
        print('post query:', post_query, ": post_values:", post_values)  # log to check query and values

        #send query and values to database
        cursor.execute(post_query % post_values)
        connection.commit()  # commits query to database

        #move to next action and return succes message to server
        return ("Record inserted successfully into owners table", 200)
    
    except (Exception, psycopg2.Error) as error: # error catching
        print("Error while fetching data from PostgreSQL", error) #log error


    # ending tag, done, after error
    finally:
        if(connection): # if connection remains open...
            cursor.close()  #close cursor
            connection.close() #closes database
            print("PostgreSQL connection is closed") #logs that connection is closed
#End POST route for owner table

