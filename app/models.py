from . import db
from werkzeug.security import (generate_password_hash,
                               check_password_hash)
from flask_login import UserMixin
from . import login_manager


class Post(db.Model):
    __tablename__ = 'posts'
    all_posts = []
    def __init__(self,name,title,post,user):
        self.name = name
        self.title = title
        self.post = post
        self.user = user
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String)
    title = db.Column(db.String)
    post = db.Column(db.String)

    def save_post(self):
        db.session.add(self)
        db.session.commit()


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    pass_secure = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    bio = db.Column(db.String(255))

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.query.get(int(user_id))

    def __repr__(self):
        return f'User {self.username}'



class Quote:
    """
    Blueprint class for quotes consumed from API
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote


class Comment(db.Model):
    __tablename__ = 'comments'
    all_comments = []

    """
    """
    def __init__(self, name, comment):
        self.name = name
        self.comment = comment
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255),index = True)
    name = db.Column(db.String(255),unique = True, index = True)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
