import random
print ("Your party of adventurers is sitting around the fire after a day of adventuring.")
print("The bard of your party suddenly stands up.")
print("He strums his lute, and announces that he's going to tell a story")

#This is how the story is determined. I may make it have bearing on plot,
class story:
    def __init__(self, genre, badGuy, damsel, goodGuy, treasure, location, fortress):
        self.genre = genre
        self.badGuy = badGuy
        self.damsel = damsel
        self.goodGuy = goodGuy
        self.treasure = treasure
        self.location = location
        self.fortress = fortress
    def tellStory(self):
        if genre == "adventure":
            print("Once, there was a " + damsel + " who lived in a " + location + " in the very kingdom we inhabit.")
            print("One day they were kidnapped by a " + badGuy + " because they guarded the " + treasure + ". ")
            print("The " + treasure + " was the most valuable treasure in the kingdom, and was coveted by the " + badGuy + ".")
            print("The " + damsel + " was taken by the " + badGuy + " to the " + fortress + ".")
            print("There, the " + damsel + " still lives to this day.")

        elif genre == "space":
            print("Once, there was a great and terrible ship named the UMS Sparkle. ")
            print("At the helm of the UMS Sparkle there was a " + goodGuy + " who was protecting a " + damsel + " and ")
            print("the " + treasure + ", which was the most valuable treasure known to planet Aeris.")
            print("One cycle, on normal duty, the ship was attacked by Space Pirates, led by the Dread Captain " + badGuy + ".")
            print("Captain " + badGuy + " led the charge to the bridge where the " + treasure + ", " + damsel + " and the " + goodGuy + " were.")
            print("The Captain and the " + goodGuy + " engaged in a sword fight, but the " + goodGuy + "lost and was killed.")
            print("The Captain of the pirates took the escape pod, and the " + treasure + " and the " + damsel + ".")
            print("They left to the " + fortress + " on planet Aeris, and to this day remain still.")

        elif genre == "western":
            print("Once, in a small desert town, there was a " + damsel + " who was the most beautiful thing in the town.")
            print("In this town, the " + damsel + " protected the " + treasure + " while living in a " + location + ".")
            print("One particularly hot day, a gang, led by a " + badGuy + ", invaded the town looking for the  " + treasure + ".")
            print("The " + damsel + "'s friend, " + goodGuy + ", defended them, but lost.")
            print("The gang found the " + treasure + " and absconded with the " + damsel + " and " + goodGuy + ".")
            print("Supposedly, the gang headed back to their headquarters, a " + fortress + " somewhere out in the desert.")

#Lists of the nouns that the stories all use.
genres = ["adventure", "space", "western"]

badGuys = ["Dragon", "Space Dragon", "Radioactive Octopus", "Centaur Stack", "Bundle of Plastic Straws", "Horde of Space Pirates"]

damsels = ["Princess", "Space Prince", " Litter of Kittens", "Sea Turtle", "Bald Eagle Chicks", "Cockatiel named Lemmy"]

goodGuys = ["Princess", "Prince", "Space Princess", "Space Prince", "Bounty Hunter", "Box of Cheddar Cheese Crackers", "Radioactive Octopus"]

treasures = ["Voice of Lemmy", "Eye of Mahnihcuh", "Ice Blade", "Band of Gales", "Baton of Water", "Rod of Holy Lightning"]

locations = ["Castle", "Typical American House", "Luxury Apartment", "Reasonably Priced Condo", "Small Trailer", "Mansion"]

fortresses = ["Spooky Hospital", "Abandoned Laboratory", "Maid Cafe", "Call Center", "Shuttered Factory"]

events = ["event1", "event2", "event3", "event4", "event5"]

eventtypes = ["Spooky Skeleton", "Public Transit", "Witches House", "Mysterious Fridge", "Creepy Church", "Graveyard Ghouls", "Retail Store"]

#Determines what nouns are assigned to the variables, randoomly, of course
genre = random.choice(genres)
badGuy = random.choice(badGuys)
damsel = random.choice(damsels)
goodGuy = random.choice(goodGuys)
treasure = random.choice(treasures)
location = random.choice(locations)
fortress = random.choice(fortresses)
storyTime = story(genre, badGuy, damsel, goodGuy, treasure, location, fortress)
storyTime.tellStory()



print("The bard sets his lute down, and looks at the party.")
print("Supposedly this story is true, you know, the bard says.")
print("We must find the " + treasure + "and defeat the " + badGuy + ".")
print("The party looks at each other, kind of grumbling because this was supposed to be their day off")
print("But leave it to the player of this game to drag them out on another adventure.")
print("The Bard looks on  with wide eyes, praising the player silently, while the party picks up their gear.")
print("The party sets off into the foggy night, without so much as a word between them")

#Initializes x & y to prevent bugs
x = 1
y = 1

#This is supposed to be a rudementary thing, I haven't debugged this yet, I think
while x in range (1,11) and y in range (1,11):
    command = input("What would you like to do?")
    if "north" in command.lower() and y <= 10 and y > 0:
        y += 1
        print(y)
        print("The party walks north, the moonlight shining brightly upon them.")
    else:
        print("A thick fog forms in front of the party, and the party is unable to continue.")
    if "south" in command.lower() and y <= 10 and y > 0:
        y -= 1
        print(y)
        print("The party walks south, wolves howling in the distance.")
    else:
        print("A thick fog forms in front of the party, and the party is unable to continue.")
    if "east" in command.lower() and x <= 10 and x > 0:
        x += 1
        print(x)
        print("The party walks east, the breeze causing chills in the night air")
    elif x >= 11:
        x -= 1
        print("A thick fog forms in front of the party, and the party is unable to continue")
    if "west" in command.lower() and x <= 10 and x > 0:
        print(x)
        print("The part walks east, the leaf litter crunching under their feet.")
    else:
        print("A thick fog forms in front of the party, and the party is unable to continue.")