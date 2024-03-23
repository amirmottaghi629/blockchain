from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home page.html')
@app.route('/login_page.html')
def login():
    return render_template('login_page.html')
@app.route('/contact_us.html')
def contact():
    return render_template('contact_us.html')
@app.route('/page1.html')
def menu():
    return render_template('page1.html')
@app.route('/m2m.html')
def m2m():
    return render_template('m2m.html')
if __name__=='__main__':
    app.run(debug=True)