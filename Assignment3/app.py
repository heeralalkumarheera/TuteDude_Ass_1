from flask import Flask, jsonify, render_template, request, redirect
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Connection (TuteDude DB)
client = MongoClient("mongodb+srv://heeralalkumarheera_db_user:Heera%401234@campuseventhub.kzgxjc0.mongodb.net/?appName=CampusEventHub")
db = client["TuteDude"]
collection = db["formdata"]

# Question 1 API
@app.route('/api')
def get_data():
    with open('data.json') as file:
        data = json.load(file)
    return jsonify(data)

# Question 2 Form
@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        collection.insert_one({
            "name": name,
            "email": email
        })

        return redirect('/success')

    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/success')
def success():
    return "Data submitted successfully"

# Run App 
app.run(debug=True)