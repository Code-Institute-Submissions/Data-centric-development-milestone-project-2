import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from mongoengine import StringField,ListField,URLField,connect,Document
from mongoengine.queryset.visitor import Q as MQ
from werkzeug.exceptions import InternalServerError,HTTPException


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = ('mongodb+srv://root1:Ranger12@myfirstcluster.xtvot.mongodb.net/' +
                          'cookbook?retryWrites=true&w=majority')

mongo = PyMongo(app)
connect(db='cookbook', host ='mongodb+srv://root1:Ranger12@myfirstcluster.xtvot.mongodb.net/cookbook?retryWrites=true&w=majority')


class Recipe(Document):
    title = StringField(required=True, max_length=200)
    cuisine_name = StringField(required=True)
    type_name = StringField(required=True, max_length=50)
    description = StringField(required=True, max_length=200)
    ingredients = ListField(field=StringField(),required=True, max_length=30)
    step=ListField(field=StringField(),required=True, max_length=30)
    image=URLField(required=True)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search_recipe')
def search_recipe():
    return render_template("search_recipe.html")

@app.route('/get_recipe',methods=['POST','GET'])
def get_recipe():
        query = request.form.get("query")
        results=Recipe.objects(title__icontains=query)
        print("hi!")
        print(results.count())
        return render_template('recipe_list.html', recipe=results)
        


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
    recipe_doc=Recipe(
        title=recipe_dict['title'],
        cuisine_name=recipe_dict['cuisine_name'],
        type_name=recipe_dict['type_name'],
        description=recipe_dict['description'],
        image=recipe_dict['image'],
        ingredients=recipe_dict['ingredients'],
        step=recipe_dict['method']

    )
    print(ingredients)
    print(method)
    print(recipe_dict)
    print(recipe_doc)
    print("inside insertrecipe app.py")
    recipe_doc.save()
    return redirect(url_for('recipe_list'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines = mongo.db.cuisine.find()
    return render_template('editrecipe.html', item=the_recipe,cuisine=all_cuisines)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe_dict = request.form.to_dict()
    ingredients = request.form.getlist('ingredient')
    recipe_dict['ingredients'] = ingredients
    method = request.form.getlist('step')
    recipe_dict['method'] = method
    recipe=Recipe.objects(pk=recipe_id)
    recipe.update ( 
        title = recipe_dict['title'] , 
        cuisine_name = recipe_dict['cuisine_name'] , 
        type_name = recipe_dict['type_name'] , 
        description = recipe_dict['description'] , 
        image = recipe_dict['image'] , 
        ingredients=recipe_dict['ingredients'],
        step=recipe_dict['method'])
    return redirect(url_for('recipe_list'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('recipe_list'))

@app.errorhandler(Exception)
def handle_500(e):
    return render_template("home.html"), 500

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
