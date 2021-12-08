from flask import Flask, render_template, request
from werkzeug.utils import redirect
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                         authSource="admin")
    db = client["skills"]
    return db

@app.route("/", methods=['GET', 'POST'])
def index():
    db = get_db()

    all_skills = db.skills.find({})

    if request.method == 'POST':
        if request.form.get('Add') == 'Add':
                db.skills.insert_one({"name": request.form['name'], "category": request.form['category'], "date": request.form['date'], "description": request.form['description'], "icon": request.form['icon']})
                return render_template("index.html", skills=all_skills) 
        else:
            return render_template("index.html", skills=all_skills)
    elif request.method == 'GET':
        return render_template("index.html", skills=all_skills)

@app.route("/newform", methods=['GET'])
def newform():
    if request.method == 'GET':
        return render_template("newform.html")

@app.route("/editform", methods=['GET'])
def editform():
    if request.method == 'GET':
        return render_template("editform.html")

@app.route('/skills/<path:path>', methods=['GET', 'POST'])
def skill(path):
    db = get_db()

    found_skill = db.skills.find_one({"name": path})

    if request.method == 'GET':
            return render_template("skill.html", skill=found_skill)
    if request.method == 'POST':
        if request.form.get('Delete') == 'Delete':
            db.skills.delete_one({"name": path})
            return redirect("/")


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')