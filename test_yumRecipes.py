import unittest  
from yumRecipes import *

#Test different classes for valid input acceptance and processing
class ValidTestCase(unittest.TestCase):
    
    def setUp(self):
        self.User = User('caesar', 'abc')
        self.RecipeCategory = RecipeCategory('cakes', 'baked goods')
        self.recipe = Recipe('fudge', ('Add chocolate','Add butter','Bake for 15min'))        
    def test_user(self):
        self.assertTrue(User, 'caesar')
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
        self.User = User('','abc')
        self.assertTrue(User, ValueError)
    def test_emptypwd(self):
        self.User = User('caesar', '')
        self.assertTrue(User, ValueError)

if __name__ == '__main__':
    unittest.main()