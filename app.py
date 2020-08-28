import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://root1:Ranger12@myfirstcluster.xtvot.mongodb.net/cookbook?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')

@app.route('/recipe_list')
def recipe_list():
    return render_template("recipe_list.html", recipe=mongo.db.recipe.find())

@app.route('/view_recipe')
def view_recipe():
    return render_template("view_recipe.html", recipe=mongo.db.recipe.find())   

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
