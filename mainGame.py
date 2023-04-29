# Importing art
from asciiArt import *

# Importing modules
import os
from getpass import getpass
from time import sleep
class Format:
    end = '\x1B[0m'
    underline = '\x1B[4m'


# \\\\\\\\ ** FUNCTIONS!!! ** \\\\\\\

# Menu options:
def menu(choice1 = "", choice2 = "", choice3 = "", choice4 = "", choice5 = ""):
    myList = [choice1, choice2, choice3, choice4, choice5]
    letterStart = 64
    index = -1
    correctAnswer = False
    listOfChoices = []
    answer = ""
    print("-----------------")
    
    for item in myList:
        index += 1
        letterStart += 1
        if item == "": 
            continue
        print(chr(letterStart) + ") " + item)
        listOfChoices.append(chr(letterStart))
        sleep(0.3)
    print("-----------------")

    while correctAnswer == False:
        try:
            answer = input("> ")
            answer = answer.upper()
            if listOfChoices.index(answer) != -1:
                correctAnswer = True
                return(listOfChoices.index(answer)+1)
        except ValueError:
            if answer == "":
                continue
            else:
                print("")
                print("Sorry, that's not an option!")
                print("")
    print("")
    

# Clear the screen:
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


# Animations:
# This function gets the first frame you want to show up. Then it gets the 
# second frame you want to appear. Next, it gets the time between each frame. 
# And lastly, the 'loops' (how many times you want the animation to repeat).
def animation(frame1, frame2, timeBetweenFrames, loops):
    for i in range(loops):
        print(frame1)
        
        sleep(timeBetweenFrames)
        
        cls()
        
        print(frame2)
        
        sleep(timeBetweenFrames)
        
        cls()


# Animating text:
def textAnimation(sentence, timeBetweenLetters=0.02):
    chars = sentence
    loop = range(1, len(chars) + 1)
    
    for idx in loop:
        print(chars[:idx], end='\r') # <-- end with carriage return
        sleep(timeBetweenLetters)
    print("")
 
    
# Phone message:
def phoneMessage(message):
    message = str(message)
    messagePart1 = message
    messagePart2 = "             "

    
    if len(message) > 13:
        messagePart1 = message[:13]
        messagePart2 = message[13:]
        
        
        if len(messagePart2) > 13:
            messagePart2 = messagePart2[:10] + "..."
        
        else:
            difference = 13 - len(messagePart2)
            messagePart2 = messagePart2 + (" ") * difference
    else:
        difference = 13 - len(messagePart1)
        messagePart1 = messagePart1 + (" ") * difference
    
    print("""
       _
      | |
      |_|
      /_\    \u001b[32m\ | /\u001b[0m
    .-" "------.----.
    |          U    |
    |               |
    | ====o======== |
    | ============= |
    |               |
    |_______________|
    | ________GF337 |
    ||"""+messagePart1+"""||
    ||"""+messagePart2+"""||
    ||_____________||
    |__.---" "---.__|
    |---------------|
    |[Yes][(|)][ No]|
    | ___  ___  ___ |
    |[<-'][CLR][.->]|
    | ___  ___  ___ |
    |[1__][2__][3__]|
    | ___  ___  ___ |
    |[4__][5__][6__]|
    | ___  ___  ___ |
    |[7__][8__][9__]|
    | ___  ___  ___ |
    |[*__][0__][#__]|
    `--------------'
    {__|""|_______'-
    `---------------'
    
    """)
    

# Game Over screen:
def gameOver(time, sentence=""):
    cls()
    print("""

  /$$$$$$                                   
 /$$__  $$                                  
| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
| $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$
| $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$
| $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/
|  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$
 \______/  \_______/|__/ |__/ |__/ \_______/
    """)
    
    sleep(time)
    
    print("""
  /$$$$$$                               
 /$$__  $$                              
| $$  \ $$ /$$    /$$ /$$$$$$   /$$$$$$ 
| $$  | $$|  $$  /$$//$$__  $$ /$$__  $$
| $$  | $$ \  $$/$$/| $$$$$$$$| $$  \__/
| $$  | $$  \  $$$/ | $$_____/| $$      
|  $$$$$$/   \  $/  |  $$$$$$$| $$      
 \______/     \_/    \_______/|__/      
                                        
    """)
    
    sleep(0.25)
    
    textAnimation(sentence)
    quit()

            
# Make background go black (only for web Python interpreters):  
def blackground(sentence = ""):
    print('\x1b[40m''\x1b[97m')
    print(" " * 9999)
    cls()


# Make background go white (only for web Python interpreters):     
def whiteBackground(sentence = ""):
    print('\u001b[0m')
    print(" " * 9999)
    cls()
        
