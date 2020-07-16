import psycopg2 # imports psycopg2 for database queries
import psycopg2.extras  # imports psycopg2.extras for advanced database queries
from datetime import datetime # imports datetime to get date and time
from flask import Flask, request, jsonify # imports items from Flask for CRUD functions
app = Flask(__name__)  # defines app as flask object





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
        # create cursor to interact with database
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        get_query = '''SELECT pets.id, pets.owner_id, pets.breed, pets.checked_in, pets.checked_in_date, pets.color, pets.pet, owners.name AS owner_name
                            FROM pets
                            JOIN owners ON pets.owner_id = owners.id;'''  # defines query for GET request

        cursor.execute(get_query)  # sends query to the database
        # logs that query has been sent to database
        print("Selecting rows from pets")

        pets = cursor.fetchall()  # defines list 'pets' as what returns from database
        print("pets: ", pets)  # logs what was defined in pets

        pets_list = [] # defines list of pets to be appended to
        for row in pets: # loop that inserts pets as dictionaries into pets_list
	        pets_list.append(
	            {"id": row["id"], "owner_id": row["owner_id"], "owner_name": row["owner_name"], "pet": row["pet"], "breed": row["breed"], "color": row["color"], "checked_in": row["checked_in"], "checked_in_date": row["checked_in_date"]})

        print(pets_list)

        # return jsonify(pets)  # returns data as JSON string
        return jsonify(pets_list)  # returns data as JSON string

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






###################################################################################################################




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

        if pet["checked_in"] == 'true': # checks if pet is checked_in when entered into system
            print('pet is checked_in')
            checked_in_date = datetime.today().strftime('%Y-%m-%d')  # gets date for today
            # defines database query
            post_query = '''INSERT INTO "pets" (owner_id, pet, breed, color, checked_in, checked_in_date)
                            VALUES(%s, %s, %s, %s, %s, %s);'''
            # defines converts values from pets into query value input
            post_values = (pet["owner_id"], pet["pet"], pet["breed"],
                           pet["color"], pet["checked_in"], checked_in_date)
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
        return ("Pet inserted successfully into pets table", 200)

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




###################################################################################################################




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

        put_query = ()
        put_values = ()

        checked_in_date = datetime.today().strftime('%Y-%m-%d') # gets date for today

        if check_in["checked_in"] == 'true':
            print('pet is checking in')
            # defines database query
            put_query = '''UPDATE pets
                                SET checked_in = true , checked_in_date = %s
                                WHERE id = (%s);'''
            # defines converts values from pets into query value input
            put_values = (checked_in_date, check_in["id"])
        elif check_in["checked_in"] == 'false':
            print('pet is checking out')
            # defines database query
            put_query = '''UPDATE pets
                                SET checked_in = false , checked_in_date = null
                                WHERE id = (%s);'''
            # defines converts values from pets into query value input
            put_values = (check_in["id"])

        print('put query:', put_query, " : put_values:",
              put_values)  # log to check query and values

        # sends query and values to database
        cursor.execute(put_query, put_values)
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




###################################################################################################################




# DELETE ROUTE for PET TABLE, to change checked in status
def pet_delete():
    #  DELETE occurs here:
    try:

        delete = request.values  # sets delete with values sent from request

        # connect to database
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="pet_hotel"
        )
        cursor = connection.cursor()  # create cursor to interact with database


        # defines database query
        delete_query = ''' DELETE FROM pets
                                WHERE id = %s;'''
        # defines converts values from pets into query value input
        delete_values = (delete["id"])

        print('delete query:', delete_query, " : delete_values:",
              delete_values)  # log to check query and values

        # sends query and values to database
        cursor.execute(delete_query, delete_values)
        connection.commit()  # commits query to database

        # move to next action and return success message to server
        return ("Pet has been removed from database", 200)

    except (Exception, psycopg2.Error) as error:  # error catching
        print("Error while fetching data from PostgreSQL", error)  # log error

    # ending tag/ to do after error
    finally:
        if(connection):  # if for when connection remains open
            cursor.close()  # closes cursor
            connection.close()  # closes database connection
            # logs that connection is closed
            print("PostgreSQL connection is closed")
# END DELTE ROUTE for PET TABLE
