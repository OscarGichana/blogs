 
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                    SubmitField, SelectField)
from wtforms.validators import Required

class PostForm(FlaskForm):
    name = StringField("Your name:", validators=[Required()])
    title = StringField("Title:", validators=[Required()])
    post = TextAreaField("What's on Yout mind:", validators=[Required()])
    submit = SubmitField("Post")

class UpdatePostForm(FlaskForm):
    title = StringField("Blog title", validators=[Required()])
    post = TextAreaField("Type Away", validators=[Required()])
    submit = SubmitField("Update")

class CommentForm(FlaskForm):
    comment = TextAreaField("Post Comment", validators=[Required()])
    name = StringField("Your Name")
    submit = SubmitField("Comment")

class UpdateProfile(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last Name")
    bio = TextAreaField("Bio")
    email = StringField("Email")
    submit = SubmitField("Update")
