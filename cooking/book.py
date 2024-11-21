import datetime
from recipe import Recipe
from typing import Union

class Book():
	@staticmethod
	def empty_recipes_list():
		return { 'starter': {}, 'lunch':{}, 'dessert': {} }	
	
	def __init__(
		self,
		name: str,
		recipes_list: dict = None
	):
		ks = ['starter', 'lunch', 'dessert']
		if (recipes_list == None):
			recipes_list = Book.empty_recipes_list() 
		for k in recipes_list.keys():
			if k not in ks:
				raise AssertionError("Recipes list must contain three keys: 'starter', 'lunch', dessert' ")
		for k in ks:
			if k not in recipes_list.keys():
				raise AssertionError("Recipes list must contain three keys: 'starter', 'lunch', dessert' ")
		self.name = name
		#self.last_update = datetime.date.today()
		#self.creation_date = datetime.date.today()
		self.recipes_list = recipes_list
	

	def get_recipe_by_name(self, name: str):
		#if (name not in self.joint_recipes):
		#	 raise KeyError(f"There is no {name} recipe in {self.name} book")
		if (name not in self.joint_recipes):
			return None
		return (self.joint_recipes[name])

	def get_recipes_by_type(self, tpe: str):
		result = self.recipes_list.get(tpe)
		if (not result):
			raise KeyError(f"There is no {tpe} type in {self.name} book")
		return (self.recipes_list[tpe])

	def add_recipe(self, recipe: Recipe):
		if (not isinstance(recipe, Recipe)):
			raise TypeError("recipe must be of type Recipe")
		self.recipes_list[recipe.recipe_type][recipe.name] = recipe

	def delete_recipe(self, recipe: Union[str, Recipe]):
		if (isinstance(recipe, str)):
			recipe = self.get_recipe_by_name(recipe)
		del self.recipes_list[recipe.recipe_type][recipe.name]
	
	def delete_all_recipes(self):
		for recipe in self.joint_recipes.values():
			self.delete_recipe(recipe)
		
	@property
	def joint_recipes(self):
		dct = {}
		for k in ['starter', 'lunch', 'dessert']:
			dct.update(self.recipes_list[k])
		return dct

	@property
	def len(self):
		return (len(self.joint_recipes))



