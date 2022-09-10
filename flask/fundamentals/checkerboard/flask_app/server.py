from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index(num, numb):
    return render_template('index.html', num = 8, numb = 8, color1 = "green", color2 = "blanchedalmond")

@app.route('/<int:num>')
def mod_one_aspect(num):
    return render_template('index.html', num = num, numb = 8, color1 = "green", color2 = "blanchedalmond")

@app.route('/<int:num>/<int:numb>')
def mod_two_aspect(num, numb):
    return render_template('index.html', num = num, numb = numb, color1 = "green", color2 = "blanchedalmond")

@app.route('/<int:num>/<int:numb>/<color1>/<color2>')
def fully_modular(num, numb, color1, color2):
    return render_template('index.html', num = num, numb = numb, color1 = color1, color2 = color2)

if __name__ == "__main__":
    app.run(debug=True)

