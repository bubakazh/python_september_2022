
# 1 UPDATE VALUES IN DICTIONARIES AND LISTS

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15        # LIST OF LISTS. IN LIST x, VALUE @ 2ND INDEX IS LIST [10,8,9], AND IN THAT LIST, VALUE IN 1ST INDEX IS 10, CHANGED TO 15.
print(x)

students[0]['last_name'] = 'Bryant'     # INITIALLY HAD students['last_name'] WHICH DIDN'T WORK, BECAUSE THE DICTIONARY IS IN A LIST. 
print(students[0]['last_name'])         # REFERENCE THE VALUE IN THE LIST, THEN THE KEY IN THE DICTIONARY.

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0])

z[0]['y'] = 30
print(z[0]['y'])


# 2 ITERATE THROUGH A LIST OF DICTIONARIES

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    # for i in students:
    #     print("First name is {} and last name is {}.".format(i['first_name'], i['last_name']))
    for s in students:
        print(f"first name is {s['first_name']}, and last name is {s['last_name']}")
    # for stud in range(len(students)):
    #     print("First name: " + students[stud]['first_name'] + ", Last name: " + students[stud]['last_name'])
iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# 3 GET VALUES FROM A LIST OF DICTIONARIES

def iterateDictionary2(key_name, some_list):
    for f in students:
        print(f['first_name'])
iterateDictionary2('first_name',students)

def iterateDictionary3(quay_name, other_list):
    for L in students:
        print(L['last_name'])
iterateDictionary3('last_name',students)

# 4 ITERATE THROUGH DICTIONARY WITH LIST VALUES

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for key in dojo:
        print(key, len(dojo[key]))
        for item in dojo[key]:
            print(item)
printInfo(dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
