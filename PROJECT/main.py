from flask import Flask, flash,render_template,redirect,url_for
from menu import menu
from contact import contact
from forms import signupform,loginform
app=Flask(__name__)

app.secret_key="jvhjfdbvhfdyvbvjbfvjv jdbvhdvjjvbj"
@app.route("/")

@app.route("/home")
def home():
    return render_template("home.html",title="Home")

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/contact",methods=['GET','POST'])
def call():
    cont=contact()
    if cont.validate_on_submit():
        return redirect(url_for("home"))
        
    return render_template("contact.html",title="Contact",contact=cont)

@app.route("/menu")
def menu():
    return render_template("menu.html",title="Menu",menu=menu)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = loginform()
    if form.validate_on_submit():
         flash(f"Successfully Registered {form.username.data}")
         return redirect(url_for("home"))
    return render_template("login.html", title="Login", form=form)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = signupform()
    if form.validate_on_submit():
         flash(f"Successfully Registered {form.username.data}")
         return redirect(url_for("home"))
        
       
    return render_template("signup.html", title="Sign Up", form=form)

if __name__=="__main__":
    app.run(debug=True)