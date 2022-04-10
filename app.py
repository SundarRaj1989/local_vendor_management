from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

import local_market_ms_db

# ======================================================================================== Login

@app.route('/login')
def login():
    return render_template('login.html')

# ==============================================================================================

@app.route('/')
def index():
    return render_template('home.html')

    
@app.route('/insert_data')
def insert_data():
    data = {}

    data['name'] = 'Raj Sundar'
    data['address'] = 'BBSR'
    data['number'] = '8569741230'

    print(data)

    local_market_ms_db.save_data(data)

    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')




if __name__ == '__main__':
    app.run(debug=True)