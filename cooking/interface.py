import traceback
import datetime
from recipe import Recipe
from book import Book 

class Interface():
	def __init__(self):
		self.book = Book("Yummy book")
		self.OPTIONS = {
			'1': {
				'str' : 'Add a recipe',
				'f' : self.new_recipe
			},
			'2': {
				'str' : 'Delete a recipe',
				'f' : self.delete_recipe
			},
			'3': {
				'str' : 'Delete all recipes',
				'f' : self.delete_all
			},
			'4': {
				'str' : 'Print a recipe',
				'f': self.get_recipe
			},
			'5': {
				'str': 'Print the recipe list',
				'f' : self.recipes_list
			},
			'6': {
				'str': 'Print the cookbook',
				'f' : self.get_all
			},
			'0': {
				'str': 'Exit',
				'f': lambda:exit()
			}
		}

	def recipes_list(self):
			print("Recipes: ")
			for key in self.book.joint_recipes.keys():
				print("  " + key) 

	def get_recipe(self, recipeName = None):
		if (self.book.len == 0):
			print("There are no recipes\n")
			return ;
		recipe = None
		while (not recipe):
			while (not recipeName):
				recipeName = input("Enter recipe: \n")
				if (recipeName == ""):
					print("Aborted, no input provided")
					return
			recipe = self.book.get_recipe_by_name(recipeName)
			if (not recipe):
				print("Recipe name does not exists")
				return 
		print(recipe)

	def delete_recipe(self, recipe = None):
		if (not self.book.len):
			print("There are no recipes\n")
			return ;
		keys = self.book.joint_recipes.keys()
		while (not recipe or recipe not in keys):
			recipe = input("Enter recipe: \n")
		self.book.delete_recipe(recipe)

	def new_recipe(self):
		name = input("Enter name: \n")
		cooking_level =  input("Enter cooking level (1-5): \n")
		cooking_time =  input("Enter preparation time: \n")
		description = input("Enter description: \n") 
		typpe = input("Enter recipe type (starer, lunch, dessert): \n")

		print("Enter ingridients (enter blank line when finished):")
		ingredient = "True"
		ingredients = []
		while (ingredient):
			ingredient = input()
			if ingredient:
				ingredients.append(ingredient)

		print("Enter preparation (enter blank line when finished):")
		step = "True"
		preparation = ""
		while (step):
			step = input()
			if step:
				preparation += step + "\n"
			
		try :
			recipe = Recipe(
							name,
							int(cooking_level),
							int(cooking_time),
							ingredients,
							description,
							typpe,
							preparation
						)
			self.book.add_recipe(recipe)
		except Exception as e:
			print(e)

	def get_all(self):
		print()
		for recipe in self.book.joint_recipes.values():
			print(recipe)

	def delete_all(self):
		self.book.delete_all_recipes()
		return

	def run(self):
		action = -1
		while (action != 0):
			for key, value in self.OPTIONS.items():
				string = value['str']
				print(f'{key}: {string}')
			action = input()
			if (action not in self.OPTIONS.keys()):
				continue
			try :
				self.OPTIONS[action]['f']()  
			except Exception as e:
				#print(traceback.format_exc())
				print(e)
