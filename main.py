import random
import time
import sys
import assets

# spaghetti time
# so many if else statements kill me

characters = ["Black", 'Red', 'Green', 'Blue', 'Yellow', 'Cyan']
crewmates = ["Black", 'Red', 'Green', 'Blue', 'Yellow', 'Cyan']
roomlist = [
    'the medbay', 'the electrical', 'the main lobby', 'the security room',
    'the engine room'
]
cutusedrooms = []
karma = 0
roundkill = ''

def dotdotdot():
    print('\n')
    typeprint("...", 0.5)
    print('\n\n')


def nocrewmatesremainingcheck():
    # one crewmate left == endgame
    if len(crewmates) <= 1:
        print(
            "With only one crewmate on board left, the ship is overtaken by the controls of the impostor."
        )
        printending("impostor victory")
        exit(0)
def narrator(txt, delay=True, end='\n\n'):
  print(txt, end=end)
  if delay:
    time.sleep(1.5)
  else:
    input("")

def ejection(ejected):
  typeprint(f"The majority votes {colorprint(ejected, ejected)}.")
  if ejected == impostor:
    print(assets.was_impos)
    print(f"{impostor} was the imposotor.")
  elif ejected == user:
    print("You have been ejected.")
    print(assets.was_not_impos)
    print(f"{user} was not the impostor.")
  else:
    print(assets.was_not_impos)
    print(f"{ejected} was not the impostor.")
    nocrewmatesremainingcheck()
  
def colorprint(txt, color):
    black = "\033[1;90m"
    red = "\033[0;31m"
    green = "\033[0;32m"
    yellow = "\033[0;33m"
    blue = "\033[0;94m"
    cyan = "\033[0;36m"

    white = "\033[0;37m"
    return eval(color.lower()) + txt + white


def typeprint(text, delay=0.03):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)


def dialogue(speaker, text):
    print("__________________________\n")
    print(f"{colorprint(speaker, speaker)}: ", end='')
    typeprint(text)
    print("\n__________________________\n")
    time.sleep(1)


def doaction(action="REACT"):
  start = time.time()
  userans = input(f"\nQuick! Type {colorprint(action.upper(), 'red')} within 3 seconds: ")
  end = time.time()

  if (end - start) > 3:
    colorprint("\nYou either took too long, or you have a typo. You have failed the task...\n", 'red')
    time.sleep(2)
    return False

  if userans.strip(' ').lower() == action.lower():
    print(f"\nYou were able to sucessfully {colorprint(action.upper(), 'green')}.\n")
    time.sleep(2)
    return True

  else:
    print(f"You have failed to {action.upper()}.")
    time.sleep(2)
    return False

  
  
def luck(max='6'):
    userans = input(f"Input a number from 1 to {max}: ").strip()
    x = random.randint(1, max)
    while not userans.isnumeric() and max >= int(userans) >= 1:
        userans = input(
            f"\nSorry, your answer isn't numeric, or isn't within the bounds (1-{max}). Try again:  "
        ).strip()

    # # always return true for testing purposes
    # if test == True:
    #     return True

    dotdotdot()
    if userans == x:
        return True
    else:
        return False


def taskmath():
    x = random.randint(1, 99)
    y = random.randint(1, 99)
    userans = input(f"\nWhat is {x} + {y}?: ").strip()

    while not userans.isnumeric():
        userans = input(
            "\nSorry, your answer isn't numeric. Please enter in a integer: "
        ).strip()

    correctans = x + y

    if int(userans) == correctans:
        colorprint("\nYou're right.\n", 'green')
        return True
    else:
        colorprint(f"Incorrect. The correct answer is {correctans}.", 'red')
        return False


def tasktrivia():
    qna = {
        "What game studio created Among Us?": 'innersloth',
        "Which is the smallest planet within our solar system?": "mercury",
        "Which planet has supersonic winds?": 'neptune',
        "Which planet rotates on its side?": "uranus",
        "Which planet has the most volcanoes?": "venus",
        "Which is the oldest planet in our solar system?": 'jupiter',
        "Which planet has the most moons?": 'saturn'
    }
    question = random.choice(list(qna))
    userans = input(f"{question}: ").strip(' ').lower()

    if userans == qna[question]:
        colorprint("\nYou're right.\n", 'green')
        return True
    else:
        colorprint(
            f"\nThat is incorrect. The correct answer is {qna[question]}.\n",
            'red')
        return False


