from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'our secret!'


@app.route('/')
def enter():
    if 'filled_form' not in session:
        session['filled_form'] = True
    previous = session['filled_form']
    return render_template("index.html")

@app.route('/process_form', methods=['POST'])
def process_form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/show')

@app.route('/show')
def show():
    return render_template("show.html")


    






if __name__=="__main__":
    app.run(debug=True)

