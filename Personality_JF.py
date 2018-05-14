import time
name = "Josh"
state = "Florida"
city = "new york city"
game = "steep"
book = "Tina Fey"

print(name + " likes to visit " + state + " and " + city)
print("He also likes pwning on " + game + " or reading " + book)

print("What's your favorite subject?")
subject = input ()

if subject == "math":
    print("That's awsome!")
else:
    print(subject + " is a good course too.")


print("What's your favorite sport?")
sport = input()

if sport == "Baseball" or sport == "Basketball":
    print("I love " + sport + " too!")
else:
    print(sport + " is pretty fun.")


print("Favorite movie?")
movie = input()

if movie == "42":
    print("What is that?")
elif movie == "Blind Side":
    print("Woah!")
else:
    print("I've never seen " + movie)

time.sleep(100)
    
    


      
    
