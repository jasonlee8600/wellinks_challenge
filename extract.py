# UPDATED SOLUTION AFTER CODING REVIEW EXERCISE

import csv
import json
import os

# initialize array to store data
answer = []

# go into subdirectory with data files
path = os.getcwd() + '/data'
os.chdir(path)

with open('erp_users.csv', 'r') as file:

    reader = csv.reader(file)

    for row in reader:
        # skip header example row
        if row[0] == "email":
            continue
        # query for needed elements using respective indexes
        lname = row[2]
        fname = row[3]
        email = row[0]
        address = row[4]
        final = [lname, fname, email, address]
        output = ", ".join(final)
        answer.append(output)



with open('users.json', 'r') as file:

	json_load = json.load(file)

    # get root out of way
data = json_load['results']

    # query for each element needed
for user in data:
    lname = user['name']['last']
    fname = user['name']['first']
    email = user['email']

    # cast street number (int) as string
    stnumber = str(user['location']['street']['number'])
    stname = user['location']['street']['name']
    address = [stnumber, stname]
    # joining elements that don't need commas between them
    new_address = " ".join(address)
        

    city = user['location']['city']

    state = user['location']['state']
    # cast zip (int) as string
    zip = str(user['location']['postcode'])
    state_zip = [state, zip]
    # joining elements that don't need commas between them
    new_state_zip = " ".join(state_zip)

    final = [lname, fname, email, new_address, city, new_state_zip]
    # combining all the elements with commas between
    output = ", ".join(final)
    answer.append(output)



# third data file "more_data.csv"

with open('more_data.csv', 'r') as file:

    reader = csv.reader(file)

    for row in reader:
        # skip header example row
        if row[0] == "name":
            continue
        # change name string element to exclude middle initial
        name = row[0][(0):(-3)] # first and last name
        email = row[2]
        
        address = row[3]
        if (not(address[0].isdigit())):
            index = 0
            for char in address:
                if not(char.isdigit()):
                    index += 1
                else:
                    break
            address = address[index:len(address)]

        state = row[6]
        zip = row[4]
        state_zip = [state, zip]
        # joining elements that don't need commas between them
        new_state_zip = " ".join(state_zip)

        final = [name, email, address, new_state_zip]
        output = ", ".join(final)
        answer.append(output)


# sort the data alphabetically by last name
answer.sort()

# print data
for x in answer:
    print(x)
