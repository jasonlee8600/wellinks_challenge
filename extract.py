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
        list = [lname, fname, email, address]
        final = ", ".join(list)
        answer.append(final)



with open('users.json', 'r') as file2:
	json_load = json.load(file2)

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
    list1 = [stnumber, stname]
    # joining elements that don't need commas between them
    address = " ".join(list1)
    

    city = user['location']['city']

    state = user['location']['state']
    # cast zip (int) as string
    zip = str(user['location']['postcode'])
    list2 = [state, zip]
    # joining elements that don't need commas between them
    state_zip = " ".join(list2)

    list3 = [lname, fname, email, address, city, state_zip]
    # combining all the elements with commas between
    final = ", ".join(list3)
    answer.append(final)

# sort the data alphabetically by last name
# did not have time to include alphabetizing by first name if some people have same last name
answer.sort()

# print data
for x in answer:
    print(x)
