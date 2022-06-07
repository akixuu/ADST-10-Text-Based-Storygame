import random
import time
import sys

crewmates = ['Black', 'Red', 'Green', 'Blue', 'Yellow', 'Cyan']
roomlist=['the medbay', 'the electrical', 'the main lobby', 'the com room', 'the engine room']
karma=0
roundkill=''


def dialogue(speaker, text):
	print(f"{speaker}: {text}\n")

def doaction(action="REACT"):
	start = time.time()
	userans = input(f"Quick! Type {action} within 3 seconds: ")
	end = time.time()
	
	if (end - start) > 3:
		print("You took too long...")
		return False
	
	if userans.strip(' ').lower() == action.lower():
		print(f"You were able to sucessfully {action}.")
		return True
	
	else:
		print(f"You have failed to {action}.")
		return False

def luck(test=False, max='6'):
	userans = input(f"Input a number from 1 to {max}.").strip()
	x = random.randint(1,max)
	while not userans.isnumeric() and max >= int(userans) >= 1:
		userans = input(f"\nSorry, your answer isn't numeric, or isn't within the bounds (1-{max}). Try again:  ").strip()

	# always return true for testing purposes
	if test == True:
		return True
	
	print("...")
	if userans == x:
		return True
	else:
		return False

def taskmath():
	x = random.randint(1,99)
	y = random.randint(1,99)
	userans = input(f"\nWhat is {x} + {y}?: ").strip()
	
	while not userans.isnumeric():
		userans = input("\nSorry, your answer isn't numeric. Please enter in a integer: ").strip()

	correctans=x+y
	
	if int(userans) == correctans:
		print("You're right.")
		return True
	else:
		print(f"Incorrect. The correct answer is {correctans}.")
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
	question=random.choice(list(qna))
	userans = input(f"{question}: ").strip(' ').lower()
	
	if userans == qna[question]:
		print("You're right.")
		return True
	else:
		print(f"That is incorrect. The correct answer is {qna[question]}.")
		return False

# user

def kill():
	copy = crewmates
	copy.remove(impostor)
	global roundkill
	roundkill=crewmates.remove(random.choice(copy))
	 
def getyesno(prompt):
	useroption = input(prompt+" (Y/N): ").lower().strip(" ")
	while useroption not in ("n", "y"):
		useroption = input(f"Input a proper answer. (Y/N): ").strip(' ').lower()
	if useroption == "y":
		return True
	else:
		return False

def karmastate():
	if 150 > karma > -150:
		return 'yellow'
	if karma >= 150:
		return 'green'
	if karma <= -150:
		return 'red'
def colorkarma():
	state = karmastate()
	if state == 'green':
		return '\033[0;32m'+ str(karma) + '\033[0;37m'
	if state == 'yellow':
		return "\033[0;33m" + str(karma) + '\033[0;37m'
	if state == 'red':
		return "\033[0;31m" + str(karma) + '\033[0;37m'
def updatekarma(change=0):
	symbol=''
	global karma
	karma+=change
	if change>0:
		symbol=='+'
	print(f"Karma: {symbol}{change}")
	print(f"You have {colorkarma()} karma.")
def printending(ending, userdeath=False):
	print(f"You have achived the {ending.upper()} ending.")
	print(f"You had {colorkarma()} karma.")
	crewmates.remove(impostor)
	if userdeath == True:
		crewmates.clear()
	if len(crewmates)==4:
		print("All crewmates survived.")
		return
	if len(crewmates)<=1:
		print("One crewmate remain on the ship.")
		return
	print(f"{len(crewmates)} crewmates survived.")
	return

user = input("Take your pick: ").lower().strip(' ').capitalize()
while user not in crewmates:
    user = input(
        "\nSorry, we don't have that color, or you may have a typo. Please try again: "
    ).strip(' ').lower().capitalize()
crewmates.remove(user)

# impos
impostor = random.choice(crewmates)

