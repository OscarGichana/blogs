from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,Length,EqualTo
from ..models import User
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(min =2, max =20)])
    email = StringField('Email', validators=[Required(), Email() ])
    password = PasswordField('Password', validators=[Required(), Length(min =8)])
    password_confirm = PasswordField('Confirm Password', validators=[Required(), EqualTo('password'), Length(min =8)])
    submit =SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')