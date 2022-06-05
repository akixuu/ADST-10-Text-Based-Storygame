from time import sleep
import sys
import random
import assets
import color

# haha i legit just lost 400 lines of code im going to cry
# bad implementation


user = {'color': '', 'tasks completed': 0, "wrong ejections":0, "location":'Main Lobby', 'vote points':0, "body encountered": True}
impostor = {'color': '', 'kill count': 0,}

class characters:
    crewmates = ['black', 'red', 'green', 'blue', 'yellow', 'cyan']
    deceased = []


class Room:
    def __init__(self, name, tasks, has_body):
        self.name = name
        self.tasks = tasks
        self.has_body = has_body


rooms = {
    "Medical": Room("Medical", 0, False),
    "Electrical and Engine": Room("Electrical and Engine", 0, False),
    "Sleep Chambers": Room("Sleep Chambers", 0, False),
    "Main Lobby": Room("Main Lobby", 0, False),
    "Navigation": Room("Navigation", 0, False),
}

def create_kill:
	# set body somewhere the user isn't
	roomlist=['Medical', 'Electrical and Engine', 'Sleep Chambers', 'Main Lobby', 'Navigation']
	roomlist.remove(user["location"])
	roomlist.get(random.choice(rooms)).has_body=True
	
	# pick who dies
	killed=random.choice(characters.crewmates)
	characters.crewmates.remove(killed)
	characters.deceased.append(killed)
	impostor["kill count"]+=1

def command(txt=''):
	valid_commands=['nav','location', 'vote', 'dotask', 'tasklist', 'rooms', 'help']
	
	if txt is '':
		txt=input("Enter a command: ")
		while txt not in valid_commands:
			print("\nSorry, that wasn't a valid command. Try checking your spelling, or type 'help' for a list of commands. Note that the input is case-sensitive.")
			txt=input("Enter a command: ")

	if txt == 'nav':
		roomlist=['Medical', 'Electrical and Engine', 'Sleep Chambers', 'Main Lobby', 'Navigation']
		selection=input('Where to?')
		while selection is not in roomlist:
			print("That isn't a valid room.")
			input("Try again: ")

		if rooms.get(selection).has_body:
			cutscenes.body

	if txt == 'location':
		print("Currently, you are in the " + user["location"] + ". You have " + rooms.get(user.get("location")).tasks  +
      " task(s) left in this room.")

	if txt == 'vote':
		if user["vote point"]>= 4:
			user["vote point"]-=4
		else if user["body encountered"]:
			user["body encountered"]=False
		else:
			print("You don't have sufficient voting points.")

		votecast=input('Who will you vote out?')
		while votecast not in characters.crewmates or votecast is not impostor['color']:
			print("Invalid entry, you may have a typo, or you may have voted someone who can not be voted out. (i.e. deceased crewmates).")
			input('Try again: ')

		characters.deceased.append(votecast)
		characters.crewmates.remove(votecast)
		if votecast not impostor['color']:
			print(assets.was_not_impos)
			user["wrong ejections"]+=1
		
		
		print('')

	if txt == 'dotask':
		dotdotdot()
		print('\n\nTask Complete')
		user["vote points"]+=1
		print("You have completed "+ user["tasks completed"])

	if txt == 'tasklist':
		print('')

	if txt == 'help':
		print('')

	if txt == 'rooms':
		print('List of rooms: ')
		print(r"""
					- Medical
					- Electrical and Engine
					- Sleep Chambers
					- Main Lobby
					- Navigation

					Note that the command input is case sensitive.
					""")

class cutscenes:
		def body():
			print('You have discovered a body. You must take action and vote who you think the imposter is.')
			command('vote')
	
    def happy():
        cut = random.randint(0, 1)

        if cut == 0:
            print("")

        if cut == 1:
            print("")

        if cut == 2:
            print("")

    def sad():
        cut = random.randint(0, 1)

        if cut == 0:
            print("")

        if cut == 1:
            print("")

        if cut == 2:
            print("")

    def imposter_revealing():
        cut = random.randint(0, 1)

        if cut == 0:
            print("")

        if cut == 1:
            print("")

        if cut == 2:
            print("")

    def joke():
        print("")


