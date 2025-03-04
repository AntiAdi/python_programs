import os

#Function to clear the screen.
def c():
    os.system("cls" if os.name=="nt" else "clear")
