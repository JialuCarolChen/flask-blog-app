from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '41c907f395dc1244c69ab23a40fa363b'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]



@app.route("/")
# cv page
@app.route("/cv")
def cv():
    return render_template('cv.html', posts=posts, title="CV")
# project page
@app.route("/projects")
def projects():
    return render_template('projects.html', title="Projects")
# blog page
@app.route("/blog")
def blog():
    return render_template('blog.html', posts=posts, title="Blog")

# register and login
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', form = form, title="Register")
@app.route("/login")
def register():
    form = LoginForm
    return render_template('login.html', form = form, title="Login")







#if __name__ == '__main__':
#    app.run(debug=True)