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
class Recipe(object):
  def __init__(self):
    self.recipes = []

  def add_recipes(self):
    recipes = [
      {
          'id' : 1,
          'title' : 'jacket potatoes',
          'body' : 'Wash potatoes, boil with jackets on for 10min, apply some butter, wrap in alu-foil and bake for 15min',
          'author' : 'Caesar'
      },
      {
          'id' : 2,
          'title' : 'mash potatoes',
          'body' : 'Wash potatoes, boil with jackets on for 10min, add some butter and milk, mash and serve',
          'author' : 'Caesar'
      },
      {
          'id' : 3,
          'title' : 'deep fried potatoes',
          'body' : 'Wash potatoes, boil with jackets on for 10min, deep fry',
          'author' : 'Caesar'
      }
    ]
    return recipes