# user


def kill():
    global roundkill
    roundkill=random.choice(crewmates)
    crewmates.remove(roundkill)
    nocrewmatesremainingcheck();

def getyesno(prompt):
    useroption = input(prompt + " (Y/N): ").lower().strip(" ")
    while useroption not in ("n", "y"):
        useroption = input(f"Input a proper answer: ").strip(
            ' ').lower()
    if useroption == "y":
        return True
    else:
        return False


def karmastate():
    if 200 > karma > -200:
        return 'yellow'
    if karma >= 200:
        return 'green'
    if karma <= -200:
        return 'red'


def colorkarma():
    state = karmastate()
    if state == 'green':
        return '\033[0;32m' + str(karma) + '\033[0;37m'
    if state == 'yellow':
        return "\033[0;33m" + str(karma) + '\033[0;37m'
    if state == 'red':
        return "\033[0;31m" + str(karma) + '\033[0;37m'


def updatekarma(change):
  color = ''
  global karma
  
  if change > 0:
    color = '\033[0;32m'
  else:
    color = '\033[0;31m'

  karma += change

  print("\n")
  if(change > 0):
    print(f"Karma: {color}+{str(change)}\033[0;37m")
  else:
    print(f"Karma: {color}{str(change)}\033[0;37m")

  print(f"You have {colorkarma()} karma.")
  narrator("\nHit enter to continue.", delay=False)

def printending(ending, userdeath=False):
  print(f"\nYou have achieved the {colorprint(ending.upper(), 'blue')} ending.\n")
  print(f"You had {colorkarma()} karma.\n")
  crewmates.remove(impostor)
  if userdeath == True:
        crewmates.clear()
        colorprint(
            "Without you on the ship, the crewmates were unable to uncover the identity of the impostor. Nobody survives.\nWithout any maintenence, the ship breaks down.",
            'red')
  if len(crewmates) > 4:
        colorprint(f"{str(1+len(crewmates))} crewmates survived.", 'green')
        return
  elif len(crewmates) == 1:
        colorprint("You and one crewmate remains on the ship.", 'red')
        return
  else:
    colorprint(f"{str(1+len(crewmates))} crewmates survived.", 'yellow')
  return


