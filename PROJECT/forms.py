from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,DateField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,optional,EqualTo


class signupform(FlaskForm):
    username= StringField(
        "username",
        validators=[DataRequired(),Length(4,20)]
    )


    email=StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )
    
    
    
    password=PasswordField(
        "password",
        validators=[DataRequired(),Length(5,15)]
    )
    confrim_password=PasswordField(
        "confrim_password",
         validators=[DataRequired(),Length(5,15),EqualTo("password")]
    )

    submit=SubmitField("sign up")



class loginform(FlaskForm):
    email=StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )
    password=PasswordField(
        "password",
        validators=[DataRequired(),Length(5,15)]
    )   
    remember= BooleanField(
        "remember me",
    )
    submit=SubmitField("login")