# user accounts will be derived from this class 

class users(object):
    def __init__(self, uname, password):
        regusers = {}


class new_user(object):
    def __init__(self, uname, password):
        self.uname = str(uname)
        self.password = str(password)
        
    def signup(self, uname, password):
        # Checking that the uname and password are not empty  
        if not uname or password:
            print "Please enter a username or password"
        elif key in regusers.keys():            
            print "Please enter a unique username"
        else:
            regusers.update({'uname':password})

    def login(self, uname, password):
        if not uname or password:
            print "Please enter a username or password"
        elif uname not in regusers.keys():
            print "User does not exist"   

        elif uname in regusers.keys():
            if regusers[key] == password:
                print "You're in"
                    #Link to user's recipe dictionaries(categories and recipes)
    


# Recipe categories will be set by this class   
class RecipeCategory(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        recipe_cats = {}

    def del_cat(self, cat):
        if cat in recipe_cats:
            del recipe_cats[cat]
            print 'Recipe Category deleted'
        else:
            print 'Category does not exits'

    def edit_name(self, category_name):
        
        if key in regusers.keys()
                print "Please enter a unique username"
        else:
            regusers.update({'uname':password})
       

    def edit_description(self, description):
        
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
