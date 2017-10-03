# user accounts will be derived from this class 

class User(object):
    def __init__(self, email, password):
        self.email = str(email)
        self.password = str(password)
        
        # Checking that the email and password are not empty  
        if not email:
            print "Please enter a valid email address"
        if not password:
            print "Please set a password"
        regusers = set()


# Recipe categories will be set by this class   
class RecipeCategory(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __del__(self):
        print 'Recipe Category deleted'
    def edit_name(self, category_name):
        pass
    def edit_description(self, description):
        pass
    def get_recipes(self):
        pass
    def add_recipe(self):
        pass
# Creating the recipe class where the individual recipes will be held. 

class Recipe(object):
    def __init__(self, name, description = [], newstep = "", oldstep = ""):
        self.name = name
        self.description = description
        self.newstep = newstep
        self.oldstep = oldstep
        
    def __del__(self):
        print 'Deleting recipe'

    def add_step(self, newstep):
            self.description.append(newstep)
            return self.description
    def del_step(self, oldstep):
            self.description.remove(oldstep)
            return self.description   