# ------------ GAME INTRODUCTION -------------------------:

getpass(title) 
    
animation(animationLetter1, animationLetter2, 0.3, 5)    
    
getpass(letter1)

cls()

getpass(letter2)

getpass("It says:")

cls()

getpass(grandpa1)

cls()

getpass(grandpa2)

cls()

print(grandpaAnimation1)
sleep(1)

cls()

print(grandpaAnimation2)
sleep(0.3)

cls()

print(grandpaAnimation3)
sleep(1.4)

cls()

print(grandpaAnimation4)
sleep(0.3)

cls()

print(grandpaAnimation5)
sleep(1)

cls()

getpass(grandpa3)

cls()

getpass(grandpa4)

cls()

getpass(grandpa5)

cls()

getpass(grandpa6)

getpass("...")
print("")
print("So, what do you say?")
sleep(1)
cls()

print(grandpa6)

print("...")
print("")

# First Choice
print("So, what do you say? (to yourself because this is a letter..)")
sleep(0.8)
print("")
mainQuest = menu("Yeah, sure!", "No way, weirdo moustache man.", "WHHHHHAAAAAAT")
     
# WHAAAAAAT choice    
if mainQuest == 3:
    print("")
    textAnimation("'WHAAAAAAAAAAAAAAAT!!!'")
    print("")
    sleep(0.5)
    getpass("[You scream.]")
    print("")
    textAnimation("'WHAAAAAAAAAAAAAAAAAAAAAAAAT!!!!!'", 0.01)
    sleep(0.5)
    print("")
    getpass("[You scream more..]")
    print("")
    sleep(0.25)
    textAnimation("'WHAAAAA-'", 0.1)
    print("")
    sleep(0.7)
    getpass("[You decide to stop screaming.]")
    
    print("")

    mainQuest = menu("Yeah, sure!", "No way, weirdo moustache man.")

# Deny quest choice
if mainQuest == 2:
    print("")
    textAnimation("[That's right! Your mom teached you never to answer weird grandpas letters!!!]", 0.02)
    getpass("> ")
    print("")
    sleep(0.05)
    cls()
    textAnimation("[You tear the letter in tiny little pieces.]")
    getpass("")
    print("[Well... What now?]")
    input("> ")
    
    cls()
    
    gameOver(1, "oh.. so that's what happens next")

# Quest accepted choice
else:
    cls()
    sleep(1)
    print(questAccepted1)
    sleep(0.8)
    cls()
    print(questAccepted2)
    sleep(1.3)
    textAnimation("[" + Format.underline + "Objective: Find Master Oogway!" + Format.end + "]") 
    print("")
    sleep(1)
    getpass("> Begin game!")
  
cls()
sleep(0.3)

# Getting to master Oogway
print("Alright, so..." + "\n")
sleep(0.7)
print("")

getToMasterOogway = 0

