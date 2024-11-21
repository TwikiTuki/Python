import datetime
from recipe import Recipe
from book import Book 
from interface import Interface 


def populate_interface(interface):
	recipe = Recipe(
					name = "food",
					cooking_level = 3,
					cooking_time = 10,
					ingredients = ["tasty thing", "sweet thing", "delicious thing"],
					description = ["food stuff"],
					recipe_type = "lunch",
					preparation = "do smth\n do smth more\n do smth else"
			)
	interface.book.add_recipe(recipe)
	recipe = Recipe(
					name = "fooder",
					cooking_level = 3,
					cooking_time = 10,
					ingredients = ["tastyer thing", "sweeter thing", "deliciouser thing"],
					description = ["more food stuff"],
					recipe_type = "lunch",
					preparation = "do smth\n do smth more\n do smth else"
			)
	interface.book.add_recipe(recipe)

if (__name__ == "__main__"):
	interface = Interface()
	#populate_interface(interface)
	#interface.delete_all()
	interface.run()
