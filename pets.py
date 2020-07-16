from flask import Flask, request, jsonify # imports items from Flask for CRUD functions
app = Flask(__name__) # defines app as flask object
import psycopg2 # imports psycopg2 for database queries

# GET ROUTE for PET TABLE
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






# POST ROUTE for PET TABLE
def pets_post():
    #  POST occurs here:
    try:
        # print(request.values['name'])
        pet = request.values  # sets pet as incoming JSON object

        # connect to database
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="pet_hotel"
        )
        cursor = connection.cursor()  # create cursor to interact with database

        post_query = ()
        post_values = ()

        if pet["checked_in"] == 'true':
            print('pet is checked_in')
            # defines database query
            post_query = '''INSERT INTO "pets" (owner_id, pet, breed, color, checked_in, checked_in_date)
                            VALUES(%s, %s, %s, %s, %s, %s);'''
            # defines converts values from pets into query value input
            post_values = (pet["owner_id"], pet["pet"], pet["breed"],
                           pet["color"], pet["checked_in"], pet["checked_in_date"])
        elif pet["checked_in"] == 'false':
            print('pet is not checked_in')
            # defines database query
            post_query = '''INSERT INTO "pets" (owner_id, pet, breed, color, checked_in)
                            VALUES(%s, %s, %s, %s, %s);'''
            # defines converts values from pets into query value input
            post_values = (pet["owner_id"], pet["pet"], pet["breed"],
                           pet["color"], pet["checked_in"])

        print('post query:', post_query, " : post_values:",
              post_values)  # log to check query and values

        # sends query and values to database
        cursor.execute(post_query, post_values)
        connection.commit()  # commits query to database

        # move to next action and return success message to server
        return ("Record inserted successfully into pets table", 200)

    except (Exception, psycopg2.Error) as error:  # error catching
        print("Error while fetching data from PostgreSQL", error)  # log error

    # ending tag/ to do after error
    finally:
        if(connection):  # if for when connection remains open
            cursor.close()  # closes cursor
            connection.close()  # closes database connection
            # logs that connection is closed
            print("PostgreSQL connection is closed")
# END POST ROUTE for PET TABLE


# PUT ROUTE for PET TABLE, to change checked in status
def pet_check_in():
    #  PUT occurs here:
    try:
        
        check_in = request.values  # sets check_in with values sent from request

        # connect to database
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="pet_hotel"
        )
        cursor = connection.cursor()  # create cursor to interact with database

        post_query = ()
        post_values = ()

        if check_in["checked_in"] == 'true':
            print('pet is checking in')
            # defines database query
            post_query = '''UPDATE pets
                                SET checked_in = false , checked_in_date = %s
                                WHERE id = (%s);'''
            # defines converts values from pets into query value input
            post_values = (check_in["checked_in_date"], check_in["id"])
        elif check_in["checked_in"] == 'false':
            print('pet is checking out')
            # defines database query
            post_query = '''UPDATE pets
                                SET checked_in = false , checked_in_date = null
                                WHERE id = (%s);'''
            # defines converts values from pets into query value input
            post_values = (check_in["id"])

        print('post query:', post_query, " : post_values:",
              post_values)  # log to check query and values

        # sends query and values to database
        cursor.execute(post_query, post_values)
        connection.commit()  # commits query to database

        # move to next action and return success message to server
        return ("Pet's state of checked_in has been changed", 200)

    except (Exception, psycopg2.Error) as error:  # error catching
        print("Error while fetching data from PostgreSQL", error)  # log error

    # ending tag/ to do after error
    finally:
        if(connection):  # if for when connection remains open
            cursor.close()  # closes cursor
            connection.close()  # closes database connection
            # logs that connection is closed
            print("PostgreSQL connection is closed")
# END PUT ROUTE for PET TABLE
