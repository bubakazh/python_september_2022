from flask import Flask, render_template
# import the class from friend.py
from friend import Friend

app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)
            
@app.route('/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')



# Note: We have set up the query_db method so that each attempted query will be printed to the terminal. Whenever the query you put together does not seem to work or gives an error message, investigate the actual query being run in the terminal. You may try copying and pasting the query into MySQL Workbench to see if you have the right syntax.

if __name__ == "__main__":
    app.run(debug=True)

