"""This is a program dsignd for madlibs that wil fill int the blank and tell a story based on usser input
"""

# The template for the story

STORY = "This morning {} woke up feeling {}. 'It is going to be a {} day!' Outside, a bunch of {}s were protesting to keep {} in stores. They began to {} to the rhythm of the {}, which made all the {}s very {}. Concerned, {} texted {}, who flew {} to {} and dropped {} in a puddle of frozen {}. {} woke up in the year {}, in a world where {}s ruled the world."
print ("Mad Libs has started")
name = input("Enter a name:")
first_adjective = input("Enter a adjective:")
second_adjective = input("Enter a adjective:")
third_adjective = input("Enter a adjective:")
verb = input("Enter a verb:")
first_noun = input("Enter a noun:")
second_noun = input("Enter a noun:")
animal = input("Enter an animal:")
food = input("Enter a food:")
fruit = input("Enter a fruit:")
hero = input("Enter a Superhero:")
country = input("Enter a country:")
dessert = input("Enter a dessert:")
year = input("Enter a year:")
print ("This morning {} woke up feeling {}. 'It is going to be a {} day!' Outside a bunch of {}s were protesting to keep {} in the stores. They began to {} to the rhythm of the {}, which made all the {}s very {}. Concerned, {} texted {}, wh flew to {} to {} and dropped {} in a puddle of frozen {}. {} woke up in the year {}, in a world where {}s ruled the world.".format(name, first_adjective, second_adjective, animal, food, verb, first_noun, fruit, third_adjective, name, hero, name, country, name, dessert, name, year, second_noun))
