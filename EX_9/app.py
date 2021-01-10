from flask import Flask, render_template, redirect, url_for, render_template
from flask import request
from flask import session



app = Flask(__name__)
app.secret_key = '1212'

@app.route('/')
@app.route('/index.html')
def main_page():
    return render_template('index.html')

@app.route('/contact_us.html')
def Contact_Us():
    return render_template('contact_us.html')

@app.route('/assigment8.html')
def assigment8():
    return render_template('assigment8.html',
                           firstName="Maya", lastName="Dvash",
                           movies_pref=['Action', 'Comedy', 'Horror']
                           )

@app.route('/assigment8new.html')
def assigment8_new():
    return render_template('assigment8new.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    name = 'Friend'
    Users = {"Roni": "Rabinovich", "Adi": "Danovich", "Hagar": "Cohen", "Daniela": "Ovadia", "David": "Dvash"}
    username = ' '
    logged_in = True

    if request.method == 'GET':
        if 'name' in request.args:
            name = request.args['name']

    if request.method == 'POST':
        username = request.form['username']
        session['logged_in'] = True
        session['username'] = username


    return render_template('assignment9.html',
                           request_method=request.method,
                           name = name,
                           Users = Users,
                           username = username)

@app.route('/log_out')
def log_out():
    session.pop('username')
    session['logged_in'] = False
    return redirect('/assignment9')