while getToMasterOogway != 3:
    textAnimation("How are you finding Master Oogway?")
    sleep(0.5)
    getToMasterOogway = menu("Call", "Send a message.", "Telepathy!")
    cls()
    
    # Send a message choice
    if getToMasterOogway == 2:
        sleep(0.25)
        print(phoneOff1)
        sleep(1)
        
        print("Oh.")
        sleep(0.5)
        textAnimation("It looks like you need to turn your phone on!")
        getpass("> Turn phone on!")
        sleep(1)
        cls()
        
        animation(phoneOff1, phoneOff2, 0.15, 10) 
        print(phoneOn)
        
        print("")
        textAnimation("What will you send to him?")
        message = input("Type your message now > ")
        cls()
        
        phoneMessage(message)
        print("")
        
        getpass("> Send message!")
        
        cls()
        
        print(phoneSending)
        textAnimation(". . .", 1.3)
        print("")
        textAnimation("oh...")
        sleep(0.5)
        
        print("")
        textAnimation("[You suddenly remember that Master Oogway doesn't have a phone.]")
        getpass("")
        cls()
        
        print(" ")
        
    # Call choice
    if getToMasterOogway == 1:
        sleep(0.25)
        print(phoneOff1)
        sleep(1)
        
        print("Oh.")
        sleep(0.5)
        textAnimation("It looks like you need to turn your phone on!")
        getpass("> Turn phone on!")
        sleep(1)
        cls()
        
        animation(phoneOff1, phoneOff2, 0.15, 10) 
        print(phoneContacts)
        
        print("")
        
        textAnimation("Who are you calling?")
        calling = menu("Weird Grandpa", "Mom", "Jeremiah", "Master Oogway")
        cls()
        print(phoneCalling)
        
        textAnimation(". . .", 0.3)
        print("")
        
        getpass("[It is calling.]")
        print("")
        
        textAnimation(". . . .", 0.3)
        sleep(0.25)
        print("")
        
        getpass("[It is still calling.]")
        print("")
        
        textAnimation(". . . . .", 0.3)
        sleep(0.25)
        print("")
        
        print("[It is-]")
        sleep(0.5)
        cls()
    
        # Calling Grandpa
        if calling == 1:
            print(phoneGrandpa)
            textAnimation("- Hey, son!")
            sleep(0.5)
            print("")
            
            getpass("> Hey")
            print("")
            
            textAnimation("- Have you received my letter?")
            sleep(0.5)
            received = menu("Yes, terrible handwriting by the way...", "Nope.")
            print("")
            
            if received == 1:
                textAnimation("- I am trying to get better ok? So, what I have here is...")
                getpass("")
                
            else:
                textAnimation("- Haven't you? Well, what I have here is...")
                getpass("")
                
            textAnimation("- OH NO!! WAIT, STAY IN THE LI- ")
            sleep(1.5)
            
            
        # Calling Mom
        if calling == 2:
            print(phoneMom)
            textAnimation("- Hello?")
            sleep(0.5)
            print("")
            
            getpass("> Hey")
            print("")
            
            textAnimation("- Oh, it's you, honey! I would recognize your voice anywhere in this world!")
            getpass("")
            textAnimation("- I miss you, y'know? You should call me more...")
            print("")
            getpass("> Sorry mom... ")
            print("")
            textAnimation("- Are you enjoying independent life so far?")
            sleep(0.5)
            received = menu("Yes, I can join crazy quests!", "No, I miss your cookies.")
            print("")
            
            if received == 1:
                textAnimation("- Ohh, son! Take care in your journey!!!")
                getpass("")
                
            else:
                textAnimation("- Hahahah. Don't worry. You'll have as many as you want when you come back home! ♥")
                getpass("")
                
            textAnimation("- Call me more, whenever you want! ")
            getpass("")
            
            
        # Calling Dog
        if calling == 3:
            print(phoneDog)
            textAnimation("[You hear some barking sounds on the otherside of the line.]")
            sleep(0.5)
            print("")
            
            getpass("> Hello?")
            print("")
            
            textAnimation("- Woof!")
            getpass("")
            
            textAnimation("[Oh. It is Jeremiah! The dog with a phone!]")
            getpass("")
            textAnimation("What will you say as a compliment?")
            sleep(0.2)
            print("")
            
            menu("Woof", "Woof woof", "Woof woof Woof woof", "Wooooooooof", "wof")
            
            print("")
            textAnimation(". . .", 1)
            print("")
            
            textAnimation("- WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOFFFFF")
            getpass("")
            cls()
            textAnimation("[You decide it's enough barking.]")
            getpass("")
            
            
        # Calling Master Oogway
        if calling == 4:
            print(phoneOogway)
            textAnimation("- Hi!!")
            sleep(1)
            print("")
            textAnimation("[You feel like Master Oogway voice is different since last time you heard it.]")
            sleep(0.5)
            getpass("")
            
            getpass("> Master Oogway?")
            print("")
            
            textAnimation("- Master what?")
            print("")
            getpass("> Who's talking?")
            print("")
            
            textAnimation("- It's me, Mr. Lamont! Isn't it obvious??")
            getpass("")
            textAnimation("[Woah! You might have saved Mr. Lamont's number with a wrong contact name!]")
            getpass("")
            
            textAnimation("- Helloooooo???")
            print("")
            getpass("> Oh, sorry, Mr. Lamont! I called the wrong number.")
            print("")
            
            textAnimation("- Ah, hahahaha. Don't worry!")
            sleep(0.5)
            print("")
            
            textAnimation(". . .", 1)
            print("")
            
            textAnimation("- Wait, have you finished my flow chart yet?")
            getpass("")
            cls()
            
            textAnimation("[YOU DECIDED IT WAS ENOUGH TALKING!!!]")
            getpass("")
        
    if getToMasterOogway == 1:
        cls()
        textAnimation("[The call was ended.]")
        getpass("")
        cls()
    
    
    if getToMasterOogway != 3:
        cls()
        textAnimation("[You turned your phone off.]")
        getpass("")
        cls()

# Telepathy choice
textAnimation("[You get a pillow and sit on it in a lotus pose.]", 0.1)
getpass("")
sleep(0.2)
blackground()
textAnimation("[You close your eyes.]", 0.1)
getpass("")
cls()

