from flask import Flask, render_template, redirect, url_for, render_template

app = Flask(__name__)

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
