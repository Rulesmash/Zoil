from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/UrbanFarm')
def guide1():
    return render_template('UrbanFarm.html')


if __name__ == '__main__':
    app.run(debug=True)
