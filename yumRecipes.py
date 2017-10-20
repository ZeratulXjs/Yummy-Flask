# user accounts will be derived from this class 

class Users(object):
  def __init__(self):
    self.user_list = []

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