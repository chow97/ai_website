#!/bin/python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure your Database URI
# For SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
# For PostgreSQL, you would eventually change the URI to something like:
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/mydatabase'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    # Add other fields as necessary

    def __repr__(self):
        return f'<Customer {self.name}>'

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/add_customer', methods=['POST'])
def add_customer():
    name = request.json['name']
    email = request.json['email']
    
    # Check if customer already exists
    if Customer.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists'}), 400

    new_customer = Customer(name=name, email=email)
    db.session.add(new_customer)
    db.session.commit()
    
    return jsonify({'message': 'Customer added successfully'}), 201

@app.route('/customers', methods=['GET'])
def get_customers():
    customers_list = Customer.query.all()
    customers = [{"id": customer.id, "name": customer.name, "email": customer.email} for customer in customers_list]
    
    return jsonify(customers)

if __name__ == '__main__':
    app.run(debug=True)
