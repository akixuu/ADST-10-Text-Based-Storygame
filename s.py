import time
import sys
def dotdotdot():
	for x in range(3):
		sys.stdout.write(".")
		sys.stdout.flush()
		time.sleep(0.05)
	print("\n")

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
typingPrint("text")
dotdotdot();