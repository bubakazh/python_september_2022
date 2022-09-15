
from flask_app import app, render_template, request, redirect
from flask_app.models.user import User

@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users) # ! DON'T REALLY NEED THIS ANYMORE
    return render_template("index.html", all_users = users)

# ! READ ALL
@app.route("/users")
def users():
    users = User.get_all()                                              # * THIS LINE               users = User.get_all()
    return render_template('users.html', all_users = users)             # * AND THIS PART           all_users = users
                                                                        # *  ||
# ! READ ONE                                                            # *  ||
@app.route("/show/<int:id>")                                            # *  ||
def show(id):                                                           # * \  /
    data = {'id' : id}                                                  # *  \/
    return render_template("show.html", user = User.get_one(data))      # * SAME AS THIS LINE       user = User.get_one(data)

# ! EDIT/UPDATE
@app.route('/edit/<int:id>')
def edit(id):
    data = {'id' : id}
    return render_template('edit.html', user = User.get_one(data))

@app.route("/edit_user", methods=["POST"])
def edit_user():
    User.update(request.form)
    return redirect('/users') # TODO CHANGE THIS REDIRECT TO SHOW THE USER THAT WAS EDITED, NOT ALL USERS. SEE NINJAS CONTROLLER FROM DOJOS AND NINJAS FOR SYNTAX
    # return redirect(f"/show/{request.form['id']}") I THINK THIS IS IT. MAYBE TEST LATER?

# ! CREATE
# THIS IS THE ROUTE THAT DISPLAYS THE FORM FOR ADDING A NEW USER
@app.route('/new')
def new_user():
    return render_template('create.html')

# THIS IS THE ROUTE THAT HANDLES THE DATA WHEN ADDING A NEW USER
@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : request.form["password"]
    }
    # We pass the data dictionary into the save method from the User class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

# ! DELETE
@app.route('/delete/<int:id>')
def delete(id):
    data = {'id' : id}
    User.destroy(data)
    return redirect('/users')