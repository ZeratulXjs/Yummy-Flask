import unittest  
from yumRecipes import *

#Test different classes for valid input acceptance and processing
class ValidTestCase(unittest.TestCase):
    
    def setUp(self):
        self.users = users('caesar', 'abc')
        self.RecipeCategory = RecipeCategory('cakes', 'baked goods')
        self.recipe = Recipe('fudge', ('Add chocolate','Add butter','Bake for 15min'))        
    def test_user(self):
        self.assertTrue(users, 'caesar')
    def test_RecipeCategory(self):
        self.assertTrue(RecipeCategory, "'cakes','baked goods'")

    #Test the different class methods
    def test_Recipedetailadd(self):
        self.recipe = Recipe('fudge', [])
        self.assertEqual(self.recipe.add_step('Cool'), ['Cool'])
    def test_Recipedeldetail(self):
        self.recipe = Recipe('fudge', ['Cool'])
        self.assertEqual(self.recipe.del_step('Cool'), [])

# This class will test for empty input and raise errors
class EmptyTestCase(unittest.TestCase):

    def test_emptyemail(self):
        self.users = users('','abc')
        self.assertTrue(users, ValueError)
    def test_emptypwd(self):
        self.User = users('caesar', '')
        self.assertTrue(users, ValueError)

if __name__ == '__main__':
    unittest.main()