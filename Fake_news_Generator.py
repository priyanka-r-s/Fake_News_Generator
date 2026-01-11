import random

subjects = [
    "Sharuk Khan",
    "MSD",
    "Virat Kohli",
    "A Mumbai Cat",
    "The Prime Minister",
    "A local politician",
    "A famous actor",
    "A school principal",
    "A government officer",
    "A social media influencer",
    "A scientist",
    "A businessman",
    "A doctor",
    "A university student",
    "A tech CEO",
    "A retired army officer",
    "A YouTuber",
    "A film director",
    "A billionaire",
    "A cricket player",
    "A football coach",
    "An environmental activist",
    "A startup founder",
    "A popular singer"
]

actions = [
    "was arrested for carrying fake currency",
    "was caught dancing on the road",
    "announced free smartphones for everyone",
    "claimed to have seen aliens",
    "was found selling invisible clothes",
    "promised to make internet free for 10 years",
    "was caught teaching monkeys",
    "opened a school for superheroes",
    "was found hiding gold under the bed",
    "claimed that the Earth is flat",
    "started a company to sell air",
    "was seen arguing with a robot",
    "promised flying cars by next year",
    "claimed to invent a time machine",
    "was caught training cats",
    "launched shoes that can talk",
    "promised to build a city on the moon",
    "was caught using magic",
    "claimed to cure all diseases",
    "was seen running a secret lab"
]

places = [
    "in Rayagada",
    "in New Delhi",
    "in Mumbai",
    "in Bengaluru",
    "in Chennai",
    "in Hyderabad",
    "in a shopping mall",
    "inside a metro station",
    "at the airport",
    "in a hospital",
    "inside a school campus",
    "near a famous temple",
    "on a busy highway",
    "inside a government office",
    "at a cricket stadium",
    "in a five-star hotel",
    "inside a university",
    "on social media",
    "inside a cinema hall",
    "at a tech conference",
    "inside a restaurant"
]

extras = [
    "according to secret sources.",
    "which shocked the entire nation.",
    "leaving everyone confused.",
    "as reported by unknown witnesses.",
    "which created panic on social media.",
    "sparking huge controversy.",
    "causing massive internet memes.",
    "and people are demanding answers.",
    "raising serious security concerns.",
    "which went viral instantly."
]

# Headline generator
while True:
    subject = random.choice(subjects) #random.choice() is use for selecting a random item from the list
    action = random.choice(actions)
    place = random.choice(places)
    extra = random.choice(extras)
    
    headline = f"BREAKING NEWS: {subject} {action} {place}, {extra}" #f is use for formatting the string and {} is use for inserting the variable value in the string and creating a complete sentence
    print("\n" + headline + "\n")

    user_input = input("Do you want to generate another headline? (yes/no): ").strip().lower() #..strip() is use for removing extra spaces and .lower() is use for converting upper case to lower case
    if user_input == 'no': 
        break

print("Thank you for using the Fake News Headline Generator!")