textAnimation("[You stay in silence for a bit]")
textAnimation("[. . .]", 0.3)
getpass("")
cls()
textAnimation("[You concentrate your thoughts into your objective]", 0.1)
textAnimation("[. . .]", 0.3)
getpass("")
cls()

textAnimation("[You feel a river flow through your mind]", 0.1)
textAnimation("[. . .]", 0.3)
getpass("")
cls()

print(aardvark)
textAnimation("- Oh hey!")
print("")
sleep(0.3)
getpass("> Hey! Who are you?")
print("")
textAnimation("- Oh, I am Mark! Mark the Aardvark")
print("")
getpass("> Where are we, Mark?")
cls()

print(aardvark)
textAnimation(". . . ?", 0.8)
textAnimation("- Now that you talked about it... Inside your head I guess.")
getpass("")

questionMark = menu("I need to talk to Master Oogway!", "What are you doing inside my head, Mark?")
cls()

print(aardvark)
print("")

if questionMark == 2:
    textAnimation("- How come?!")
    sleep(0.3)
    textAnimation("- This is what I do for a living!")
    textAnimation("- I am your mental aardvark, everyone has one!")
    getpass("")
    getpass("> I need to talk to Master Oogway!")
    print("")


textAnimation("- Oh, you need to use the telepathy system!")
textAnimation("- Follow your path to the right and keep thinking about sci-fi!")
textAnimation("- At some point, you will see a sign 'TELEPATHY AREA' or something...")
textAnimation("- When you get to this sign, just think about whoever you want to connect with!")
getpass("")
getpass("> Thank you, Mark the Aardvark!")
cls()

textAnimation("[You walk slowly, as the world is generated under your feet]")

getpass("")
cls()

textAnimation("[You see a sign:]")
sleep(0.5)
print(signTelepathy)
getpass("")
thinkOption = menu("Think about Master Oogway", "Think about bananas")
cls()

# Bananas option
if thinkOption == 2:
    textAnimation(". . .", 0.5)
    print("")
    textAnimation("[You feel the sweet power of bananas running through your veins.]")
    getpass("")
    cls()
    print(banana)
    textAnimation(". . .", 0.3)
    print("")
    textAnimation("[You start wondering what would be like to be a banana...]")
    getpass("")
    cls()
    textAnimation("[You feel the transformation occuring...]")
    textAnimation("[. . .]", 0.3)
    getpass("")
    cls()
    print(bananaFace)
    print("")
    textAnimation("[You are now a BANANA!]")
    getpass("")
    cls()
    print(bananaFace)
    textAnimation("[You lost track of your mission!]")
    sleep(0.2)
    textAnimation("[Because bananas don't care about missions.]")
    getpass("")
    gameOver(1, "you got the 'Banana Ending'!")

# Master Oogway option
textAnimation(". . .", 0.5)
print("")
textAnimation("[You feel connected.]")
getpass("")
cls()
textAnimation("[You hear the noisy silence]")
print("")
getpass("> Master Oogway?")
print("")
textAnimation(". . .", 0.5)
print("")

textAnimation("- H-hello?")
print("")
sleep(0.3)
textAnimation("[You'd recognize his voice anywhere!]")
print("")
sleep(0.7)
getpass("> MASTER OOGWAY!!!")
print("")
cls()

print(oogway)
sleep(0.5)
textAnimation("- Wait! Who's talking?", 0.1)
sleep(0.3)

print("")
playerName = input("> It is me, [TYPE YOUR NAME]: \u001b[33m")
print('\x1b[40m''\x1b[97m')
sleep(0.3)

# Master Oogway presentation
textAnimation("- OOHH!!! Greetings, " + playerName + ", my friend!")
textAnimation("- It's been so long since our last talk... What do you need?")
sleep(1)

print("")
getpass("> MASTER OOGWAY WE NEED TO GO TO MY GRANDPA'S HOUSE!")

print("")
textAnimation("- ALRIGHT!")
textAnimation("- Where are we gonna meet up?")
sleep(0.5)
print("")
place = input("> We are gonna meet at [TYPE THE LOCATION]: \u001b[33m")
print('\x1b[40m''\x1b[97m')

print("")
textAnimation("- At " + place + "? Sounds good!")
sleep(0.2)
textAnimation("- See you there!")
getpass("")
cls()

whiteBackground()

# Meeting Oogway
textAnimation("[You suddenly wake up from your meditation!]")
getpass("")
cls()

textAnimation("It's time to pack your things. Your journey is about to begin!")
getpass("")
cls()

sleep(1)
print(ending)
sleep(0.8)
cls()
print(ending2)
sleep(1.3)
textAnimation("Thanks for playing, " + playerName + "!")
print("")
textAnimation("Created by Victor Fatala and Brian Ho")

