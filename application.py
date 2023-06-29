from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

#Setting up Flask
app = Flask(__name__)

#Configuring the databse
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # Update with the correct relative or absolute path

#Setting up SQLAlchemy. It allow us to access the database
db = SQLAlchemy(app)

#Creating a class to store data from the db
#To create a column we use db.Column

class Drink (db.Model):
    id = db.Column(db.Integer, primary_key=True) # Creates a column Integer used as a primary key. 
    name = db.Column(db.String(80), unique=True, nullable=False) # Creates a column string with max 80, unique values only and no nulls
    description = db.Column(db.String(120))
    
#We also must create a representation method so we can get the attributes of the drinks
    def __repr__(self):
       return f"{self.id} - {self.name} - {self.description}"

#Make a simple route in the endpoint
@app.route('/')

#define a method we want to hit when someone visits this roude
def index():
    return 'Hello! I am creating my own KPI now! This is awesome!!!!!!'

#Creating a route for drinks
@app.route('/drinks')
def get_drinks():
   drinks = Drink.query.all()
   #Since the output of Drink.query.all is not interactable, we create an empty list, look in each of hte drinks and pass the values to a dictionary.
   #At the end we append the values to the emtpy list we created called output
   output = []

   for drink in drinks:
        drink_data = {'id': drink.id, 'name': drink.name, 'description':drink.description}
        output.append(drink_data)
   
   return {"drinks" : output}

#The < and >  signs let us define a parameter in the route. 
@app.route('/drinks/<id>')
def get_drink(id):
    #The get_or_404 is the method. We can check documentation of flask on about more detail on it
    drink = Drink.query.get_or_404(id)
    #Dictionary are serializable. We don't need jsonify in here but sometimes we might need it if we are not working with a dictionary
    return {"name":drink.name, "description":drink.description}

#We are now creating a way to include more drinks. We are defining. We could use the method in all one definition and check if they want to add
#or if they want to query all drinks
@app.route('/drinks', methods=['POST'])
def add_drink():
    #the request.json allow us to get the data that users are sending on our way
    drink = Drink(name = request.json['name'], description = request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id}

#We are not creating a way to delete a drink from the system. This will get the id from the user and will then get the structure of the drink
#based on the id passed from the user form the database. We then use the delete method from the session as well as the commit to pass the changes
#to the data base. We also must handle errors in case the user does not pass any argument
@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error" : "not found"}
    db.session.delete(drink)
    db.session.commit()    
    return {"message": "yeet@!"}

