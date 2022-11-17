ages = [5, 15, 64, 27, 84, 26]

odd_ages = [number for number in ages if number % 2 != 0]

print(odd_ages)

chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]

names_10 = [chicken for chicken in chicken_names if len(chicken) > 10]

print(names_10)

names_h = [chicken for chicken in chicken_names if chicken[0] == "H"]

print(names_h)

words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

lower_letters = [letter[0].lower() for letter in words]

print(lower_letters)




