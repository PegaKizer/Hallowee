import random

print("Welcone to Halloween by Jonah Kizer.")
print(
    " Halloween is an interactive story game were inorder to save your friends lifes you must answer 3 questions. "
    + "However these questions wont be so easy for they will be in French, Spanish and English."
)
print(
    "The story starts off with your and 5 of your friends going trick or treating late into the night. "
    + " At around 10:30 you and your friends decide to head back to your house for the sleepover. "
    + " When you get to your house you decide to watch a movie (the terifier) "
    + " mid way through the movie you hear a thunk however you quickly shrug it off. "
    + " Later your friend goes to the bathroom and never comes back. "
    + "You and your friend go to look for him but hes nowhere to be found. "
    + " Slowly one by one you notice your friends go missing and that its just the three of you left when..."
    + "The door slowly creeks open and you see a clown standing holding your friends hostage, when the clown tells you "
    + " the only way to save them is by answering these 3 questions if you get one question wrong two of your friends die."
    + " If you get two questions wrong another 2 friends die, and if you get all questions wrong YOUR ALL DEAD!"
)

# Player will have a max a 3 guesses.
MAX_GUESSES = 3
# Answer in with the first letter capitalized 
List_of_possible_questions = [
    [
        "En francais como dit-on 'I would like to play tennis?",
        "Je voudrais jouer au tennis",
    ],
    [
        "En Espanol que tu dijiste 'translates to what in french?",
        "Qu'est ce que tu as dit",
    ],
    [
        "En Francais Je voudrais jouer au tennis, mais je ne peux pas parce que j'ai mal au coude translates to what in english?",
        "I would like to play tennis but I cant because my elbow hurts",
    ],
    [
        "What river makes up 1/2 of the US/Mexico border? Answer in French.",
        "La rivere grande",
    ],
    ["En cual idioma tu dices 'Volia?", "Francais"],
]
friends_remaining = 6
guesses = 0
MAX_GUESSES = 3
questions_answered = 0

random.shuffle(List_of_possible_questions)
possible_questions = List_of_possible_questions[:3]

for question, answer in possible_questions:
    guess = input(question)
    print(guess)
    guesses += 1
    if guess != answer:
        print("Two of your friends die!")
        friends_remaining = friends_remaining - 2
        print("You now have " +  str(friends_remaining) + " remaining friends.")
        print(answer)
    if guess == answer and guesses <= MAX_GUESSES:
        print("Congradulations you saved two of your friends lives.")
        questions_answered = questions_answered + 1 
        questions_remaining = 3 - questions_answered
        if questions_remaining >0: 
            print(f"You have {str(questions_remaining)} more questions to answer if you wish to walk off unscaved.")
        if questions_remaining == 0 :
            print("You have 0 questions remaining, I knew you could do it")
       
    
if friends_remaining == 6:
    print("You win, I knew you could do it, bye!")
    # Now you have a choice grab the knife from the kitchen and stab him to death or let him go free 
    Kill_clown_choice = input("Kill clown or let clown go free?: ").lower()
    if Kill_clown_choice == "kill clown":
        print("get moving, you have little time before he disapears!")
        print("Your friend says, \"Quick, get a knife from the kitchen!\"")
        destination_choice = input("Do you want to go to the garage or the kitchen?").lower()
        while destination_choice not in ["kitchen", "garage"]:
            destination_choice = input("Please type Kitchen or Garage").lower()
        if destination_choice == ("kitchen"):
            weapon_choice_kitchen = input("Do you want to grab a knife from the kitchen or a axe?").lower() 
            while weapon_choice_kitchen not in ["knife", "axe"]:
                weapon_choice_kitchen = input("please type Knife or Axe").lower()
            if weapon_choice_kitchen == ("knife"):
                print("You run after the clown and stab him in the back!")
            if weapon_choice_kitchen == "axe":
                print("You slice the clowns head off with the axe. He is DEAD!")
        if destination_choice == "garage":
            weapon_choice_garage = input("Would you like to grab a bat or a fire extinguisher?").lower()
            while weapon_choice_garage not in ["bat", "fire extinguisher"]:
                weapon_choice_garage = input("please type Bat or Fire Extinguisher.").lower()
            if weapon_choice_garage == "bat":
                print("You chase after the clown and whack him on the head with a bat. He is dead")
            if weapon_choice_garage == "fire extinguisher":
                print("You chase after the clown and whack him on the head with the fire extinguisher. He is dead")
    if Kill_clown_choice == "let clown go free":
         print("You and your friends return to your movie.")

if friends_remaining not in [0, 6]:
    print("YOU FAILED!")

if friends_remaining == 0: 
    print ("Well I gave them a chance.")
   