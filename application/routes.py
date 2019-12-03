from flask import render_template, redirect, url_for
from application import app, db
from application.models import Posts
from application.forms import PostForm

dummyData = [
{
       "name": {"first":"Chester", "last":"Gardner"},
       "title":"First Post",
       "content":"This is some dummy data for Flask lectures"
},
{
       "name": {"first":"Chris", "last":"Perrins"},
       "title":"Second Post",
       "content":"This is even more dummy data for Flask lectures"
}
]





@app.route('/home')
def home():
    return render_template('home.html', title='Home', posts=dummyData)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/post', methods=['GET','POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        postData = Posts(
        first_name=form.first_name.data,
        last_name=form.last_name.data,
        title=form.title.data,
        content=form.content.data
    )
        db.session.add(postData)
        db.session.commit()
        return redirect(url_for('home'))

    else:
        print (form.errors)
    return render_template('post.html', title='Post', form=form)