{
    # black = "\033[0;30;41m"
    # red = "\033[0;31m"
    # green = "\033[0;32m"
    # yellow = "\033[0;33m"
    # blue = "\033[0;34;47m"
    # cyan = "\033[0;36m"
    # white = "\033[0;37m"
    # purple = "\033[0;35m"
    # bright_black = "\033[1;90m"
    # bright_red = "\033[0;91m"
    # bright_green = "\033[0;92m"
    # bright_yellow = "\033[3;93;44m"
    # bright_blue = "\033[0;94m"
    # bright_purple = "\033[0;95m"
    # bright_cyan = "\033[0;96m"
    # bright_white = "\033[0;97m"
}

# text effects

def bolden(txt):
    return bold + txt + normal


def dotdotdot(delay=0.5):
    for x in range(3):
        type('.', delay)
    print("\n")


def type(text, delay=0.05):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(delay)


def color_print(colorcode, text, typed=False, delay=0.05):
    if typed:
        type(colorcode + text + white, delay)
    else:
        print(colorcode + text + white, end='')



## START ##
			
print(red + assets.title + white + '\n')
print(
    "Welcome to " + red + "AmongSus 2.0" + white +
    " - a luck based murder mystery.\n\nFirst, select your avatar color. We have red, black, green, yellow, blue, cyan. ",
    end='')

user["color"] = input("Take your pick: ")

while user["color"] not in characters.crewmates:
    user["color"] = input(
        "\nSorry, we don't have that color, or you may have a typo. Please try again: "
    )

print('\n')
dotdotdot()

# remove user color from main npc list
characters.crewmates.remove(user["color"])

# now select random impostor and remove them from npc list
impostor["color"] = random.choice(characters.crewmates)
characters.crewmates.remove(impostor["color"])

# print("\nYou have chosen ", end='')
# color_print(eval(user["color"]), user["color"])
# print('.\n\n', end='')
# color_print(eval(user["color"]), assets.smallsus)
# print("\n")

# dotdotdot()

### INTRODUCTION
# bolden("INTRODUCTION")

# uncomment later
# type("\You are the captain of a spaceship that embarks on a mission to another planet. "+bolden("")+" Soaring through space, you and your crew make breakthroughs in science. " +
#      bolden("") +
#      "But recently, the spaceship has been breached by a unknown entity. " +
#      bolden("") +
#      "Blending in as a crewmate, the entity is now under disguise. " +
#      bolden("") + "Uncover identity of this " + bolden('IMPOSTOR') +
#      ", and save the crew before it's too late")

# #dotdotdot()

# print('\n\n')

# dotdotdot()

print(
    "They're 8 tasks for you to complete. Navigate to different rooms to complete tasks. You may attempt to eliminate the impostor by voting them off after every 4 tasks completed, or if you are in the same room as a body."
)

print("Here are a list of commands you can use in game:\n")
print("\t" + bolden("help") + ": shows the list of available commands")
print("\t" + bolden("nav") + ": navigate to a specific room")
print("\t" + bolden("rooms") + ": prints the list of rooms")
print(
    "\t" + bolden("vote") +
    ": allows you to kick a crewmate off ship. note that this tasks requires you to be in the same room as a body, or you must have complete four tasks for each vote"
)
print("\t" + bolden("tasklist") +
      ": gives info on how many tasks you have left and in which room")
print("\t" + bolden("dotask") +
      ": gives info on how many tasks you have left and in which room")

print("\nAnother note that this is a ", end='')
color_print(yellow, "luck based")
print(" game.\n\n")

#### GAME START

dotdotdot()
color_print(eval(user["color"]), assets.tinysus)
type("  Welcome aboard, " + bolden('crewmate') + "!\n\n")
dotdotdot()

print("The stars are really pretty tonight.")

def command():
	input("Enter a command: ")

def location():
	print("Currently, you are in the " + user["location"] + ". You have " +  +
      " task(s) left in this room.")

# runs when impostor gets ejected, or no crewmates remain
def endgame(imposter_ejected):
	if imposter_ejected == True:
		print(assets.was_impos)
		print("The imposter was: ", end='')
		color_print(impostor["color"], imposter["color"], True)
	else:
		print(assets.was_not_impos)
	
	if user["wrong votes"]>impostor["kill count"]:
		print('')

	# imposter kills-based endings
	if impostor["kill count"]==0:
		# all crewmates live (4/4)
		print('')
	
	if impostor["kill count"]==1:
		# 3 crewmates live (3/4)
		print('')
	
	if impostor["kill count"]==2:
		# 2 crewmates live (2/4)
		print('')
		
	if impostor["kill count"]==3:
		# 1 crewmates live (1/4)
		print('')
			
	if impostor["kill count"]==4:
		# no crewmates live (0/4, (you))
		print('')
