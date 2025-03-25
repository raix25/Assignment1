print("Welcome to the recipe ingredients tracker!\n")

#making list of the options
list1=["1","2","3","4","0"]
list2=["Add a new recipe", "View a Recipe", "List all recipe", "Remove a recipe", "exit"]

#making dictionary to store recipes
recipe ={}

#for adding recipes 
def add_recipe():
    recipe_name = input("Enter the recipe name:")
    ingredient= input("Enter ingredients (comma-separated):").split(",") #to separate the ingredients 
    recipe[recipe_name] = ingredient #storing user input in recipe
    print(f"Recipe'{recipe_name}' added successfully!")

#for viewing recipe
def view_recipe():
    recipe_name= input ("enter the recipe to view:")
    if recipe_name in recipe:
        print(f'\nRecipe: {recipe_name} \nIngredient: {','.join (recipe[recipe_name])}') # joining the ingredients of recipe and if not found then printing not found
    else:
        print("Recipe not found!")

#for listing all the recipe
def list_all_recipes():
    if recipe:
        print("\nAll Recipes:")
        for recipe_name in recipe:
            print(f"-{recipe}") #displaying the recipes
    else:
        print("No recipe found!")

#removing the recipe from the dictionary 
def remove_recipe():
    recipe_name= input("enter the recipe name to remove:")
    if recipe_name in recipe:
        del recipe[recipe_name] #for deleting the recipe 
        print(f'Recipe "{recipe_name}" removed successfully!')
    else:
        print("Recipe not found!")

#display the result 
def main():
    while True: 
        print("\nAvailable options:\n")
        for i in range(len(list1)):
            print(f'{list1[i]}: {list2[i]}')
            
        choice= input("\nEnter your choice: ")

        if choice =="1":
            add_recipe()
        elif choice =="2":
            view_recipe()
        elif choice =="3":
            list_all_recipes()
        elif choice =="4":
            remove_recipe()
        elif choice =="0":
            print("Existing program.BYE!!!!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()