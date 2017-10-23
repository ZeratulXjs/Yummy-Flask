from wtforms import Form, StringField, PasswordField, TextAreaField, validators

# Define form attributes for signup using WTForms to allow easy validation
class SignupForm(Form):
  uname = StringField('Username', [validators.Length(min=3, max=50), validators.DataRequired()])
  password = PasswordField('Password', [
    validators.DataRequired(),
    validators.Length(min=6),
    validators.EqualTo('password_rep', message='Passwords do not match'),
  ] )
  password_rep = PasswordField('Repeat Password', [validators.DataRequired()])

# Creating the recipe class where the individual recipes will be held. 
class RecipeForm(Form):
  title = StringField('Recipe title', [validators.length(min=10, max=100)])
  steps = TextAreaField('Recipe steps',[validators.length(min=5)])
   