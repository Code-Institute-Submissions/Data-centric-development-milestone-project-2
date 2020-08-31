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

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines = mongo.db.cuisine.find()
    return render_template("view_recipe.html", item=the_recipe,cuisine=all_cuisines) 

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html')


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipe
    recipe_dict=request.form.to_dict()
    ingredients=recipe_dict['ingredients_name'].split(',')
    recipe_dict['ingredients_name']=ingredients
    method=recipe_dict['method'].split(',')
    recipe_dict['method']=method
    recipe.insert_one(recipe_dict)
    print(request.form)
    return redirect(url_for('recipe_list'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines = mongo.db.cuisine.find()
    return render_template('editrecipe.html', item=the_recipe,cuisine=all_cuisines)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipe
    recipe.update({'_id': ObjectId(recipe_id)},
    {
        'title': request.form.get('title'),
        'cuisine_name': request.form.get('cuisine_name'),
        'description': request.form.get('description'),
        'type_name': request.form.get('type_name'),
        'image': request.form.get('image')
    })
    return redirect(url_for('recipe_list'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('recipe_list'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
