import random
import time
import sys

crewmates = ["Black", 'Red', 'Green', 'Blue', 'Yellow', 'Cyan']
roomlist=['the medbay', 'the electrical', 'the main lobby', 'the com room', 'the engine room']
cutusedrooms=[]
karma=0
roundkill=''

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
def doaction(action="REACT"):
	start = time.time()
	userans = input(f"Quick! Type {action.upper()} within 3 seconds: ")
	end = time.time()
	
	if (end - start) > 3:
		print("You took too long...")
		return False
	
	if userans.strip(' ').lower() == action.lower():
		print(f"You were able to sucessfully {action.upper()}.")
		return True
	
	else:
		print(f"You have failed to {action.upper()}.")
		return False

def luck(test=False, max='6'):
	userans = input(f"Input a number from 1 to {max}: ").strip()
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
	# check if endgame
	# this means only impos remains
	if len(crewmates)==1:
		print("The imposter has killed the other last crewmate on board. Only you and the impostor remain.")
		print("There is nothing for you to do now but await your doom.")
		printending("impostor victory")
		exit(0)
	
	# if len(crewmates)==1:
	# 	dialogue(impostor, "HAHA")
	# 	dialogue(impostor, "HAHAHAHAHAHAHA")
	# 	print("Oh no.")
	# 	dialogue(impostor, "I'm a little surprised that nobody voted me out.")
	# 	dialogue(impostor, "I bet if you had done things a bit differently, I would've been voted out.")
	# 	dialogue(impostor, "But, well, good news for me I guess!")
	# 	print(f"{impostor} aproaches you. You can do nothing but close your eyes and await your doom.")
	# 	printending("impostor victory")
	 
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
	color='\033[0;31m'
	global karma
	karma+=change
	if change>0:
		symbol=='+'
		color='\033[0;32m'
	print("_________________________________\n")
	print(f"Karma: {color}{symbol}{change}\033[0;37m")
	print(f"You have {colorkarma()} karma.")
	print("_________________________________\n")
def printending(ending, userdeath=False):
	print(f"You have achived the {ending.upper()} ending.")
	print(f"You had {colorkarma()} karma.")
	crewmates.remove(impostor)
	if userdeath == True:
		crewmates.clear()
		print("Nobody survives.")
	if len(crewmates)==4:
		print("All crewmates survived.")
		return
	if len(crewmates)==1:
		print("One lonely crewmate remains on the ship.")
		return
	print(f"{len(crewmates)} crewmates survived.")
	return

user = input("Take your pick: ").lower().strip(' ').capitalize()
while user not in crewmates:
		user = input(
        "\nSorry, we don't have that color, or you may have a typo. Please try again: "
    ).strip(' ').lower().capitalize()
crewmates.remove(user)
print(f"You have selected {colorprint(user, user)}.")


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
			updatekarma(50)
			return
		else:
			print("Bruh. Ok, fine.")
			updatekarma(-50)
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
		
