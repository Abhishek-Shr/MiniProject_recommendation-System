from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__,template_folder='pages')

app.config['SECRET_KEY'] = 'ede904d885f000b4ddc283d1ad0378c49e91a440'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from UI1 import routes