#1 - The user must inform how many foods ate during the day
#2 - The user must inform the number of calories of each one

foods = int(input("Inform the number of foods you ate today: "))
print(foods)
i = 0

while (i < foods):
    i = i + 1
    total_calories = 0.0

    food_calories = float(input("Inform how many calories that food has: "))

    total_calories = total_calories + food_calories

print("You ate a total of {} calories".format(total_calories))