from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flasklogin'
db = SQLAlchemy(app)

class userlogin(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Username= db.Column(db.String(80), nullable=True)
    Password= db.Column(db.String(12), nullable=False)

@app.route("/")  
def home():  
    return render_template('index.html');

@app.route("/Book appointment")  
def cources():  
    return render_template('cources.html'); 

@app.route("/About us")  
def books():  
    return render_template('books.html'); 


@app.route('/Admin login', methods=['GET', 'POST'])
def login():
    if(request.method=='POST'):
        '''Add entry to the database'''
        Username= request.form.get('Username')
        Password= request.form.get('password')
        entry = userlogin(Username=Username,Password=Password )
        db.session.add(entry)
        db.session.commit()
    return render_template('login.html')



if __name__ =="__main__":  
    app.run(debug = True)