def crewmatecut():

  # setup
  charactercut = random.choice(crewmates) # character to interact with
  roomcut = random.choice(roomlist) # setting room
  roomlist.remove(roomcut) # no longer use this room for any more cutscenes

  # room scenarios
  
  if roomcut == 'the medbay':
    narrator(f"You enter the medical room to find {charactercut}.")
    if getyesno(f"They're doing their medical scan. Would you like to check?"):
      
      narrator("You decide to gather some intel...")
      
      narrator(f"Looking at {charactercut}'s scan, they seem to have very normal human biology.")
      
      narrator(f"{charactercut} probably isn't the impostor.")
      
      updatekarma(50)
    else:
      narrator("You decide to mind your own buisness.")
         
      narrator("You did lose out on intel though, and for that, your karma will go down.")
      
      updatekarma(-50)
    
  if roomcut == 'the electrical':
    narrator("The lights have turned off, so you go to the electrical to fix it.")
    narrator(f"Fortunately, {charactercut} is already there, and is fixing the lights.")
    dialogue(charactercut, "Have you come to fix the lights, or to kill me?")
    dialogue(user, "Haha, I've come to help you fix the lights.")
    narrator("The two of you help fix the lights, and you both move on to do other tasks.")
    updatekarma(100)
  
  if roomcut == 'the main lobby':
    narrator(f"While walking towards {roomcut}, you pass by {charactercut}.")

    s = input("Enter in the inclusive range of 1 - 4: ")
    while (int(s) in range(1, 5, 1)):
        s = input("Sorry, that input didn't work - please try again.")

    if s == 1:
        dialogue(charactercut, f"Hey, {user}!")
        dialogue(user, "Hi.")
        dialogue(charactercut, f"Enjoying the weather?")
        dialogue(user, "We're in space.")
    if s == 2:
        narrator("You exchange greetings, and head opposite ways.")
    if s == 3:
        dialogue(charactercut, "Why did the kitchen cross the road?")
        dialogue(user, "Is it 'To get to the other side?'")
        dialogue(charactercut,
                 "It's because there was a KFC on the other side.")
        narrator(f"{charactercut} walks away.")
    if s == 4:
        dialogue(charactercut, "Nice socks.")
        dialogue(user, "Thanks.")
        narrator("You look down at your feet. You aren't wearing any socks.")
    if s == 5:
        narrator(
            f"While walking around the map, you pass by {impostor}. They smile at you menacingly. You think they're a little creepy so you look away."
        )
        updatekarma(-50)
  if roomcut == 'the security room':
    narrator("You walk into the security room for some tasks.")
    if taskmath():
      updatekarma(100)
    else:
      updatekarma(-50)
    narrator("In the meantime, you check up on the cams, but you find nothing of use.")
  if roomcut == 'the engine room':
    narrator(f"\nYou walk by {charactercut} on your way to {roomcut}.")

    dialogue(charactercut, f"Hi {user}.")
    dialogue(user, f"Hey.")
    dialogue(charactercut, f"Where are you going?")
    dialogue(user, f"Just heading to {roomcut} to do some tasks.")
    dialogue(charactercut, f"Oh I see.")
    dialogue(charactercut, f"Can I come with you?")
    narrator(
        f"You think about the impostor that's been going around. If {charactercut} isn't the impostor, it would be understandable them to feel that way.")
    narrator(f"On the other hand, if they aren't a crewmate...")

    useroption = getyesno(f"Do you trust {charactercut}?")

    if useroption == False:
        narrator("You decide it's safer to stay alone.")
        dialogue(
            user,
            "Uhhhhh... I'd rather stay alone. It's probably safer that way.")
        narrator(f"{charactercut} looks a bit sad.")
        dialogue(charactercut,
                 "Don't worry. I understand where you're coming from.")
        updatekarma(-50)

        dotdotdot()
        if getyesno(f"You are now in {roomcut}. Do you do your task?"):
            narrator("You decide to be productive.")
            taskmath()
            updatekarma(50)
            return
        else:
            narrator("Bruh. Ok, fine.")
            updatekarma(-50)
            return

    narrator(f"You decide to keep {charactercut} company.")
    dialogue(charactercut, "Yay! Let's go together then.")

    narrator(f"The two of you walk inside {roomcut}.")

    dialogue(charactercut, "So what kind of task is it?")
    dialogue(user, "It's just some simple calculations.")

    narrator(f"\n{charactercut} watches closely as you do your task.")
    typeprint("...", delay=0.5)
    narrator("you better get this right. It's gonna look real sus if you don't.")

    if taskmath():
        narrator(f"\n{charactercut} smiles. You have completed the task.\n")
        dialogue(
            charactercut,
            "I was a little worried you might've actually been the impostor. I'm glad you're not."
        )
        updatekarma(100)

    else:
        narrator(
            f"\nYou have failed the task."
        )

        dialogue(user, "Oops.")
        narrator(f"{charactercut} is looking a bit nervous being around you now.")
        updatekarma(-100)






