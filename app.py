from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def home():
<<<<<<< HEAD
    return render_template('index.html')
=======
    return render_template('home page.html')
@app.route('/login_page.html')
def login():
    return render_template('login_page.html')
@app.route('/contact_us.html')
def contact():
    return render_template('contact_us.html')
>>>>>>> 1016db48166137b25134e4d3b3cb63ee8d990c30
if __name__=='__main__':
    app.run(debug=True)