def impostorhintcut(): # not impos, impos, walk in on murder, no event -> crewmate finds body
	charactercut = random.choice(crewmates)
	if charactercut == impostor(): isimpos=True
	roomcut = random.choice(roomlist)

	if roomcut == "the medbay":
		print(f"You walk by {charactercut} in the medbay.")
		userans = getyesno("They're doing a body scan. Would you like to check it out?")
		if userans == False:
			print(f"You decide to mind your own buisness.")

		print("You decide to collect some intel.")
		if isimpos:
			print(f"{impostor}'s scans are very, very strange. It's almost as if they're... alien...")
			print(f"Oh crap, they're going to see you snooping.")
			if doaction("HIDE") == True:
				print(f"You hide behind the wall. They didn't notice you.")
				if getyesno("Would you like to call a emergency meeting to discuss what you saw?: ") == False:
					print("You decide to ignore what you saw.")
					karma(-100)
				else:
					print("You run to the main lobby to announce a meeting.")
					meetingcut('witness sussy thing')
		
			else:
				deathending(impostor, roomcut)
		else:
			print(f"It looks like charactercut isn't the impostor.")
			karma(+50)
	if roomcut == "the electrical":
		print(f"You pass by the electrical and see {impostor}.")
		print(f"They're messing with the lights!")
		if getyesno("Would you like to call a emergency meeting to discuss what you saw?: ") == False:
			print("You decide to ignore what you saw.")
			karma(-50)
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
				print("...")
				randomthoughtscut()
				print("")
		else:
				print("You make a emergency broadcast.")
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
def meetingcut(reason):
	# the result of this meeting will depend on your level of trust and hostility you have with the other crewmates
	print("...")

	if reason == "other crewmate finds body":
		print("You hear a emergency meeting announcement.")
		kill()
		reporter=random.choice(crewmates) # impostor left in as it could be a self report
		dialogue(reporter, f"I found {roundkill} dead...")
		dialogue(user, f"...")
		dialogue(user, f"Tell me the details.")
		print(f"{reporter} tells you everything. Unfortunately, they have not seen who had killed {roundkill}.")
		copy = crewmates
		copy.append(user)
		copy.append('skip')
		print("Here are the list of people you can vote for: ")
		print(*copy, sep=', ')
		print("Note that 'skip' exists aswell.")
		
		userans=input("Who do you vote for?:").lowercase().strip(' ').capitalize()
		while userans not in copy:
			input("Please enter a proper option: ").lowercase().strip(' ').capitalize()

		ejected=''
		if karmastate() == 'red':
			ejected = random.choice(copy)
			print(f"The majority lands on {ejected}.")
		else: # yellow or green
			if userans!='skip':
				if luck(max=5):
					ejected = userans
					print(f"The majority lands on {ejected}.")
			else:
				print(f"Majority decides to skip vote.")
				return
		
		if ejected == impostor:
				print(f"{impostor} has been ejected.")
				print(f"{impostor} was the impostor. How lucky!")
				printending("lucky")
				exit(0)
			
		if ejected == user:
			print(f"You have been ejected. Very unlucky of you.")
			printending('ejected', True)
			exit(0)

		print(f"{ejected} has been ejected.")
		print(f"{ejected} was not the impostor.")
		crewmates.remove(ejected)
		if len(crewmates) == 1:
			print("...")
			print("You are now the last crewmate on board. Only you and the imposter remain.")
			print("There is nothing for you to do now but await your doom.")
			printending("impostor victory")
			exit(0)
		print("...")	
		
	if reason == "witness sussy thing":
		dialogue(random.choice(crewmates), "What happend?")
		print(f"You explain what you saw. You advise that it might be safest to eject {impostor}")

		print("The crewmates discuss.")

		print(f"Your karma is currently at {colorkarma()}.")

		if karmastate() == 'yellow':
			print(f"You have a netural karma. You have a 50% chance to survive.")
			if luck(max=2):
				print(f"The crewmates decide to do as you say and vote out {impostor}.")
				print("The impostor has been ejected.")
				copy = crewmates
				copy.remove(impostor)
				dialogue(random.choice(copy), "Wow. I was sorta doubting you, but I'm glad to have trusted you.")
				dialogue(random.choice(copy), f"Thank you, {user}.")
				karma(1000)
				print("Although there may have been some casulaties, the crewmates celebrate their survival, revenge, and victory over the impostor.")
				printending("crewmates victory")
			else:
				print(f"The crewmates don't trust you enough to vote out {impostor}")
				copy=crewmates
				copy.remove(impostor)
				dialogue(random.choice(copy), f"Sorry, {user}. We can't be too safe.")
				dialogue(random.choice(copy), f"We don't want to lose anymore people. I don't think we should vote out anyone without concrete evidence.")
				print("The meeting ends.")
				print("...")
				print("Well crap.")
				print(f"{impostor} has it's eyes on you.")
				print("You try to stick around some other crewmates, but you already know you're the next victim.")
				print("And right on cue, the lights shut down.")
				print("You feel a sharp pain behind you.")
				print("Before you know it, you've hit the floor.")
				print("...")
				print("A emergency meeting has been called.")
				spoke=random.choice(copy)
				copy.remove(spoke)
				dialogue(spoke, f"What? Who died?")
				spoke=random.choice(copy)
				copy.remove(spoke)
				dialogue(spoke, f"It was {user}...")
				print(f"Everyone turn to look at {impostor}")
				print("...")
				print(f"{impostor} has been ejected.")
				print(f"{impostor} was the impostor.")
				print("...")
				dialogue(spoke, "So they were really telling the truth...")
				spoke=random.choice(copy)
				copy.remove(spoke)
				dialogue(spoke, f"May you rest in piece, {user}.")
				printending("'you've won, but at what cost?'")
				exit(0)
		if karmastate() == 'green':
			print(f"You have a good karma. The crewmates decide to listen to you, and ejects {impostor}.")
			dialogue(random.choice(crewmates), f"Glad we listend to you, {user}.")
			dialogue(random.choice(crewmates), f"Thank you, {user}.")
			karma(1000)
			print("Although there may have been some casulaties, the crewmates celebrate their survival, revenge, and victory over the impostor.")
			printending("crewmates victory")
			exit(0)
		if karmastate() == 'red':
			print(f"You have bad karma.")
			print("You have a 5% chance that they will belive you.")
			if luck(max=20) == False:
				print(f"{impostor} has been ejected.")
				crewmates.remove(impostor)
				dialogue(random.choice(crewmates), f"Wow. I really didn't belive you, but I think {impostor} was actually the impostor.")
				dialogue(random.choice(crewmates), f"We're saved. Thank you, {user}.")
				karma(1000)
				printending("crewmate victory")
				exit(0)
			else:
				print("Your plan seems to have backfired. The crewmates vote you out instead.")
				print(f"{user} has been ejected.")
				print("...")
				print("Nobody ends up figuring out who the impostor is, and all the crewmates on board dies. Without maintenence, the spaceship collapses.")
				printending("impostor victory", True)
				exit(0)
			

	if reason == "escaped from impostor":
		print("You're safe - for now.")
		print(f"You look back to a very pissed-off looking {impostor}.")

		print(f"They wouldn't dare kill me - not when there's people coming.")
		print(f"Crewmates start to assemble around the table, feeling the tension between you and {impostor}. You're still breathing a bit heavy.")
		print("You look a little crazed, which the other crewmates are a bit afraid of.")
		updatekarma(-50)
		copy = crewmates
		copy.remove(impostor)
		spoke=random.choice(copy)
		copy.remove(spoke)
		dialogue(spoke, "...")
		
		spoke=random.choice(copy)
		copy.remove(spoke)
		dialogue(spoke, "Care to explain what happend?")

		if doaction("SPEAK"):
			dialogue(user, f"{impostor} is probably the impostor.")
			print(f"{spoke} raises an eyebrow.")
			if doaction("EXPLAIN"):
				dialogue(user, f"They...")
				userans=input("(A) tried to kill me.\n(B) have strange biology. I saw their medbay scan.\n(C) vented in front of me.\nYour choice: ").strip(' ').lower()
				while userans not in ('a','b','c'):
					userans=input("Enter in either 'a', 'b', or 'c': ")
				if userans=='a':
					dialogue(user, f"...tried to kill me.")
				if userans=='b':
					dialogue(user, f"...have strange biology. I saw their medbay scan.")
				if userans=='c':
					dialogue(user, f"...vented in front of me.")
				if doaction("CONVINCE"):
					print(f"You say random stuff, but it sounds convincing.")
					# TODO print()
		else:
			print()

	if reason == "body encountered":
		print("body encountered")

	
def bodyencountercut():
	charactercut = random.choice(crewmates)
	roomcut = random.choice(roomlist)

	userans = getyesno("You see a body on the floor. Do you want to report the body?")
	if userans == True:
		print("You make a emergency broadcast.")
		meetingcut("body encountered")
		updatekarma(100)
	else:
		print("You turn around, acting like you haven't seen a thing.")
		updatekarma(-500)

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

meetingcut('escaped from impostor')