def impostorcut():
    charactercut = impostor
    roomcut = random.choice(roomlist) # no longer use this room for cutscene
    roomlist.remove(roomcut)

    if roomcut == "the medbay":
        narrator(f"You walk by {charactercut} in the medbay.")
        userans = getyesno(
            "Would you like to check it out?")
        if userans == False:
            narrator(f"You decide to mind your own buisness.")

        narrator("You decide to collect some intel.")
        time.sleep(2)
        narrator(
            f"{impostor}'s scans are very, very strange. It's almost as if they're... alien..."
        )
        narrator(f"Suddenly, {impostor} turns around. Oh crap, they're going to see you snooping.")
        if doaction("HIDE") == True:
          narrator(f"You hide behind the wall. They didn't notice you.")
          if getyesno(
                  "Would you like to call a emergency meeting to discuss what you saw?: "
          ) == False:
              narrator("You decide to ignore what you saw.")
              karma(-100)
          else:
              narrator("You run to the main lobby to announce a meeting.")
              meetingcut('witness sussy thing')

        else:
            deathending()

    if roomcut == "the electrical":
        narrator(f"You pass by the electrical and see {impostor}.")
        narrator(f"They're messing with the lights!")
        if getyesno(
                "Would you like to call a emergency meeting to discuss what you saw?: "
        ) == False:
            narrator("You decide to ignore what you saw.")
            karma(-100)
        else:
            narrator("You run to the main lobby to announce a meeting.")
            meetingcut('witness sussy thing')

    if roomcut == "the engine room":
        narrator("You pass go to the engine room for some tasks.")
        narrator(f"There, you see {impostor} on top of the vent.")
        dialogue(
            impostor,
            "I'm having a little trouble with this task, can you help me?")
        userans = input(
            "What do you do?\n(A) Nope the frick out.\n(B) Sure, YOLO amirite?\n"
        ).strip(' ').lower()
        while userans not in ('a', 'b'):
            userans = input(
                "Invalid entry. Enter in either option (A) or (B) please: "
            ).strip(' ').lower()

        if userans == "b":
            if getyesno("Are you sure?") == True:
                if getyesno("Cmon, it could be dangerous.") == True:
                    if getyesno("REALLY?") == True:
                        narrator(f"You walk over to help {impostor}.")
                        narrator(f"You turn around to start doing the task.")
                        updatekarma(100)
                        deathending()
                        return
        userans == "a"
        if userans == "a":
            dialogue(user, "I'm a little busy right now, sorry.")
            updatekarma(-100)

    if roomcut == "the security room":
        narrator(
            "You run to the security room for some tasks. On the side, you check the cams."
        )
        narrator("You might've just saw someone venting.")
        narrator(f"There was a flash of {impostor.lower()}.")
        if getyesno(
                "Would you like to call a emergency meeting to discuss what you saw?"
        ) == False:
            narrator("You decide to ignore what you saw.")
            updatekarma(-100)
        else:
            narrator("You run to the main lobby to announce a meeting.")
            meetingcut('witness sussy thing')
          
    if roomcut == "the main lobby":
        kill()
        userans = getyesno(
        f"You see a body on the floor - its {roundkill}. You see {impostor} quickly running out of the crime scene. Do you want to report the body?")
        if userans == True:
          narrator("You make a emergency broadcast.")
          meetingcut("witness sussy thing")
          updatekarma(100)
        else:
          narrator("You turn around, acting like you haven't seen a thing.")
          updatekarma(-500)
  

def emergencymalfunctioncut():
    dotdotdot()

    narrator(
        "The emergency alarms start blaring. The ships nuclear engine is overheating. There is little to no time left, and the ship may end up exploding in a few minutes."
    )

    userans = getyesno("Will you go and help save the ship?")
    if userans == False:
        updatekarma(-1000)
        narrator(
            "Without your help, the spaceship overheats. The explosion sends many millions of debris and dust into the infinite void."
        )
        narrator("The lonely ship drifts away into the endless sky.")
        printending("spacewreak")
        exit(0)
    
    narrator("You reach the engine room.")
    dialogue(
        random.choice(crewmates),
        "THANK GOD YOU'RE HERE. Someone messed with the settings. Help me fix it ASAP, or we'll all die."
    )
    narrator("You'll need to complete three tasks to fix the malfunction.")
    if tasktrivia() and taskmath() and tasktrivia():
        narrator("You have sucessfully saved the ship from destruction.")
        dialogue(random.choice(crewmates),
                 "Dude, you just saved everyone. Thank you.")
        updatekarma(1000)
        dotdotdot()
        narrator("After that, the crewmates do a headcount to see who's present.")
        dialogue(random.choice(crewmates), f"Wait. Where is {impostor}?")
        narrator(f"Everyone silently agress on who to vote in the next meeting.")
        printending("unanimous vote")
        exit(0)
    else:
        updatekarma(-100)
        narrator(
            "You failed to fix the spaceship, and so it overheats. It explodes, and the force sends many millions of debris and dust into the infinite void."
        )
        narrator("The lonely ship drifts away into the endless sky.")
        printending("spacewreak")
        exit(0)