def trustcut():
	charactercut = random.choice(crewmates)
	roomcut = random.choice(roomlist)
	
	print(f"\nYou walk by {charactercut} on your way to {roomcut}.")

	dialogue(charactercut, f"Hi {user}.")
	dialogue(user, f"Hey.")
	dialogue(charactercut, f"Where are you going?")
	dialogue(user, f"Just heading to {roomcut} to do some tasks.")
	dialogue(charactercut, f"Oh I see.")
	dialogue(charactercut, f"Can I come with you?")
	print(f"You think about the impostor that's been going around. If {charactercut} isn't the impostor, it would be understandable them to feel that way.")
	print(f"On the other hand, if they aren't the crewmate...")
	
	useroption=getyesno(f"Do you trust {charactercut}? (Y/N): ")

	if useroption == False:
		print("You decide it's safer to stay alone.")
		dialogue(user, "Uhhhhh... I'd rather stay alone. It's probably safer that way.")
		print(f"{charactercut} looks a bit sad.")
		dialogue(charactercut, "Don't worry. I understand where you're coming from.")
		updatekarma(100)

		print("...")
		if getyesno(f"You are now in {roomcut}. Do you do your task? (Y/N): "):
			print("You decide to be productive.")
			taskmath()
			print("ship stability: +10")
			return
		else:
			print("Bruh. Ok, fine.")
			return
		

	print(f"You decide to keep {charactercut} company.")
	dialogue(charactercut, "Yay! Let's go together then.")

	print(f"The two of you walk inside {roomcut}.")

	dialogue(charactercut, "So what kind of task is it?")
	dialogue(user, "It's just some simple calculations.")

	if luck() and charactercut == impostor:
		# death ending
		deathending(impostor, roomcut)
	
	print(f"\n{charactercut} watches closely as you do your task")
	
	if taskmath():
		print(f"\n{charactercut} smiles. You have completed the task.\n")
		dialogue(charactercut, "I was a little worried you might've actually been the impostor. I'm glad you're not.")
		updatekarma(100)
	
	else:
		print(f"\nYou have failed the task. {charactercut} has become suspicious of you...\n")

		dialogue(user, "Oops.")
		print(f"{charactercut} is looking a bit nervous being around you now.")
		updatekarma(-100)


def crewmatechatcut():
	charactercut = random.choice(crewmates)
	roomcut = random.choice(roomlist)

	print(f"While walking towards {roomcut}, you pass by {charactercut}.")
	
	s = input("Enter in a value between 1 and 4.")
	while s.isnumeric() == False and 1 <= s <= 5:
		s = input("Please enter in a numeric value between 1 and 5.")

	if s == 1:
		dialogue(charactercut, f"Hey, {user}!")
		dialogue(user, "Hi.")
		dialogue(charactercut, f"Enjoying the weather?")
		dialogue(user, "We're in space.")
	if s == 2:
		print("You exchange greetings, and head opposite ways.")
	if s == 3:
		dialogue(charactercut, "Why did the kitchen cross the road?")
		dialogue(user, "Is it 'To get to the other side?'")
		dialogue(charactercut, "It's because there was a KFC on the other side.")
		print(f"{charactercut} walks away.")
	if s == 4:
		dialogue(charactercut, "Nice socks.")
		dialogue(user, "Thanks.")
		print("You look down at your feet. You aren't wearing any socks.")
	if s == 5:
		print(f"While walking around the map, you pass by {impostor}. They smile at you menacingly. You think they're a little creepy so you look away.")
		updatekarma(-50)
		
