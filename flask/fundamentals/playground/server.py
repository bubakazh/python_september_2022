from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def boxes():
    return render_template('index.html', num = 3, color = "aqua")

@app.route('/play/<int:num>')
def hellaBoxes(num):
    return render_template('index.html', num = num, color = "aqua")

@app.route('/play/<int:num>/<string:color>')
def customBoxes(num, color):
    return render_template('index.html', num = num, color = color)


if __name__ == '__main__':
    app.run(debug=True)