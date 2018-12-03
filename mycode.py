from flask import Flask, render_template, url_for, flash, redirect
from form import registrationform, loginform
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__,template_folder='pages')

app.config['SECRET_KEY'] = 'ede904d885f000b4ddc283d1ad0378c49e91a440'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default='default.jpg')
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref = 'author',lazy = True)

    def __repr__(self):
        return f"User('{self.username}',{self.email},{self.image_file})"
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable = False)
    date_posted = db.Column(db.DateTime, nullable = True, default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}'"


data = [
    {
        'name' : 'abhishek',
        'password' : 'abhi@2',
        'email' : 'abhishekshr2@gmail.com',    
        'rollno' : '161500022',
    },
    {
        'name' : 'abhinav',
        'password' : 'nav@3',
        'email' : 'abhinavrao3@gmail.com',
        'rollno' : '161500013',
    }
]

@app.route("/")
def home():
    return render_template('home.html',data = data,title = 'WELCOME')

@app.route("/register", methods = ['GET','POST'])
def register():    
    form = registrationform()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title = 'Register',form = form)

@app.route("/login", methods = ['GET','POST'])
def login():
    form = loginform()
    if form.validate_on_submit():
        if form.email.data == 'abhishekshr2@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')                
    return render_template('login.html',title = 'Register',form = form)

@app.route("/about")
def about():
    return render_template('about.html',title = 'ABOUT')

if __name__ == '__main__':
    app.run(debug=1)