def impostorhintcut():
	# charactercut = random.choice(crewmates)
	roomcut = random.choice(roomlist)

	if roomcut == "the medbay":
		print(f"You walk by {impostor} in the medbay.")
		userans = getyesno("They're doing a body scan. Would you like to check it out?")
		if userans == False:
			print(f"You decide to mind your own buisness.")

		print("You decide to collect some intel.")
		print("...")
		print(f"{impostor}'s scans are very, very strange.")
		print(f"Oh crap, they're going to see you snooping.")
		if doaction("HIDE") == True:
			print(f"You hide behind the wall. They didn't notice you.")
			if getyesno("Would you like to call a emergency meeting to discuss what you saw?: ") == False:
				print("You decide to ignore what you saw.")
			else:
				print("You run to the main lobby to announce a meeting.")
				meetingcut('witness sussy thing')
		else:
			deathending(impostor, roomcut)
			
	if roomcut == "the electrical":
		print(f"You pass by the electrical and see {impostor}.")
		print(f"They seem to be messing with the lights...")
		if getyesno("Would you like to call a emergency meeting to discuss what you saw?: ") == False:
				print("You decide to ignore what you saw.")
		else:
				print("You run to the main lobby to announce a meeting.")
				meetingcut('witness sussy thing')
	
	if roomcut == "the engine room":
		print("You pass go to the engine room for some tasks.")
		print(f"There, you see {impostor} on top of the vent.")
		dialogue(impostor, "I'm having a little trouble with this task, can you help me?")
		userans = input("What do you do?\n(A) Nope the frick out.\n(B) Sure, YOLO amirite?\n").strip(' ').lower()
		while userans not in ('a','b'):
			userans = input("Invalid entry. Enter in either option (A) or (B) please: ").strip(' ').lower()

		if userans == "b":
			if getyesno("Are you sure?") == True:
				if getyesno("Cmon, it could be dangerous.") == True:
					if getyesno("REALLY?") == True:
						print(f"You walk over to help {impostor}.")
						print(f"You turn around to start doing the task.")
						updatekarma(100)
						deathending(impostor, roomcut)
						return
		userans=="a"
		if userans == "a":
			dialogue(user, "I'm a little busy right now, sorry.")
			updatekarma(-100)
		
	if roomcut == "the com room":
		print("You run to the com room for some tasks. On the side, you check the cams.")
		print("...")
		print("You might've just saw someone venting.")
		print(f"There was a flash of {impostor.lower()}.")
		if getyesno("Would you like to call a emergency meeting to discuss what you saw?") == False:
				print("You decide to ignore what you saw.")
				updatekarma(-100)
		else:
				print("You run to the main lobby to announce a meeting.")
				meetingcut('witness sussy thing')
	
	if roomcut == "the main lobby":
		print("While walking around the map, you see two crewmates in the main lobby.")
		kill()
		print(f"It's {impostor} and {roundkill}.")
		print(f"{impostor} drives a knife deep into the back of {roundkill}'s head. You think you can see bone.")
		if getyesno("Would you like to call a emergency meeting to discuss what you saw?") == False:
				print("You decide to ignore what you saw.")
				updatekarma(-300)
		else:
				print("You make a emergency broadcast.")
				print("...")
				meetingcut('witness sussy thing')
		

def emergencymalfunctioncut():
	print("...")

	print("The emergency alarms start blaring. The ships nuclear engine is overheating. There is little to no time left, and the ship may end up exploding in a few minutes.")

	userans = getyesno("Will you go and help save the ship? (Y/N): ")
	if userans == False:
		updatekarma(-1000)
		print("Without your help, the spaceship overheats. The explosion sends many millions of debris and dust into the infinite void.")
		print("The lonely ship drifts away into the endless sky.")
		printending("spacewreak")
		sys.exit(0)
	copycrewmates=crewmates
	copycrewmates.remove(impostor)
	print("You reach the engine room.")
	dialogue(random.choice(crewmates), "THANK GOD YOU'RE HERE. Someone messed with the settings. Help me fix it ASAP, or we'll all die.")
	print("You'll need to complete three tasks to fix the malfunction.")
	if tasktrivia() and taskmath() and tasktrivia():
		print("You have sucessfully saved the ship from destruction.")
		dialogue(random.choice(crewmates), "Dude, you just saved everyone. Thank you.")
		updatekarma(1000)
		print("...")
		print("After that, the crewmates do a headcount to see who's present.")
		dialogue(random.choice(crewmates), f"Wait. Where is {impostor}?")
		print(f"Everyone silently agress on who to vote in the next meeting.")
		printending("unanimous vote")
		sys.exit(0)
	else:
		updatekarma(-100)
		print("You failed to fix the spaceship, and so it overheats. It explodes, and the force sends many millions of debris and dust into the infinite void.")
		print("The lonely ship drifts away into the endless sky.")
		printending("spacewreak")
		sys.exit(0)
		
	

 # completed
