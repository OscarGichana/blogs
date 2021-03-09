from flask import (render_template, request, redirect, url_for, abort)
from . import main
from ..models import Post,Comment,User
from flask_login import login_required, current_user
from .forms import (UpdateProfile, PostForm, CommentForm, UpdatePostForm)
from datetime import datetime
from .. import db,photos
from flask_wtf import FlaskForm
from ..requests import get_quote



@main.route('/')
def index():
    title = 'BLOGGED'
    post = Post.query.all()
    Quote = get_quote()

    return render_template('index.html', title =title, post = post, quote = Quote)

@main.route("/post", methods = ["POST", "GET"])
def post():
    form=PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data, name = form.name.data, user = current_user, post = form.post.data)
        post.save_post()
        return redirect(url_for("main.index"))

    return render_template("post.html", form = form)




@main.route('/post/<int:id>/comments', methods = ["POST", "GET"])
def comments(id):
    title = 'COMMENTS'
    comment_form = CommentForm()
    comments = Comment.query.all()
    post=Post.query.get(id)
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        name = comment_form.name.data

        # Updated review instance
        new_comment = Comment(comment = comment, name = name)

        # save review method
        new_comment.save_comment()
        #return redirect(url_for('.movie',id = movie.id ))

    return render_template('comments.html', title =title, comment_form = comment_form, comments = comments, post = post)



@main.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", username = username,user = user)


@main.route('/profile/<username>/update/pic',methods= ['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',username=username))


@main.route('/profile/<username>/update',methods = ['GET','POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',username=user.username))

    return render_template('profile/update.html',form =form)
