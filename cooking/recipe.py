class Recipe():
    def __init__(self, name, cooking_level, cooking_time, ingredients, description, recipe_type, preparation):
        if (not isinstance(name, str)):
            raise ValueError("Recipe.name must be type str")
        if (not isinstance(cooking_level, int) or cooking_level < 0):
            raise ValueError("Recipe.cooking_level must be a positive integer")
        if (cooking_level < 1 or cooking_level > 5):
            raise ValueError("Cooking level must be between 1 and 5")
        if (not isinstance(cooking_time, int) or cooking_time < 0):
            raise ValueError("Recipe.cooking_time must be a positive integer")
        if (not isinstance(ingredients, list)):
            raise ValueError("Recipe.ingredients must be of type list")
        for ingredient in ingredients:
            if (not isinstance(ingredient, str)):
                raise ValueError("Recipe.ingredients[i] must be of type str for every i")
                if (not isinstance(description, str)):
                    raise ValueError("Recipe.description must be of type str")
        if (not isinstance(recipe_type, str)):
            raise ValueError("Recipe.recipe_type must be of type str")
        if (recipe_type not in ["starter", "lunch", "dessert"]):
            raise ValueError(f"<{recipe_type}> Recipe.recipe_type value must be one of the following: 'starter', 'lunch', 'dessert'")

        self.name = name
        self.cooking_level = cooking_level
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        self.preparation = preparation


    def __str__(self):
        result=f'{self.name}: lv.{self.cooking_level} {self.cooking_time}min. ({self.recipe_type}) '
        result+="\ningregdients: " + " ".join(self.ingredients)
        result+="\npreparation: \n" + self.preparation
        return (result)
    def __repr__(self):
        return (self.__str__())  




