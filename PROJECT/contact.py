from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,DateField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,optional,EqualTo


class contact(FlaskForm):
    name=StringField(
        "name",
        validators=[DataRequired(),Length(4,15)]
    )

    email=StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )

    submit=SubmitField("Submit")