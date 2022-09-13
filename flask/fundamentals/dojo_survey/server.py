from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ffs'

@app.route('/')
def survey():
        return render_template('index.html')

@app.route('/process', methods=['POST'])
def handle_submission():
    print(request.form)
    session['name'] = request.form['ninja_name']
    session['dojo'] = request.form['dojo']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    print(session)
    return redirect('/submission')

@app.route('/submission')
def display_submission():
    return render_template('submission.html')

if __name__ == '__main__':
    app.run(debug=True)