# completed
def meetingcut(reason):
    narrator("A meeting has been called.")
    # 
    dotdotdot()
    narrator("The result of this meeting will depend on your level of trust and hostility you have with the other crewmates.\n\nHit enter to continue", end='', delay=False)
    if reason == "other crewmate finds body":
        kill()
        
        copy = characters
        copy.append(impostor) # impostor left in as it could be a self report
        copy.append(user)
        
        reporter = random.choice(copy) 
        dialogue(reporter, f"I found {roundkill} dead...")
        narrator(f"{reporter} tells you the circumstances surrounding the body. Unfortunately, they have not seen who had killed {roundkill}. Nobody has any clues either...")
        
        copy = characters
        copy.append('Skip')
        
        narrator("Here is the list of people you can vote for: ")
        print(*copy, sep=', ')
        narrator("Reminder that 'skip' exists aswell.")

        # user input
        userans = input("Who do you vote for?: ").lower().strip(' ').capitalize()
        while userans not in copy:
            input("Please enter a proper option: ").lower().strip(' ').capitalize()
        
        
        # ejections
        ejected = ''
        if karmastate() == 'red': # red state; crewmates vote at random
            copy=crewmates
            copy.append(impostor)
            copy.append(user)
            ejected = random.choice(copy)
            ejection(ejected)
        else:  # yellow or green
            if userans != 'Skip':
                if luck(max=5):
                    narrator(f"The majority lands on {userans}.")
                    ejection(userans)
                    ejected=userans
                
                #impos
                if ejected == impostor:
                    printending("lucky")
                    exit(0)
                #user
                elif ejected == user:
                    ejection(ejected)
                    printending('unlucky', True)

            else:
                narrator(f"Majority decides to skip vote.")         
                return

    
    if reason == "witness sussy thing":
        dialogue(random.choice(crewmates), "What happend?")
        narrator(
            f"You explain what you saw. You advise that it might be safest to eject {impostor}."
        )

        narrator("The crewmates discuss.")

        narrator(f"Your karma is currently at {colorkarma()}.")

        if karmastate() == 'yellow':
            narrator(
                f"You have a netural karma. You have a 50% chance of sucess in convincing the crewmates to vote out the impostor.")
            if luck(max=2):

                narrator(
                    f"The crewmates decide to do as you say and vote out {impostor}."
                )

                ejection(impostor)

                dialogue(
                    random.choice(crewmates),
                    "Wow. I was sorta doubting you, but I'm glad to have trusted you."
                )

                dialogue(random.choice(crewmates), f"Thank you, {user}.")

                karma(1000)

                narrator(
                    "Although there may have been some casulaties, the crewmates celebrate their survival, revenge, and victory over the impostor."
                )

                printending("crewmates victory")

            else:

                narrator(
                    f"The crewmates don't trust you enough to vote out {impostor}."
                )

                dialogue(random.choice(crewmates),
                         f"Sorry, {user}. We can't be too safe.")

                dialogue(
                    random.choice(crewmates),
                    f"We don't want to lose anymore people. I don't think we should vote out anyone without concrete evidence."
                )

                narrator("The meeting end has ended.")

                dotdotdot()

                narrator("Well crap.")

                narrator(f"{impostor} has it's eyes on you.")

                narrator(
                    "You try to stick around some other crewmates, but you already know you're the next victim."
                )

                narrator("And right on cue, the lights shut down.")

                narrator("You feel a sharp pain behind you.")

                narrator("Before you know it, you've hit the floor.")
                nocrewmatesremainingcheck()

                dotdotdot()

                hasnotspoken = crewmates

                spoke = random.choice(hasnotspoken)
                hasnotspoken.remove(spoke)
              
                narrator("A emergency meeting has been called.")
                dialogue(spoke, f"What? Who died?")

                spoke = random.choice(hasnotspoken)
                hasnotspoken.remove(spoke)
                
                dialogue(spoke, f"It was {user}...")
                
                narrator(f"Everyone turns to look at {impostor}")
                narrator(f"Since {user} was sussing {impostor}, it would only be natural for them to aim for {user}.")
                narrator(f"Everyone votes to eject impostor.")

                dotdotdot()

                narrator(f"{impostor} has been ejected.")

                narrator(f"{impostor} was the impostor.")

                dotdotdot()

                dialogue(spoke, f"So {user} was really telling the truth...")

                spoke = random.choice(crewmates)
                dialogue(spoke, f"May you rest in piece, {user}.")

                updatekarma(1000)

                printending("'you've won, but at what cost?'")
                exit(0)
        if karmastate() == 'green':
            narrator(
                f"You have a good karma. The crewmates decide to listen to you, and ejects {impostor}."
            )
            ejection(impostor)
            dialogue(random.choice(crewmates),
                     f"Glad we listend to you, {user}.")
            dialogue(random.choice(crewmates), f"Thank you, {user}.")
            updatekarma(1000)
            narrator(
                "Although there may have been some casulaties, the crewmates celebrate their survival, revenge, and victory over the impostor."
            )
            printending("crewmates victory")
            exit(0)
        if karmastate() == 'red':
            narrator(f"You have bad karma.")
            narrator(
                "You have a 5% chance that they will belive you. You have a 95% chance they will eject you instead."
            )
            if luck(max=20) == True:
                ejection(impostor)
                dialogue(
                    random.choice(crewmates),f"I really didn't belive you, but wow."
                )
                dialogue(random.choice(crewmates),
                         f"We're saved. Thank you, {user}."
								)
                updatekarma(1000)
                printending("crewmate victory")
                exit(0)
            else:
                narrator(
                    "Your plan seems to have backfired. The crewmates vote you out instead."
                )
                ejection(user)
                printending("impostor victory", True)
                exit(0)

    if reason == "escaped from impostor":
        narrator("You're safe - for now.\n")
        narrator(f"You look back to a very pissed-off looking {impostor}.\n")
        narrator(
            f"They wouldn't dare kill me - not when there's people coming.\n")
        narrator(
            f"Crewmates start to assemble around the table, feeling the tension between you and {impostor}."
        )

        spoke = random.choice(crewmates)
        copy.remove(spoke)
        dialogue(spoke, "...")

        spoke = random.choice(copy)
        copy.remove(spoke)
        dialogue(spoke, "Care to explain what happend?")

        if doaction("SPEAK"):
            dialogue(user, f"{impostor} is probably the impostor.")
            print(f"{spoke} raises an eyebrow.")
            if doaction("EXPLAIN"):
                dialogue(user, f"They...")
                userans = input(
                    "(A) tried to kill me.\n(B) failed to do medbay scan.\n(C) vented in front of me.\nYour choice: "
                ).strip(' ').lower()
                while userans not in ('a', 'b', 'c'):
                    userans = input("Enter in either 'a', 'b', or 'c': ")
                if userans == 'a':
                    dialogue(user, f"...tried to kill me.")
                if userans == 'b':
                    dialogue(
                        user,
                        f"...failed the medbay scan. And I witnessed it, so they started to chase me."
                    )
                if userans == 'c':
                    dialogue(user, f"...vented in front of me. And I witnessed it, so they started to chase me.")

                if doaction("CONVINCE"):
                  print(f"You say random stuff, and it sounds convincing.")
                  print(
											f"With your quick wit, charisma, and speaking abilities, you managed to convince the crew to vote out {colorprint(impostor, impostor)}",
											end='')
                  if karmastate() == 'red':
                    print(", even with your bad karma.")
                  else:
                    print(".\n")
                  dialogue(random.choice(crewmates),
													 f"Glad we listend to you, {user}.")
                  dialogue(random.choice(crewmates), f"Thank you, {user}.")
                  updatekarma(1000)
                  printending("crewmate victory")
                  exit(0)
                else:
                  print("Your plan seems to have backfired. The crewmates vote you out instead.")
                  ejection(user)
                  printending("impostor victory", True)
                  exit(0)
        else:
            dialogue(impostor, f"{user} just tried to kill me! :(")
            updatekarma(-50)
            print(f"WHAT. What a lying prick.")
            if doaction("defend") == True:
                dialogue(
                    user,
                    f"They're lying- THEY were the one who tried to kill ME.")
                print("The crewmates discuss.")
                print(
                    "The karma you have accumulated will decide your fate...")
                if karmastate() == 'yellow':
                    print(
                        f"You have a netural karma. You have a 50% chance to survive."
                    )
                    if luck(max=2):
                        print(
                            f"The crewmates decide to do as you say and vote out {impostor}."
                        )
                        ejection(impostor)
                        dialogue(
                            random.choice(crewmates),
                            "Wow. I was sorta doubting you, but I'm glad to have trusted you."
                        )
                        dialogue(random.choice(crewmates), f"Thank you, {user}.")
                        karma(1000)
                        print(
                            "Although there may have been some casulaties, the crewmates celebrate their survival, revenge, and victory over the impostor."
                        )
                        printending("crewmates victory")
                    else:
                        narrator(
                            f"The crewmates don't trust you enough to vote out {impostor}"
                        )
                        dialogue(random.choice(crewmates),
                                 f"Sorry, {user}. We can't be too safe. You could be the impostor for all we know...")
                        dialogue(
                            random.choice(crewmates),
                            f"We don't want to lose anymore people. I don't think we should vote out anyone without concrete evidence."
                        )
                        narrator("The meeting ends.")
                        dotdotdot()
                        narrator("Well crap.")
                        narrator(f"{impostor} has it's eyes on you. You know you're screwed.")
                        narrator(
                            "You try to stick around some other crewmates, but you already know you're the next victim."
                        )
                        narrator("And right on cue, the lights shut down.")
                        narrator("You feel a sharp pain behind you.")
                        narrator("Before you know it, you've hit the floor.")
                        dotdotdot()
                        print("A emergency meeting has been called.")
                        spoke = random.choice(copy)
                        copy.remove(spoke)
                        dialogue(spoke, f"What? Who died?")
                        spoke = random.choice(copy)
                        copy.remove(spoke)
                        dialogue(spoke, f"It was {user}...")
                        print(f"Everyone turn to look at {impostor}")
                        dotdotdot()
                        print(f"{impostor} has been ejected.")
                        print(f"{impostor} was the impostor.")
                        dotdotdot()
                        dialogue(spoke,
                                 "So they were really telling the truth...")
                        spoke = random.choice(copy)
                        dialogue(spoke, f"May you rest in piece, {user}.")
                        printending("'you've won, but at what cost?'")
                        exit(0)

                # based on karma
                if karmastate() == 'green':
                    narrator(
                        f"You have a good karma. The crewmates decide to listen to you, and ejects {impostor}."
                    )
                    ejection(impostor)
                    dialogue(random.choice(crewmates),
                             f"Glad we listend to you, {user}.")
                    dialogue(random.choice(crewmates), f"Thank you, {user}.")
                    updatekarma(1000)
                    narrator(
                        "Although there may or may not have been some casulaties, the crewmates celebrate their survival, revenge, and victory over the impostor."
                    )
                    printending("crewmates victory")
                    exit(0)
                if karmastate() == 'red':
                    print(f"You have bad karma.")
                    narrator(
                        f"You have a 5% chance that they will help eject {impostor}. You have a 95% chance of death."
                    )
                    if luck(max=20) == False:
                        ejection(ejected)
                        dialogue(
                            random.choice(crewmates),
                            f"Wow. I really didn't belive you, but I think {impostor} was actually the impostor."
                        )
                        dialogue(random.choice(crewmates),
                                 f"We're saved. Thank you, {user}.")
                        updatekarma(1000)
                        printending("crewmate victory")
                        exit(0)
                    else:
                        narrator(
                            "Your plan seems to have backfired. The crewmates vote you out instead."
                        )
                        ejection(user)
                        printending("impostor victory", True)
                        exit(0)

            else:
              narrator("Your silence wasn't a good look on your part. The crewmates see you as incredibly suspicious.")
              narrator("Because you were unable to defend yourself, the crewmates decided you should be voted out.")
              updatekarma(-250)
              ejection(user)
              
              dotdotdot()

              if len(crewmates) > 1:
                narrator("Another meeting indicated that the impostor was still on board.")
                narrator(f"Now knowing that you were innocent, the remaining crewmates decide that it might be best to eject {impostor}.")
                updatekarma(1000)
                printending("'you've won, but at what cost?'")
                exit(0)
              else:
                narrator("With only the impostor and a crewmate left on the ship, the impostor overpowers the last crewmate on board. In the end, nobody survives")
                printending("impostor victory", True)
                exit(0)

