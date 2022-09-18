
from flask_app import app, render_template, request, redirect, session, bcrypt, flash
from flask_app.models.recipe import Recipe

# ! ADDING A RECIPE
# * DISPLAY ROUTE
@app.route("/newrecipe")
def newRecipe():
    return render_template('newRecipe.html')

# TODO HANDLE ROUTE
@app.route("/addRecipe", methods=['post'])
def addRecipe():
    print(request.form)
    # if not Recipe.validate_recipe(request.form):
    #     return redirect('/newrecipe')
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
@app.route("/recipe/<int:id>")
def recipe_show(id):
    return render_template('recipe_show.html')
# ! END SHOW ONE



# ! EDIT / UPDATE A RECIPE
# * DISPALY ROUTE
@app.route("/editrecipe/<int:id>")
def recipe_edit(id):
    return render_template('recipe_edit.html')

# TODO HANDLE ROUTE
@app.route("/updaterecipe/<int:id>", methods=['post'])
def recipe_update(id):
    if not Recipe.validate_recipe(request.form):
        return redirect('/editrecipe')
    return redirect('/dashboardShowAll')
# ! END EDIT/UPDATE



# ! DELETE A RECIPE
@app.route("/recipe/<int:id>/delete")
def recipe_delete(id):
    return redirect('/')
# ! END DELETE