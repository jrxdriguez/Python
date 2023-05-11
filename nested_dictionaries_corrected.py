#1 update values
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

x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0]= 'Andres'
print(sports_directory)


#2 iterate through
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for names in students:
        for key, val in names.items():
            print(f'Key = {key}')
            print(f'Value = {val}')

print(iterateDictionary(students))

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)


#3 get values from
def iterateDictionary2(first_name, students):
    for names in students:
        print(names['first_name'])

print(iterateDictionary2('first_name', students))

def iterateDictionary2(last_name, students):
    for names in students:
        print(names['last_name'])

print(iterateDictionary2('last_name', students))


#4 iterate through a dict w list values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, val in some_dict.items():
        print(f"{len(val)} {key.upper()}")
        for item in val:
            print(item)

print(printInfo(dojo))


