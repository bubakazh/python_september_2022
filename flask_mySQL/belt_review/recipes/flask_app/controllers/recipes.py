
from flask_app import app, render_template, request, redirect, session, bcrypt, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

# ! ADDING A RECIPE
# * DISPLAY ROUTE
@app.route("/newrecipe")
def newRecipe():
    return render_template('newRecipe.html')

# TODO HANDLE ROUTE
@app.route("/addRecipe", methods=['post'])
def addRecipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect('/newrecipe')
    data = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'date_made' : request.form['date_made'],
        'under_30' : request.form['under_30'],
        'user_id': request.form['user_id']
    }
    Recipe.create(data)
    return redirect('/dashboardShowAll')
# ! END ADDING


@app.route('/dashboardShowAll')
def dashboardShowAll():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {'id' : id}
    return render_template('dashboardShowAll.html', recipes = Recipe.get_all())


# ! SHOW ONE RECIPE
@app.route("/showrecipe/<int:id>")
def showRecipe(id):
    data = {'id' : id}
    recipe = Recipe.get_one(data)
    user = User.get_one({'id' : recipe.user_id})
    return render_template('showOne.html', recipe = recipe)
# ! END SHOW ONE



# ! EDIT / UPDATE A RECIPE
# * DISPALY ROUTE
@app.route("/editrecipe/<int:id>")
def edit_recipe(id):
    data = {'id' : id}
    recipe = Recipe.get_one(data)
    return render_template('editRecipe.html', recipe = recipe)

# TODO HANDLE ROUTE
@app.route("/updaterecipe", methods=['post'])
def update_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/editrecipe/{request.form['id']}")
    Recipe.update(request.form)
    return redirect('/dashboardShowAll')
# ! END EDIT/UPDATE



# ! DELETE A RECIPE
@app.route("/deleterecipe/<int:id>")
def delete_recipe(id):
    Recipe.destroy({'id': id})
    return redirect('/dashboardShowAll')
# ! END DELETE