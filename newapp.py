from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def home():
    render_template('siteflask.html')
if __name__=='__main___':
      app.run(debug=True)

