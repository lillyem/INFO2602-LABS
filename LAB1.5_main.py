import json
from flask import Flask, request, jsonify

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response

@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') # get the parameter from url
  if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: # select only the students with a given meal preference
        result.append(student) # add match student to the result
    return jsonify(result) # return filtered set if parameter is supplied
  return jsonify(data) # return entire dataset if no parameter supplied

@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: # filter out the students without the specified id
      return jsonify(student)
  return f"Student {id} does not exist in the dataset."

@app.route('/stats')
def get_stats():
  chicken = 0
  fish = 0
  vegetarian = 0
  compSciMajor=0
  compSciSpecial=0
  itMajor=0
  itSpecial=0
  
  for student in data:
    if student['pref'] == 'Chicken':
      chicken += 1
    elif student['pref'] == 'Fish':
      fish += 1
    else:
      vegetarian += 1
  for student in data:
    if student['programme']=='Computer Science (Major)':
      compSciMajor+=1
    elif student['programme']=='Computer Science (Special)':
      compSciSpecial+=1
    elif student['programme']=='Information Technology (Major)':
      itMajor+=1
    else: 
      itSpecial+=1
    
  return jsonify({
    'Chicken': chicken,
    'Computer Science (Major)':compSciMajor,
    'Computer Science (Special)':compSciSpecial,
    'Fish': fish,
    'Information Technology (Major)':itMajor,
    'Information Technology (Special)':itSpecial,
    'Vegetable': vegetarian
  })

@app.route('/add/a/b')
def add(a,b):
  result=a+b
  return jsonify(result)

@app.route('/subtract/a/b')
def subtract(a,b):
  result=a-b
  return jsonify(result)

@app.route('/multiply/a/b')
def multiply(a,b):
  result=a*b
  return jsonify(result)
  
@app.route('/divide/a/b')
def divide(a,b):
  result=a/b
  return jsonify(result)


    
app.run(host='0.0.0.0', port=8080, debug=True)