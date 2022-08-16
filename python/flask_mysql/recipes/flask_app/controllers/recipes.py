from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models import recipe, user
from ..models.recipe import Recipe

#? change after .models to model file (in this case.recipe - then go greate recipe model. | change User to Recipe)

@app.route('/recipes')  #?only use method when you post something (form action) 
def recipes(): #? never use model name as function name
    if "user_id" not in session:
        flash("ERROR! Must login")
        return redirect('/') #? checking if user id exists in our dictionary: session | should be on all of your routes.
    user_data={
        'id' : session['user_id']
    }
    this_user = user.User.get_user_by_id(user_data)

    this_recipe = recipe.Recipe.get_all_recipes()

    return render_template('dashboard.html', user = this_user, recipes = this_recipe)

    


@app.route('/create')
def new_recipe():
    if "user_id" not in session:
        flash("ERROR! Must login")
        return redirect('/') #! add to routes (only users can access this page)
    return render_template('create.html')


@app.route('/create', methods=['POST'])
def recipe_submit():
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect('/create') #! this chunk kicks  you back to create if recipe is not valid
    recipe.Recipe.create(request.form)
    return redirect('/recipes')

@app.route('/recipes/<int:id>')
def view_recipe(id):
    user_dict = {
        'id' : session['user_id']
    }
    this_user = user.User.get_user_by_id(user_dict)
    recipe_data = {
        'id' : id
    }
    this_recipe = recipe.Recipe.get_one(recipe_data)
    return render_template('show.html', user = this_user, recipes = this_recipe) 

@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    user_dict = {
        'id' : session['user_id']
    }
    this_user = user.User.get_user_by_id(user_dict)
    recipe_data = {
        'id' : id
    }
    this_recipe = recipe.Recipe.get_one(recipe_data)
    if(this_recipe.user_id != this_user.id):
        flash(f'Unauthorized access to edit recipe with id {id}')
        return redirect('/dashboard')

    return render_template('edit.html', user = this_user, recipes = this_recipe) 


@app.route('/recipes/<int:id>/edit', methods=['POST'])
def submit_edit(id):
    user_dict = {
        'id' : session['user_id']
    }
    this_user = user.User.get_user_by_id(user_dict)
    recipe_data = {
        'id' : id
    }
    this_recipe = recipe.Recipe.get_one(recipe_data)
    if(this_recipe.user_id != this_user.id):
        flash(f'Unauthorized access to edit recipe with id {id}')
        return redirect('/dashboard')
    recipe.Recipe.update(request.form)
    # return redirect('/dashboard')
    return redirect(f'/recipes/{id}') #!sends us specifically to show route. redirects to show 1 page or back to "recipes" page


@app.route('/recipes/<int:id>/delete')
def delete(id):
    recipe_data = {
    'id' : id
}
    this_recipe = recipe.Recipe.get_one(recipe_data)
    if(this_recipe.user_id !=session['user_id']):
        flash(f'Unauthorized access to edit review with id {id}')
        return redirect('/dashboard')
    Recipe.delete(recipe_data)
    return redirect('/recipes')

@app.route('/recipes/<int:id>')
def show(id):
    recipe_data = {
        'id' : id
    }
    user_dict = {
        'id' : session['user_id']
    }
    this_recipe = recipe.Recipe.get_one(recipe_data)
    this_user = user.User.get_user_by_id(user_dict)

    return render_template('show.html', user = this_user, recipes = this_recipe) 