import json

def load_foods():
    try:
        with open("foods.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_foods(foods):
    with open("foods.json", "w") as file:
        json.dump(foods, file, indent=4)

def main():
    foods = load_foods()
    while True:

        print(
            " Please enter a number to determine your choice \n"
            "1 to view all dish names \n"
            "2 to view dish details by name \n"
            "3 to filter dishes by calorie count \n"
            "4 to add a new dish \n"
            "5 to remove a dish \n"
            "6 to modify a dish by name \n"
            "7 to search a dish by ingredient \n"
            "8 to exit"
        )
        ans = input()
        if ans == "1":
            view_dish_names(foods)
        elif ans == "2":
            print("Enter the name of the dish you want to view")
            dish_name = input().lower()
            if check_valid_dish(dish_name, foods):
                view_dish_details(dish_name, foods)
        elif ans == "3":
            print("1. View dishes below a calorie threshold")
            print("2. View dishes above a calorie threshold")
            option = input("Enter your choice: ")
            max_calories = int(input("Enter the calorie value: "))
            filter_dishes_by_calories(max_calories, foods, option)

        elif ans == "4":
            new_food = create_dish(foods)
            if new_food:
                foods.append(new_food)
                print("Your food has been added")
            else:
                print("That food already exists or input is invalid")

        elif ans == "5":
            print("Enter the name of the dish you want to remove")
            dish_name = input().lower()
            if check_valid_dish(dish_name, foods):
                remove_dish(dish_name, foods)
            else:
                print("food does not exist double check your spelling")
        elif ans == "6":
            print("Enter the name of the dish you want to modify")
            dish_name = input().lower()
            if check_valid_dish(dish_name, foods):
                modify_dish(dish_name, foods)
        elif ans == "7":
            print("Enter the ingredient you want to search")
            ingredient = input().lower()
            search_dish_by_ingredient(ingredient, foods)
        elif ans == "8":
            save_foods(foods)
            print("Have a nice day")
            break
        else:
            print("Input not recognized please try again")


def view_dish_names(foods):
    dish_names = []
    for dish in foods:
        dish_names.append(dish.get("name"))
    for item in dish_names:
        print(item)


def view_dish_details(dish_name, foods):

    for item in foods:
        if item.get("name") == dish_name:
            print(f"Name:{item.get('name')}, Calories:{item.get('calories')}, Ingredients:{item.get('ingredients')}")
            return
    print("Dish not found")
    return


def filter_dishes_by_calories(max_calories, foods, option):
    acceptable_foods = [
        item for item in foods
        if (option == '1' and item.get("calories") < max_calories) or
           (option == '2' and item.get("calories") > max_calories)
    ]
    for item in acceptable_foods:
        print(f"You can eat {item}")


def create_dish(foods):
    new_food = {}
    print("enter the foods name then calories then ingredients (e.g Spaghetti 400 ingredients meatballs sauce noodles")
    input_tokens = input().split()
    if len(input_tokens) < 4:
        return False
    for item in foods:
        if item.get("name") == input_tokens[0]:
            return False
    new_food["name"] = input_tokens[0]
    new_food["calories"] = int(input_tokens[1])
    new_food["ingredients"] = input_tokens[3:]
    return new_food


def remove_dish(dish_name, foods):
    index_of_dish = get_valid_dish_index(dish_name, foods)
    foods.pop(index_of_dish)
    print("Dish has been removed")


def modify_dish(dish_name, foods):
    dish_to_modify_index = get_valid_dish_index(dish_name, foods)
    print("What do you want to modify \n"
          "1 to change name \n"
          "2 to change calories \n"
          "3 to edit ingredients")
    ans = input()
    if ans == "1":
        print("Enter the new name")
        new_name = input()
        foods[dish_to_modify_index]["name"] = new_name
    elif ans == "2":
        print("Enter the new calories")
        new_calories = int(input())
        foods[dish_to_modify_index]["calories"] = new_calories
    elif ans == "3":
        print("Enter the new ingredients")
        new_ingredients = input().split()
        foods[dish_to_modify_index]["ingredients"] = new_ingredients


def search_dish_by_ingredient(ingredient, food):
    for item in food:
        if ingredient in item.get("ingredients"):
            print(f"{item.get('name')}")


def get_valid_dish_index(dish_name, foods):
    for index, item in enumerate(foods):
        if item.get("name") == dish_name:
            return index


def check_valid_dish(dish_name, foods):
    valid_dish = False
    for item in foods:
        if item.get("name") == dish_name:
            valid_dish = True
    return valid_dish



if __name__ == "__main__":
    main()