def deathending():
    narrator("Suddenly, you feel like you made a big mistake.")
    narrator(
        f"You turn around to see {impostor} staring at you menacingly."
    )
    dialogue(impostor, "Haha - no hard feelings.")
    narrator(f"{impostor} is holding a sharp knife. A VERY sharp knife. You should probably run away.", delay=False)
    if doaction('RUN'):
        narrator(
            "You make a mad dash all the way to the main lobby, slamming the emergency meeting button."
        )
        meetingcut('escaped from impostor')
    else:
        narrator(
            "You tried to make a run for it, but the impostor - with their inhuman biology - catches up to you."
        )
        narrator(
            "Before you know it, you feel a sharp pain in your back, and now you're fast asleep."
        )
        printending("DEATH BY IMPOSTOR", True)
        exit(0)

def bugending():
    narrator(
        "This ending is supposed to be impossible, but you have somehow got it."
    )
    printending("impossible")
    exit(0)


# sus ending - ejection
# neutral ending - generally average scores and survivals
# impostor ending: the user all the worst options. revealed that you were actually the impostor all along


def bodyencountercut():
  kill()
  narrator("You have called a meeting.")
  narrator("You explain the circumstances of the body.")
  narrator("The crewmates discuss, but do not have any idea on who the impostor is.")
  narrator("Fortunately, calling the meeting has given you a better reputation among the crewmates.")
  updatekarma(150)
  narrator("The meeting has ended.")


