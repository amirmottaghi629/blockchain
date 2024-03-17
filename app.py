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
<<<<<<< HEAD

=======
>>>>>>> 5ceee93dfb763d77d2ea810953e44e829af58474
if __name__=='__main__':
    app.run(debug=True)