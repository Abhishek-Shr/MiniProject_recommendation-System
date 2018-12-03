from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from UI1.models import User
from flask_login import current_user

class registrationform(FlaskForm):
    username = StringField('Username', 
                                    validators = [ DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email', 
                                    validators = [ DataRequired(), Email()])                                    
    password = PasswordField('Password', 
                                    validators = [ DataRequired(), Length(min = 4, max = 15)])                                    
    confirm_password = PasswordField('Confirm Password', 
                                    validators = [ DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user  = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('The username has been taken. Please choose a unique one')

    def validate_email(self,email):
        email  = User.query.filter_by(email = email.data).first()
        if email:
            raise ValidationError('The email has been taken. Please choose a unique one')
            
class loginform(FlaskForm):
    email = StringField('Email', 
                                    validators = [ DataRequired(), Email()])                                    
    password = PasswordField('Password', 
                                    validators = [ DataRequired(), Length(min = 4, max = 15)])                                    
    submit = SubmitField('Log In' )
    remember = BooleanField('Remember Me')


class updateaccountform(FlaskForm):
    username = StringField('Username', 
                                    validators = [ DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email', 
                                    validators = [ DataRequired(), Email()])                                    
    submit = SubmitField('Update')

    picture = FileField('Update Profile Picture', validators =[FileAllowed('jpg','png')])

    def validate_username(self,username):
        if username.data != current_user.username:  
            user  = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('The username has been taken. Please choose a unique one')


    def validate_email(self,email):
        if email.data != current_user.email: 
            email  = User.query.filter_by(email = email.data).first()
            if email:
                raise ValidationError('The email has been taken. Please choose a unique one')