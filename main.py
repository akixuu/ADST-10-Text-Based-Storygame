import random
import time

crewmates = ['Black', 'Red', 'Green', 'Blue', 'Yellow', 'Cyan']
roomlist=['the medbay', 'the electrical', 'the main lobby', 'the navigation room', 'the com room', 'the engine room']
def dialogue(speaker, text):
	print(f"{speaker}: {text}")

def taskreact(action="REACT"):
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
		
def taskmath():
	x = random.randint(1,99)
	y = random.randint(1,99)
	userans = input(f"\nWhat is {x} + {y}?: ").strip()
	
	while not userans.isnumeric():
		userans = input("\nSorry, your answer isn't numeric. Please enter in a integer: ")

	print(f"\nThe correct answer is {x+y}.")
	
	if userans == (x+y):
		return False
	
	return True

def tasktrivia():
	qna = {
		"What game studio created of Among Us?": 'innersloth',
		"Which is the smallest planet within our solar system?": "mercury",
		"Which planet has supersonic winds?": 'neptune',
		"Which planet rotates on its side?": "uranus",
		"Which planet has the most volcanoes?": "venus",
		"Which is the oldest planet in our solar system?": 'jupiter',
		"Which planet has the most moons?": 'saturn'
	}
	question=random.choice(qna)
	
	userans = input(f"{question}: ").strip(' ').lower()
	
	if userans == qna[question]:
		"You're right."
		return True
	else:
		print(f"That is incorrect. The correct answer is {qna[question]}.")
		return False



# user



# user

user = input("Take your pick: ").lower().strip(' ').capitalize()
while user not in crewmates:
    user = input(
        "\nSorry, we don't have that color, or you may have a typo. Please try again: "
    ).strip(' ').lower().capitalize()
crewmates.remove(user)

# character stats setup
trust = 0 # negation of trust is suspicion; trust between you and your crewmates
camraderie = 0 # negation of camraderie is hostility; trust between you and your crewmates
morale = 0 # general vibe of ship
clues = 0

max_achiveable_trust = 0
max_achiveable_camraderie = 0
max_achiveable_morale = 0
max_achivable_clues = 0

# impos
impostor = random.choice(crewmates)
crewmates.remove(impostor)

def trustcut():
	charactercut = random.choice(crewmates)
	roomtcut = random.choice(roomlist)
	
	print(f"\nYou walk by {charactercut} on your way to {roomtcut}.")

	dialogue(charactercut, f"Hi {user}.")
	dialogue(user, f"Hey.")
	dialogue(charactercut, f"Where are you going?")
	dialogue(user, f"Just heading to {roomtcut} to do some tasks.")
	dialogue(charactercut, f"Oh I see.")
	dialogue(charactercut, f"Can I come with you?")
	print(f"You think about the impostor that's been going around. If {charactercut} isn't the impostor, it would be understandable them to feel that way.")
	print(f"On the other hand, if they aren't the crewmate...")
	
	useroption = input(f"Do you trust {charactercut}? (Y/N): ").strip(' ').lower()
	while useroption != 'y' or useroption != 'n':
		input(f"Input a proper answer. (Y/N): ")

	if useroption == 'n':
		dialogue(user, "Uhhhhh... I'd rather stay alone. It's probably safer that way.")
		print(f"{charactercut} looks a bit sad.")
		dialogue(charactercut, "Don't worry. I understand where you're coming from.")
		print(f"camraderie: -100 trust: -50")
		camraderie=-100
		trust=-10
		max_achiveable_camraderie=+100
		max_achiveable_trust=+10
		return

	dialogue(charactercut, "Yay! Let's go together then.")

	print(f"The two of you walk inside {roomtcut}.")

	dialogue(charactercut, "So what kind of task is it?")
	dialogue(user, "It's just some simple calculations.")

	if random.randint(1,10) == 1:
		# death ending
		deathending()
	
	print(f"\n{charactercut} watches closely as you do your task")
	
	if taskmath():
		print(f"\n{charactercut} smiles. You have completed the task.\n")
	
	else:
		print(f"\nYou have failed the task. {charactercut} has become suspicious of you...\n")

		dialogue(user, "Oops.")
		print(f"\n{charactercut} is looking a bit nervous being around you now.\n")
		print(f"\ntrust: -50  suspiciousness: +50  hostility: +50")
		trust=-100
		max_achiveable_trust=+100
		camraderie=-100
		max_achiveable_camraderie+=100

def crewmatechatcut():
	print()

def imposterhintcut():
	# make it room specific?
	print()

def emergencymalfunctioncut():
	print()

def meetingcut():
	print()

def bodyencountercut():
	print()

def randomthoughtscut():
	dialogues=["You wonder about your family back at home. You wonder if they miss you too.", "The stars are pretty tonight. But I guess in space it's always night.", "You miss Earth.", "You feel like someone is watching you.", "You feel a prescence behind your back.", "You might've seen a flash of color in the vents.",]
	print(random.choice(dialogues))

def deathending(charactercut, roomcut):
	print("You feel ")
	
def imposterending():
	print()
# true ending - hero: perfect run with no casulaties
# death ending - impostor kills you
# sus ending - ejection
# spacewreak: ship gets destroyed due to low task completion or emergency malfunction
# neutral ending - generally average scores and survivals
# sabotaged ending: bad scores in general
# impostor ending: the user all the worst options. revealed that you were actually the impostor all along

# gut instints reverse physch, like keeping asking are you sure?