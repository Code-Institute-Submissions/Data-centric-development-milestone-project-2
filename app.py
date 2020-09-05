import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://root1:Ranger12@myfirstcluster.xtvot.mongodb.net/cookbook?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search_recipe')
def search_recipe():
    return render_template("search_recipe.html")

@app.route('/get_recipe',methods=['POST','GET'])
def get_recipe():
        query = request.form.get("query")
        results = mongo.db.recipe.find({
        '$or': [
            {'title': query},
            {'ingredient': query},
            {'type_name': query},
            {'cuisine_name': query}
            ]
        })
        print(results)
        return render_template('recipe_list.html', query=query, recipe=results)


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
    ingredients = request.form.getlist('ingredient')
    recipe_dict['ingredients']=ingredients
    method = request.form.getlist('step')
    recipe_dict['method']=method
    print(ingredients)
    print(method)
    print(recipe_dict)
    print("inside insertrecipe app.py")
    recipe.insert_one(recipe_dict)
    return redirect(url_for('recipe_list'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines = mongo.db.cuisine.find()
    return render_template('editrecipe.html', item=the_recipe,cuisine=all_cuisines)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipe
    recipe_dict=request.form.to_dict()
    ingredients = request.form.getlist('ingredient')
    recipe_dict['ingredients']=ingredients
    method = request.form.getlist('step')
    recipe_dict['method']=method
    recipe.update({'_id': ObjectId(recipe_id)},
    {
        'title': request.form.get('title'),
        'cuisine_name': request.form.get('cuisine_name'),
        'description': request.form.get('description'),
        'type_name': request.form.get('type_name'),
        'image': request.form.get('image'),
        'ingredients': request.form.getlist('ingredient'),
        'method': request.form.getlist('step')
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
