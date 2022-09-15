- [x] create directory for app
- [x] create virtual environment

```bash

[python -m] pipenv install flask

```

- [x] create [server.py](server.py)


```bash

from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

```

- [x] activate our virtual environment

```bash

[python -m] pipenv shell

```

- [x] [python server.py](http://127.0.0.1:5000/)