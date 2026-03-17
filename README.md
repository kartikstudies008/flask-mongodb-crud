Flask MongoDB CRUD Application

A simple CRUD (Create, Read, Update, Delete) web application built using Python Flask and MongoDB.
This project demonstrates how to connect Flask with MongoDB and perform database operations through a web interface.

Features

Add new users

View all users

Update user details

Delete users

MongoDB database integration

Simple web interface

Tech Stack

Python

Flask

PyMongo

MongoDB

HTML / JavaScript

Project Structure
flask-mongodb-crud
│
├── app.py
├── templates
│   └── index.html
├── venv
└── README.md
Installation

Clone the repository

git clone https://github.com/YOUR_USERNAME/flask-mongodb-crud.git
cd flask-mongodb-crud

Create virtual environment

python -m venv venv

Activate virtual environment

Windows

venv\Scripts\activate

Install dependencies

pip install flask flask-cors pymongo
Run the Application

Start the Flask server

python app.py

Open your browser and go to

http://127.0.0.1:5000
Database

MongoDB is used as the database.

Database name

testdb

Collection

users
CRUD Operations
Operation	API Endpoint
Create User	POST /users
Get Users	GET /users
Update User	PUT /users/:id
Delete User	DELETE /users/:id
Learning Outcome

Understanding Flask backend development

Connecting Python applications with MongoDB

Implementing CRUD operations

Creating RESTful APIs

Basic frontend and backend integration

Author

Kartik
MCA Student