def meetingcut(reason='none'):
	# the result of this meeting will depend on your level of trust and hostility you have with the other crewmates
	if reason == "witness sussy thing":
		print("...")
		dialogue(random.choice(crewmates), "Whats this meeting for? I was in the middle of a task.")
		dialogue(random.choice(crewmates), "What happend?")
		print("You explain what you saw.")

		print("The crewmates discuss.")

		print(f"Your karma is currently at {colorkarma()}.")

		if karmastate == 'yellow':
			print(f"You have a netural karma.")
			print(f"You have a 50% chance to survive.")
			luck(max=2)
		if karmastate == 'green':
			print(f"You have a good karma. The crewmates decide to listen to you, and ejects {impostor}.")
		if karmastate == 'red':
			print(f"You have bad karma.")
			print("You have a 1% chance that they will belive you.")
			if luck(max=100) == False:
				print(f"{impostor} has been ejected.")
				crewmates.remove(impostor)
				dialogue(random.choice(crewmates), f"Wow. I really didn't belive you, but I think {impostor} was actually the impostor.")
				dialogue(random.choice(crewmates), f"We're saved. Thank you, {user}.")
				printending("crewmate victory")
			else:
				print("Your plan seems to have backfired.")
				print(f"{user} has been ejected.")
				print("...")
				print("Nobody ends up figuring out who the impostor is, and all the crewmates on board dies. Without maintenence, the spaceship collapses.")
				printending("impostor victory", True)
			

	if reason == "escaped from impostor":
		print("...")
		print("You're safe. For now.")
		print(f"You look back to a very pissed-off looking {impostor}.")
		dialogue()


	if reason == "body encountered":
		print()

	# check if endgame

	# if user is voted out (ending: ejected), all crewmates are going to die
	# impostor kick is called crewmates victory
	# this means only impos remains
	if crewmates.len() == 1 and crewmates[0] == impostor:
		dialogue(impostor, "HAHA")
		dialogue(impostor, "HAHAHAHAHAHAHA")
		print("Oh no.")
		dialogue(impostor, "I'm a little surprised that nobody voted me out.")
		dialogue(impostor, "I bet if you had done things a bit differently, I would've been voted out.")
		dialogue(impostor, "But, well, good news for me I guess!")
		print(f"{impostor} aproaches you. You can do nothing but close your eyes and await your doom.")
		printending("impostor")
def bodyencountercut():
	charactercut = random.choice(crewmates)
	roomcut = random.choice(roomlist)

	userans = getyesno("You see a body on the floor. Do you want to report the body?")
	if userans == True:
		print("You make a emergency broadcast.")
		meetingcut("body encountered")
		updatekarma(150)
	else:
		print("You turn around, acting like you haven't seen a thing.")
		updatekarma(-150)
		print("...")
		# second impostor ending

def randomthoughtscut():
	dialogues=["You wonder about your family back at home. You wonder if they miss you too.", "The stars are pretty tonight. But I guess in space it's always night.", "You miss Earth.", "You feel like someone is watching you.", "You feel a prescence behind your back.", "You hear tapping in the vents. Must be a rat or... You to not think about it.", "It's a cool night. You silently curse the person who turned the AC on.", "You think about today's lunch.", "You can hear some crewmates chatting from a distance."]
	print(random.choice(dialogues))


def deathending(charactercut, roomcut):
	print("Suddenly, you feel like you made a big mistake.")
	print(f"You turn around to see {charactercut} staring at you. They start to drool.")
	dialogue(charactercut, "Haha - it sucks that you have to see me like this.")
	if doaction('RUN'):
		print("You make a mad dash all the way to the main lobby, slamming the emergency meeting button.")
		meetingcut('escaped from impostor')
	else:
		print("You tried to run, but the impostor catches up to you.")
		print("Before you know it, you're fast asleep.")
		printending("DEATH BY IMPOSTOR")
		sys.exit(0)

def badkarma():
	# trigger: crewmates list only has one val
		print()

def bugending(): 
	print("This ending is supposed to be impossible, but you have somehow got it.")
	printending("impossible")
	sys.exit(0) 

# sus ending - ejection
# neutral ending - generally average scores and survivals
# impostor ending: the user all the worst options. revealed that you were actually the impostor all along

impostorhintcut()