narrator('\033[0;31m'+assets.title+'\033[0;37m')
narrator("Welcome to Amongsus - a luck based murder mystery.\n\nFirst, select your avatar color. We have red, black, green, yellow, blue, and cyan.\n")
user = input("Take your pick: ").lower().strip(' ').capitalize()
while user not in crewmates:
    user = input(
        "\nSorry, we don't have that color, or you may have a typo. Please try again: "
    ).strip(' ').lower().capitalize()
crewmates.remove(user)
# narrator(f"You have selected {colorprint(user, user)}.\n")

# narrator(f"NOTE: some of the dialogue do not run automatically, and you must PRESS ENTER on your keyboard to let the dialogue run.", delay=False)

# narrator("You are the captain of a spaceship that embarks on a mission to another planet. ")

# narrator("Soaring through space, you and your crew make breakthroughs in science. ")

# narrator("But recently, the spaceship has been breached by a unknown entity. ")

# narrator("Blending in as a crewmate, the entity is now under disguise. ")

# print("Uncover identity of this "+ colorprint("IMPOSTOR", 'red') + " and save the crew before it's too late", end='')

# dotdotdot()

# narrator("\nHit enter to continue.", delay=False)

# print("_________________________________________\n")
print("GAME START\n")

# impos
impostor = random.choice(crewmates)
crewmates.remove(impostor)
print("IMPOSTOR " + impostor)

print("ඞ Welcome aboard, crewmate!\n")

print("Gather karma to increase your chances of winning. Get more karma by completing tasks, doing morally good things, conducting investigations, or by being friendly with crewmates.")

print("_________________________________________\n\n")

narrator("")

time.sleep(2)

# run a task first
crewmatecut()
dotdotdot()
crewmatecut()
dotdotdot()
meetingcut('other crewmate finds body')
dotdotdot()
impostorcut()
dotdotdot()
impostorcut()