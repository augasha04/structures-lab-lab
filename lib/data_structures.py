spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# for keys in spicy_foods:
#     print(keys["name"])
    
for item in spicy_foods[1:0]:
    print(item)
      
for item in spicy_foods[0:3]:
    heat_level = item.get("heat_level")
    multiplied_heat_level = heat_level * "🌶️"
    print(multiplied_heat_level)
 
 
 
# def get_spicy_food_by_cuisine(spicy_foods, cuisine):
#     pass

# def print_spiciest_foods(spicy_foods):
#     pass

# def get_average_heat_level(spicy_foods):
#     pass

# def create_spicy_food(spicy_foods, spicy_food):
#     pass
