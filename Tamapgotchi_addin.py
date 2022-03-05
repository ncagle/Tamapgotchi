# -*- coding: utf-8 -*-
import arcpy
import pythonaddins as adn
from random import choice
from datetime import datetime


########## Variable Definitions ##########

today = datetime.today().strftime('%m-%d')
boredom_decrement = 3
hunger_decrement = 6
danger_decrement = 2
boredom_threshold = 15
hunger_threshold = 15
sleep_threshold = 30
count = 0
Mametchi = u"""
  ⠀⠀⠀⠀|▔|▔|▔|█|█|█|▔|▔|▔|▔|█|█|█|▔|▔|▔|
  ⠀⠀⠀⠀|▔|▔|█|█|▔|▔|█|▔|▔|█|▔|▔|█|█|▔|▔|
  ⠀⠀⠀⠀|▔|▔|█|█|▔|▔|█|▔|▔|█|▔|▔|█|█|▔|▔|
  ⠀⠀⠀⠀|▔|▔|█|█|█|█|█|█|█|█|█|█|█|█|▔|▔|
  ⠀⠀⠀⠀|▔|▔|█|█|█|█|█|█|█|█|█|█|█|█|▔|▔|
  ⠀⠀⠀⠀|▔|▔|█|▔|▔|▔|▔|▔|▔|▔|▔|▔|▔|█|▔|▔|
  ⠀⠀⠀⠀|▔|█|▔|█|█|█|▔|▔|▔|█|█|█|▔|▔|█|▔|
  ⠀⠀⠀⠀|▔|█|▔|█|█|▔|█|▔|▔|█|█|▔|█|▔|█|▔|
  ⠀⠀⠀⠀|▔|█|▔|█|█|▔|█|▔|▔|█|█|▔|█|▔|█|▔|
  ⠀⠀⠀⠀|▔|█|▔|█|█|█|▔|▔|▔|█|█|█|▔|▔|█|▔|
  ⠀⠀⠀⠀|▔|▔|█|▔|▔|▔|▔|█|█|▔|▔|▔|▔|█|▔|▔|
  ⠀⠀⠀⠀|▔|▔|▔|█|█|█|█|█|█|█|█|█|█|▔|▔|▔|
  ⠀⠀⠀⠀|▔|▔|▔|▔|█|▔|▔|▔|▔|▔|▔|█|▔|▔|▔|▔|
  ⠀⠀⠀⠀|▔|▔|▔|█|▔|█|▔|▔|▔|▔|█|▔|█|▔|▔|▔|
  ⠀⠀⠀⠀|▔|▔|▔|█|█|█|▔|▔|▔|▔|█|█|█|▔|▔|▔|
  ⠀⠀⠀⠀|▔|▔|▔|▔|▔|█|▔|█|█|▔|█|▔|▔|▔|▔|▔|
  ⠀⠀⠀⠀|▔|▔|▔|▔|▔|█|█|▔|▔|█|█|▔|▔|▔|▔|▔|
  ⠀⠀⠀⠀|▔|▔|▔|▔| M  A  M  E  T  C  H  I |▔|▔|▔|▔|
⠀⠀⠀⠀
        """
Neliatchi = u"""
      |▔|▔|█|▔|█|▔|▔|▔|▔|▔|▔|▔|▔|█|▔|█|▔|▔|
      |▔|▔|▔|█|▔|█|█|█|█|█|█|█|█|▔|█|▔|▔|▔|
      |▔|▔|█|▔|█|▔|▔|█|▔|▔|█|▔|▔|█|▔|█|▔|▔|
      |▔|█|▔|█|▔|▔|▔|▔|█|█|▔|▔|▔|▔|█|▔|█|▔|
      |▔|█|▔|█|▔|█|█|▔|▔|▔|▔|█|█|▔|█|▔|█|▔|
      |▔|█|▔|█|▔|█|▔|▔|▔|▔|▔|▔|█|▔|█|▔|█|▔|
      |▔|█|▔|█|▔|█|█|▔|▔|▔|▔|█|█|▔|█|▔|█|▔|
      |▔|█|▔|█|▔|▔|▔|▔|█|█|▔|▔|▔|▔|█|▔|█|▔|
      |▔|█|▔|█|▔|▔|▔|▔|▔|▔|▔|▔|▔|▔|█|▔|█|▔|
      |▔|█|▔|▔|█|▔|▔|▔|▔|▔|▔|▔|▔|█|▔|▔|█|▔|
      |▔|█|▔|█|▔|█|█|█|▔|▔|█|█|█|▔|█|▔|█|▔|
      |▔|█|▔|█|▔|█|▔|▔|█|█|▔|▔|█|▔|█|▔|█|▔|
      |▔|█|▔|▔|▔|█|▔|▔|▔|▔|▔|▔|█|▔|▔|▔|█|▔|
      |▔|█|▔|▔|█|▔|█|█|█|█|█|█|▔|█|▔|▔|█|▔|
      |▔|▔|█|█|▔|█|▔|▔|█|█|▔|▔|█|▔|█|█|▔|▔|
      |▔|▔|▔|▔|▔|█|▔|▔|▔|▔|▔|▔|█|▔|▔|▔|▔|▔|
      |▔|▔|▔|▔|▔|█|▔|▔|█|█|▔|▔|█|▔|▔|▔|▔|▔|
      |▔|▔|▔|▔|▔|▔|█|█|▔|▔|█|█|▔|▔|▔|▔|▔|▔|
      |▔|▔|▔|▔|▔| N  E  L  I  A  T  C  H  I |▔|▔|▔|▔|▔|
    
        """
Soyofuwatchi = u"""
      |▔|▔|▔|▔|▔|█|█|█|█|█|█|█|█|▔|▔|▔|▔|▔|
      |▔|▔|▔|█|█|▔|▔|█|▔|█|▔|█|▔|█|█|▔|▔|▔|
      |▔|▔|█|▔|▔|▔|▔|▔|▔|▔|▔|▔|▔|▔|▔|█|▔|▔|
      |▔|█|▔|▔|▔|█|█|▔|▔|▔|▔|█|█|▔|▔|▔|█|▔|
      |▔|█|▔|▔|▔|█|█|▔|▔|▔|▔|█|█|▔|▔|▔|█|▔|
      |▔|█|▔|▔|█|▔|▔|▔|▔|▔|▔|▔|▔|█|▔|▔|█|▔|
      |▔|█|▔|▔|▔|▔|▔|█|▔|▔|█|▔|▔|▔|▔|▔|█|▔|
      |▔|▔|█|▔|▔|▔|▔|▔|█|█|▔|▔|▔|▔|▔|█|▔|▔|
      |▔|▔|▔|█|█|▔|▔|▔|▔|▔|▔|▔|▔|█|█|▔|▔|▔|
      |▔|▔|▔|▔|▔|█|█|█|█|█|█|█|█|▔|▔|▔|▔|▔|
      |▔|▔|▔|▔|█|▔|▔|▔|▔|▔|▔|▔|▔|█|▔|▔|▔|▔|
      |▔|▔|▔|█|▔|█|▔|█|▔|█|▔|█|▔|█|▔|▔|▔|▔|
      |▔|▔|▔|█|▔|█|▔|█|▔|█|▔|█|▔|█|▔|▔|▔|▔|
      |▔|▔|▔|█|▔|▔|█|▔|▔|▔|█|▔|▔|▔|█|▔|▔|▔|
      |▔|▔|▔|▔|█|▔|▔|▔|▔|▔|▔|▔|▔|▔|█|▔|▔|▔|
      |▔|▔|▔|▔|█|▔|▔|▔|█|▔|▔|▔|█|▔|▔|█|▔|▔|
      |▔|▔|▔|▔|▔|█|▔|█|▔|█|▔|█|▔|█|▔|█|▔|▔|
      |▔|▔|▔|▔|▔|▔|█|█|▔|▔|█|█|▔|▔|█|█|▔|▔|
      |▔|▔|▔| S  O  Y  O  F  U  W  A  T  C  H  I |▔|▔|▔|

        """
tamagotchis = [Mametchi, Neliatchi, Soyofuwatchi]
new_pet = choice(tamagotchis)
name = "text"
hunger = 3
starve = 0
boredom = 1
abandoned = 0
sleep = 5
awake = True
zzz = 0
hp = 15
lights = True # Light on
poop = False # No poop
sick = False
dead = True
switch = False
editing = False
start = False
happiness_check = ["           I'm happy! ", "           I'm fine.  ", "           I'm sad... "]
hunger_check = ["I'm full!     ", "I'm hungry.   ", "I'm starving!!"]
health_check = ["I feel great!    ", "I've felt better.", "I feel awful.    "]
# Column vars for menu formatting
c1r1 = happiness_check[0]
c2r1 = hunger_check[0]
c3r1 = health_check[0]
c1r2 = "Yes"
c2r2 = "No "
c3r2 = "No "
c2r3 = "The light is on."
# Easter Egg dictionary
date_dict = {
  "01-01": "Happy New Year!",
  "01-21": "Hug your vaccinated friends. It's National Hugging Day!",
  "02-09": "It's National Pizza Day!",
  "02-16": "Party like it's Mardi Gras!",
  "02-22": "Have a drink. It's National Margarita Day!",
  "03-14": "3.141592653. Eat a slice of Pi today!",
  "03-15": "Et tu, Brute? Beware the Ides of March!",
  "03-17": "Drink til yer green around ye gills. It's St. Patty's Day!",
  "03-20": "Go outside. It's the Spring Equinox, Ostara!",
  "04-01": "This tool just deleted a random feature. April Fools!",
  "04-07": "Crack open a cold one with the boys. It's National Beer Day!",
  "04-20": "Is it legal yet? Take a big breath and relax, man!",
  "04-22": "Reduce, Reuse, Recycle. Happy Earth Day!",
  "04-30": "Go hug a tree. It's Arbor Day!",
  "05-01": "It's Free Comic Book Day at your local comic store!",
  "05-04": "May the Fourth be with you!",
  "05-05": "It's Revenge of the Fifth!",
  "05-09": "Don't forget to call your mother today!",
  "06-04": "Sweet relief. It's National Donut Day!",
  "06-19": "Never forget your history. It's Juneteenth!",
  "06-20": "He'll come back with the milk soon. Happy Father's Day.",
  "06-20": "Get a tan. It's the Summer Solstice, Litha!",
  "07-18": "Chill out. It's National Ice Cream Day!",
  "09-22": "Get a good book and fuzzy socks. It's the Fall Equinox, Mabon!",
  "09-29": "Time for an all-nighter. It's National Coffee Day!",
  "10-31": "Spooky, scary skeletons abound. Happy Halloween!",
  "11-05": "Remember, remember, the 5th of November. It's Guy Fawkes Day!",
  "11-25": "Time for food and family feuds. Happy Thanksgiving!",
  "12-21": "Tis the season. It's the Winter Solstice, Yule!"
}
# Ascii art for message boxes
on = ur"""
            .      |      .
              \    '    /
                ` ,--⹁ '
          ---⠀(  ~ )⠀---
                  \⠀/
                _| ≡|_
               |_____|
                  ON
"""
off = ur"""
                  __
                ( ~ )
                 \_/
               _| ≡|_
              |_____|
                OFF
"""
game = ur"""
              .-----------.        _______
            /      o      /|      /\           \
          /________ /o|    /o  \    o    \
          |  o          |   |  /      o\______\
          |      o      |o/  \o      /o        /
          |          o  |/      \  o/     o    /
          '-----------'          \/_____o/
"""
bone = ur"""
        .--.        .----.﹏,--.        ,--.
      (       `----(                \----'     `)
        >=        )                 )     =<
      (       ,----(     {#}       /----,      )
        `--'         `----------'         `--'
"""
poo = ur"""
                   "."
                         ༼༽  "."
                       ༼ ¯ ༽ 
                     ༼ ¯¯¯ ༽
                     ¯¯¯¯¯¯
"""
meds = ur"""
               [I I I I I]
                 )'''''(
               /        \
             /     ╬     \
             |``--.....--'|
             | health |
             |``--.....--'|
       (\)   `.______.'(I)   (/)
           (I)    (/)(I)(\)
                 (I)
"""



########## Function Definitions ##########
# Addins have issues updating button.enabled and changing variables after
# outputting a message box. Seems the variables need to go before the
# message box.

#---------------#
def clock_tick():
#---------------#
    
    # For each change in selection, run checks and updates for the next pet status cycle
    global boredom, hunger, sleep, awake, count, poop, sick, hp, name, dead, zzz, starve, abandoned, switch
    #adn.MessageBox("Update\n", "Tick")

    # Only increment if not dead
    # While awake, increment all major status values
    if awake == True and dead == False:
        boredom += 1
        hunger += 1
        sleep += 1
    # After 30 cycles, fall asleep and turn off food and play options
    if sleep == sleep_threshold and dead == False and switch == False:
        awake = False
        switch = True #toggle variable for silencing messages about sleep while asleep
        feed.enabled = False
        play.enabled = False
        adn.MessageBox(name + " has fallen asleep.\n\nDon't forget to turn its light off.", "Bedtime")
    # Count 10 cycles of sleep and wake up and enable food and play options. resets switch toggle
    if awake == False and dead == False:
        if zzz < 10:
            zzz += 1
        elif zzz == 10:
            awake = True
            switch = False
            feed.enabled = True
            play.enabled = True
            adn.MessageBox(name + " has woken up.\n\nDon't forget to turn on the light.", "Good morning")
    # When asleep with the lights on, it's bad for its health
    # When awake with the lights off, it gets bored
    if awake == False and lights == True and dead == False:
        hp -=1
    elif awake == True and lights == False and dead == False:
        boredom += 1
    # After being full for one cycle, pet poops
    if hunger == 1 and dead == False:
        poop = True
        adn.MessageBox(name + " has left a mess.", "Uh-oh!")
    # If poop is left with the pet for 4 cycles, it will get sick and reset the cycle count
    if poop == True and count >= 4 and dead == False:
        sick = True
        count = 0
        adn.MessageBox(name + " has gotten sick!\n\nThey need medicine to feel better.\n\nDon't forget to clean up after your pet.", u"【•﹏•】 I don't feel so good.")
    # Remaining sick reduces health by 2 every cycle
    if sick == True and dead == False:
        hp -= 2
    # Hunger warning 2 cycles before starving
    # Begins starve counter for health reduction when forgetting to feed for too long
    if hunger >= 13 and dead == False:
        if hunger == 13:
            adn.MessageBox("I'm hungry!", name)
        starve += 1
        if starve >= 3:
            hp -= 1
    # Boredom warning 2 cycles before extreme sadness
    # Begins abandonment count as the pet begins to realize the inevitable loss of all who care for them and embrace the everlasting void of loneliness the consumes all happiness and leaves nothing but a husk of the former self longing for an end to its existence
    # Affects health after 3 if not played with.
    if boredom >= 13 and dead == False:
        if boredom == 13:
            adn.MessageBox("I'm bored...", name)
        abandoned += 1
        if abandoned >= 3:
            hp -= 1
    # Locks buttons when pet dies at 0 hp
    if hp <= 0 and dead == False:
        adn.MessageBox(name + " has passed away from an illness.", u"💀 R.I.P. 💀")
        dead = True
        feed.enabled = False
        play.enabled = False
        light.enabled = False
        clean.enabled = False
        medicine.enabled = False

    # Increment cycle count
    # Epicyle of length 7
    count += 1
    if count >= 7:
        count = 0

#-----------#
def do_egg():
#-----------#
    
    # Chooses new pet and reestablishes button options
    global new_pet, name, dead, tamagotchis, start, Mametchi, Neliatchi, Soyofuwatchi, editing
    # Keeps buttons active during edit session after its been activated and off when needed
    if editing == True:
        dead = False
        free.enabled = True
        # Choose a new pet from the list
        new_pet = choice(tamagotchis)
        health.enabled = True
        feed.enabled = True
        play.enabled = True
        light.enabled = True
        clean.enabled = True
        medicine.enabled = True
        # Sets the name based on the choice and introduces the pet
        if new_pet == Mametchi:
            name = "Mametchi"
            start = True
            adn.MessageBox(Mametchi, u"❤ Meet Mametchi! ❤")
            adn.MessageBox("Please click anywhere on the screen.", "ArcMap Quirk")
        elif new_pet == Neliatchi:
            name = "Neliatchi"
            start = True
            adn.MessageBox(Neliatchi, u"❤ Meet Neliatchi! ❤")
            adn.MessageBox("Please click anywhere on the screen.", "ArcMap Quirk")
        elif new_pet == Soyofuwatchi:
            name = "Soyofuwatchi"
            start = True
            adn.MessageBox(Soyofuwatchi, u"❤ Meet Soyofuwatchi! ❤")
            adn.MessageBox("Please click anywhere on the screen.", "ArcMap Quirk")
    elif editing == False:
        adn.MessageBox("Please start an editing session to interact with your pet.", "Start")    
    
#-----------------#
def check_health():
#-----------------#
    
    # Checks values and formats and displays the status menu and image of your pet
    global c1r1, c2r1, c3r1, c1r2, c2r2, c3r2, c2r3, name, dead
    text1 = "line 1"
    text2 = "line 2"
    text3 = "line 3"
    top = u"╔════════════════════════════════════════════╗"
    on = "The light is on."
    off = "The light is off."

    # Evaluates happiness to assign rank string to column 1 row 1
    if boredom <= 4:
        c1r1 = happiness_check[0]
    elif boredom > 4 and boredom < 11:
        c1r1 = happiness_check[1]
    elif boredom >= 11:
        c1r1 = happiness_check[2]
    # Evaluates hunger to assign rank string to column 2 row 1
    if hunger <= 4:
        c2r1 = hunger_check[0]
    elif hunger > 4 and hunger < 11:
        c2r1 = hunger_check[1]
    elif hunger >= 11:
        c2r1 = hunger_check[2]
    # Evaluates HP to assign rank string to column 3 row 1
    if hp >= 11:
        c3r1 = health_check[0]
    elif hp < 11 and hp > 4:
        c3r1 = health_check[1]
    elif hp <= 4:
        c3r1 = health_check[2]

    if awake == False:
        c1r2 = "Yes"
    elif awake == True:
        c1r2 = "No "
    if poop == True:
        c2r2 = "Yes"
    elif poop == False:
        c2r2 = "No "
    if sick == True:
        c3r2 = "Yes"
    elif sick == False:
        c3r2 = "No "
    if lights == True:
        c2r3 = on
    elif lights == False:
        c2r3 = off

    # String formatting to build a fancy menu. Also fuck how ArcMap interprets unicode characters. 
    text1 = c1r1 + " {:^24} ".format(c2r1) + c3r1
    text2 = u"           Asleep: " + c1r2 + " {:^20} ".format("Soiled: " + c2r2) + "   Sick: " + c3r2
    text3 = u"╚═══════════════  " + c2r3 + u"  ══════════════╝"
    adn.MessageBox(top + "\n" + text1 + u"\n ─────────────────────────────────────────────\n" + text2 + u"\n ─────────────────────────────────────────────\n" + text3 + "\n\n" + new_pet, "Health status of " + name + ".")

#------------#
def do_feed():
#------------#

    # Feed decreases hunger value by the decrement amount
    global hunger, hp, hunger_decrement
    if hunger > 0:
        hunger = max(0, hunger - hunger_decrement)
    # If already full, overfeeding causes damage
    elif hunger <= 0:
        hp -= 1
        hunger = 0            
    adn.MessageBox("Fed " + name + ".\n\nCareful not to overfeed.\n" + bone, "Feed")

#------------#
def do_play():
#------------#

    # Playing decreases boredom value and makes the pet more tired
    global boredom, boredom_decrement, sleep
    boredom = max(0, boredom - boredom_decrement)
    sleep += 2
    adn.MessageBox("Played with " + name + ".\n\nHappiness increased.\n" + game, "Play")

#-------------#
def do_light():
#-------------#

    # Turns the light on or off (Pretty straightforward)
    global lights, on, off
    bulb = ""
    if lights == True:
        bulb = off
        adn.MessageBox("Turned off the light.\n" + bulb, "Lights")
    elif lights == False:
        bulb = on
        adn.MessageBox("Turned on the light.\n" + bulb, "Lights")
    lights = not lights

#-------------#
def do_clean():
#-------------#

    # Does some shit
    global poop
    if poop == True:
        poop = False
    adn.MessageBox("Cleaned up " + name + "'s mess.\n" + poo, "Clean")

#----------------#
def do_medicine():
#----------------#

    # Heals sickness and resets health or just heals 2 normally
    global sick, hp
    if sick == True:
        sick = False
        hp = 10
    elif hp < 9:
        hp += 2
    adn.MessageBox("Healed " + name + ".\n" + meds, "Medicine")

#------------#
def do_free():
#------------#

    # Frees the current pet and reestablishes conditions for creating a new pet while allowing viewing of the status of the previous pet
    global dead, hunger, start, boredom, sleep, awake, hp, lights, poop, sick, dead, c1r1, c2r1, c3r1, c1r2, c2r2, c3r2, c2r3
    # Disables the buttons until a new pet is made
    egg.enabled = True
    health.enabled = False
    feed.enabled = False
    play.enabled = False
    light.enabled = False
    clean.enabled = False
    medicine.enabled = False
    # Resets variables for next pet
    hunger = 3
    starve = 0
    boredom = 1
    abandoned = 0
    sleep = 5
    zzz = 0
    awake = True
    hp = 10
    lights = True # Light on
    poop = False # No poop
    sick = False
    switch = False
    c1r1 = happiness_check[0]
    c2r1 = hunger_check[0]
    c3r1 = health_check[0]
    c1r2 = "Yes"
    c2r2 = "No "
    c3r2 = "No "
    c2r3 = "The light is on."

    # Changes message if pet is dead or alive
    if dead == False:
        dead = True
        start = False
        adn.MessageBox(name + " has been freed to live in the wild.\n\nYou can now hatch a new egg.", name + " is now free!")
        adn.MessageBox("Please click anywhere on the screen.", "ArcMap Quirk")
    elif dead == True:
        start = False
        adn.MessageBox(name + " has been buried.\n\n" + new_pet, "In Memoriam")
        adn.MessageBox("Please click anywhere on the screen.", "ArcMap Quirk")


########## Extension Class ##########

class Extension(object):
    """Implementation for Tamapgotchi_addin.tick (Extension)"""
    def __init__(self):
        self.enabled = True
    def onEditorSelectionChanged(self):
        global start
        clock_tick()
        if start == True:
            egg.enabled = False
        elif start == False:
            free.enabled = False
    def onStartEditing(self):
        global editing, dead
        editing = True
        if dead == False:
            feed.enabled = True
            play.enabled = True
            light.enabled = True
            clean.enabled = True
            medicine.enabled = True
    def onStopEditing(self, save_changes):
        global editing
        editing = False
        feed.enabled = False
        play.enabled = False
        light.enabled = False
        clean.enabled = False
        medicine.enabled = False



########## Button Classes ###########

class egg(object):
    """Implementation for Tamapgotchi_addin.egg (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        do_egg()

class health(object):
    """Implementation for Tamapgotchi_addin.health (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        check_health()

class feed(object):
    """Implementation for Tamapgotchi_addin.feed (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        do_feed()

class play(object):
    """Implementation for Tamapgotchi_addin.play (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        do_play()

class light(object):
    """Implementation for Tamapgotchi_addin.light (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        do_light()

class clean(object):
    """Implementation for Tamapgotchi_addin.clean (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        do_clean()

class medicine(object):
    """Implementation for Tamapgotchi_addin.medicine (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        do_medicine()

class free(object):
    """Implementation for Tamapgotchi_addin.free (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False
    def onClick(self):
        do_free()

class about(object):
    """Implementation for Tamapgotchi_addin.about (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        global today
        if today not in date_dict.keys():
            adn.MessageBox("This toolbar was an experiment on the capabilities\nand limits of python addins. The scripting necessary\nto acheive the button functions had to be very specific.\nArcMap's Unicode decoder does not take kindly to text\nart at all. The status updates come from an extension\ntracking changes during an edit session. Not surprisingly,\nit was difficult to program a 90's toy into industry\nleading mapping software. Yet it was not only possible,\nbut also fun, highly educational, and entirely unnecessary!\nThis knowledge will enable me to create a wide variety\nof solutions with custom addins.", "Not an easter egg today.")
        if today in date_dict.keys():
            adn.MessageBox("This toolbar was an experiment on the capabilities\nand limits of python addins. The scripting necessary\nto acheive the button functions had to be very specific.\nArcMap's Unicode decoder does not take kindly to text\nart at all. The status updates come from an extension\ntracking changes during an edit session. Not surprisingly,\nit was difficult to program a 90's toy into industry\nleading mapping software. Yet it was not only possible,\nbut also fun, highly educational, and entirely unnecessary!\nThis knowledge will enable me to create a wide variety\nof solutions with custom addins.", date_dict[today])



########## Trash Pile ##########

# This is all the iterations of art for the tamagotchis. ArcMap does not understand the fact that unicode is supposed to be universal
# I finally had the art working and thought maybe I'd add some unicode emojis to the menu. It forced some kind of update interally
# and everything broke. It drew the characters entirely different. I even rolled back to an old version and it reinterpreted them
# incorrectly again. If you'll notice, all my ascii art looks janky in the code. I started looking normal but Arc can't handle regular
# character spacing. So here is my graveyard of attempts to force this thing to work.

##Mametchi3 = u"""
##⠀⠀⠀⠀⠀⠀⠀⠀╔═════════════════════════════════╗
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|⠀|███|⠀|⠀|⠀|⠀|███|⠀|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|██|⠀|⠀|█|⠀|⠀|█|⠀|⠀|██|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|██|⠀|⠀|█|⠀|⠀|█|⠀|⠀|██|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|████████████|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|████████████|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|█|⠀|⠀|⠀|⠀|⠀|⠀|⠀|⠀|⠀|⠀|█|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|█|⠀|███|⠀|⠀|⠀|███|⠀|⠀|█|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|█|⠀|██|⠀|█|⠀|⠀|██|⠀|█|⠀|█|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|█|⠀|██|⠀|█|⠀|⠀|██|⠀|█|⠀|█|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|█|⠀|███|⠀|⠀|⠀|███|⠀|⠀|█|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|█|⠀|⠀|⠀|⠀|██|⠀|⠀|⠀|⠀|█|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|⠀|██████████|⠀|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|⠀|⠀|█|⠀|⠀|⠀|⠀|⠀|⠀|█|⠀|⠀|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|⠀|█|⠀|█|⠀|⠀|⠀|⠀|█|⠀|█|⠀|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|⠀|███|⠀|⠀|⠀|⠀|███|⠀|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|⠀|⠀|⠀|█|⠀|██|⠀|█|⠀|⠀|⠀|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|⠀|⠀|⠀|██|⠀|⠀|██|⠀|⠀|⠀|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|⠀|⠀|M|a|m|e|t|c|h|i|⠀|⠀|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀╚═════════════════════════════════╝
##        """
##Mametchi4 = u"""
##⠀⠀⠀⠀|░|░|░|█|█|█|░|░|░|░|█|█|█|░|░|░|
##⠀⠀⠀⠀|░|░|█|█|░|░|█|░|░|█|░|░|█|█|░|░|
##⠀⠀⠀⠀|░|░|█|█|░|░|█|░|░|█|░|░|█|█|░|░|
##⠀⠀⠀⠀|░|░|█|█|█|█|█|█|█|█|█|█|█|█|░|░|
##⠀⠀⠀⠀|░|░|█|█|█|█|█|█|█|█|█|█|█|█|░|░|
##⠀⠀⠀⠀|░|░|█|░|░|░|░|░|░|░|░|░|░|█|░|░|
##⠀⠀⠀⠀|░|█|░|█|█|█|░|░|░|█|█|█|░|░|█|░|
##⠀⠀⠀⠀|░|█|░|█|█|░|█|░|░|█|█|░|█|░|█|░|
##⠀⠀⠀⠀|░|█|░|█|█|░|█|░|░|█|█|░|█|░|█|░|
##⠀⠀⠀⠀|░|█|░|█|█|█|░|░|░|█|█|█|░|░|█|░|
##⠀⠀⠀⠀|░|░|█|░|░|░|░|█|█|░|░|░|░|█|░|░|
##⠀⠀⠀⠀|░|░|░|█|█|█|█|█|█|█|█|█|█|░|░|░|
##⠀⠀⠀⠀|░|░|░|░|█|░|░|░|░|░|░|█|░|░|░|░|
##⠀⠀⠀⠀|░|░|░|█|░|█|░|░|░|░|░|░|█|░|░|░|
##⠀⠀⠀⠀|░|░|░|█|█|█|░|░|░|░|█|█|█|░|░|░|
##⠀⠀⠀⠀|░|░|░|░|░|█|░|█|█|░|█|░|░|░|░|░|
##⠀⠀⠀⠀|░|░|░|░|░|█|█|░|░|█|█|░|░|░|░|░|
##⠀⠀⠀⠀|░|░|░|░| M  A  M  E  T  C  H  I |░|░|░|░|
##⠀⠀⠀⠀
##        """
##Mametchi5 = u"""
##⠀⠀⠀⠀⠀⠀⠀⠀╔═════════════════════════════════╗
##⠀⠀⠀⠀⠀⠀⠀⠀║▁▁▁███▁▁▁▁███▁▁▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁▁██▁▁█▁▁█▁▁██▁▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁▁██▁▁█▁▁█▁▁██▁▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁▁████████████▁▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁▁████████████▁▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁▁█▁▁▁▁▁▁▁▁▁▁█▁▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁█▁███▁▁▁███▁▁█▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁█▁██▁█▁▁██▁█▁█▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁█▁██▁█▁▁██▁█▁█▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁█▁███▁▁▁███▁▁█▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁▁█▁▁▁▁██▁▁▁▁█▁▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁▁▁██████████▁▁▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁▁▁▁█▁▁▁▁▁▁█▁▁▁▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁▁▁█▁█▁▁▁▁█▁█▁▁▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁▁▁███▁▁▁▁███▁▁▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁▁▁▁▁█▁██▁█▁▁▁▁▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁▁▁▁▁██▁▁██▁▁▁▁▁║
##⠀⠀⠀⠀⠀⠀⠀⠀║▁▁▁▁|M|a|m|e|t|c|h|i|▔▔▔▔║
##⠀⠀⠀⠀⠀⠀⠀⠀╚═════════════════════════════════╝
##        """
##Mametchi6 = u"""
##⠀⠀⠀⠀|▔|▔|▔|█|█|█|▔|▔|▔|▔|█|█|█|▔|▔|▔|
##⠀⠀⠀⠀|▔|▔|█|█|▔|▔|█|▔|▔|█|▔|▔|█|█|▔|▔|
##⠀⠀⠀⠀|▔|▔|█|█|▔|▔|█|▔|▔|█|▔|▔|█|█|▔|▔|
##⠀⠀⠀⠀|▔|▔|█|█|█|█|█|█|█|█|█|█|█|█|▔|▔|
##⠀⠀⠀⠀|▔|▔|█|█|█|█|█|█|█|█|█|█|█|█|▔|▔|
##⠀⠀⠀⠀|▔|▔|█|▔|▔|▔|▔|▔|▔|▔|▔|▔|▔|█|▔|▔|
##⠀⠀⠀⠀|▔|█|▔|█|█|█|▔|▔|▔|█|█|█|▔|▔|█|▔|
##⠀⠀⠀⠀|▔|█|▔|█|█|▔|█|▔|▔|█|█|▔|█|▔|█|▔|
##⠀⠀⠀⠀|▔|█|▔|█|█|▔|█|▔|▔|█|█|▔|█|▔|█|▔|
##⠀⠀⠀⠀|▔|█|▔|█|█|█|▔|▔|▔|█|█|█|▔|▔|█|▔|
##⠀⠀⠀⠀|▔|▔|█|▔|▔|▔|▔|█|█|▔|▔|▔|▔|█|▔|▔|
##⠀⠀⠀⠀|▔|▔|▔|█|█|█|█|█|█|█|█|█|█|▔|▔|▔|
##⠀⠀⠀⠀|▔|▔|▔|▔|█|▔|▔|▔|▔|▔|▔|█|▔|▔|▔|▔|
##⠀⠀⠀⠀|▔|▔|▔|█|▔|█|▔|▔|▔|▔|▔|▔|█|▔|▔|▔|
##⠀⠀⠀⠀|▔|▔|▔|█|█|█|▔|▔|▔|▔|█|█|█|▔|▔|▔|
##⠀⠀⠀⠀|▔|▔|▔|▔|▔|█|▔|█|█|▔|█|▔|▔|▔|▔|▔|
##⠀⠀⠀⠀|▔|▔|▔|▔|▔|█|█|▔|▔|█|█|▔|▔|▔|▔|▔|
##⠀⠀⠀⠀|▔|▔|▔|▔| M  A  M  E  T  C  H  I |▔|▔|▔|▔|
##⠀⠀⠀⠀
##        """
##Mametchi7 = u"""
##⠀⠀⠀⠀|░|░|░|█|█|█|░|░|░|░|█|█|█|░|░|░|
##⠀⠀⠀⠀|░|░|█|█|▒|▒|█|░|░|█|▒|▒|█|█|░|░|
##⠀⠀⠀⠀|░|░|█|█|▒|▒|█|░|░|█|▒|▒|█|█|░|░|
##⠀⠀⠀⠀|░|░|█|█|█|█|█|█|█|█|█|█|█|█|░|░|
##⠀⠀⠀⠀|░|░|█|█|█|█|█|█|█|█|█|█|█|█|░|░|
##⠀⠀⠀⠀|░|░|█|▒|▒|▒|▒|▒|▒|▒|▒|▒|▒|█|░|░|
##⠀⠀⠀⠀|░|█|▒|█|█|█|▒|▒|▒|█|█|█|▒|▒|█|░|
##⠀⠀⠀⠀|░|█|▒|█|█|░|█|▒|▒|█|█|░|█|▒|█|░|
##⠀⠀⠀⠀|░|█|▒|█|█|░|█|▒|▒|█|█|░|█|▒|█|░|
##⠀⠀⠀⠀|░|█|▒|█|█|█|▒|▒|▒|█|█|█|▒|▒|█|░|
##⠀⠀⠀⠀|░|░|█|▒|▒|▒|▒|█|█|▒|▒|▒|▒|█|░|░|
##⠀⠀⠀⠀|░|░|░|█|█|█|█|█|█|█|█|█|█|░|░|░|
##⠀⠀⠀⠀|░|░|░|░|█|▒|▒|▒|▒|▒|▒|█|░|░|░|░|
##⠀⠀⠀⠀|░|░|░|█|▒|█|▒|▒|▒|▒|█|▒|█|░|░|░|
##⠀⠀⠀⠀|░|░|░|█|█|█|▒|▒|▒|▒|█|█|█|░|░|░|
##⠀⠀⠀⠀|░|░|░|░|░|█|▒|█|█|▒|█|░|░|░|░|░|
##⠀⠀⠀⠀|░|░|░|░|░|█|█|░|░|█|█|░|░|░|░|░|
##⠀⠀⠀⠀|░|░|░|░| M  A  M  E  T  C  H  I |░|░|░|░|
##⠀⠀⠀⠀
##        """
##Neliatchi = u"""
##    |░|░|█|░|█|░|░|░|░|░|░|░|░|█|░|█|░|░|
##    |░|░|░|█|░|█|█|█|█|█|█|█|█|||░|█|░|░|░|
##    |░|░|█|▒|█|▒|▒|█|▒|▒|█|▒|▒|█|▒|█|░|░|
##    |░|█|▒|█|▒|▒|▒|▒|█|█|▒|▒|▒|▒|█|▒|█|░|
##    |░|█|▒|█|▒|█|█|▒|▒|▒|▒|█|█|▒|█|▒|█|░|
##    |░|█|▒|█|▒|█|▒|▒|▒|▒|▒|▒|█|▒|█|▒|█|░|
##    |░|█|▒|█|▒|█|█|▒|▒|▒|▒|█|█|▒|█|▒|█|░|
##    |░|█|▒|█|▒|▒|▒|▒|█|█|▒|▒|▒|▒|█|▒|█|░|
##    |░|█|▒|█|▒|▒|▒|▒|▒|▒|▒|▒|▒|▒|█|▒|█|░|
##    |░|█|▒|▒|█|▒|▒|▒|▒|▒|▒|▒|▒|█|▒|▒|█|░|
##    |░|█|▒|█|▒|█|█|█|▒|▒|█|█|█||▒|█||▒|█|░|
##    |░|█|▒|█|▒|█|▒|▒|█|█|▒|▒|█|▒|█|▒|█|░|
##    |░|█|▒|▒|▒|█|▒|▒|▒|▒|▒|▒|█|▒|▒|▒|█|░|
##    |░|█|▒|▒|█|░|█|█|█|█|█|█|░|█|▒|▒|█|░|
##    |░|░|█|█|░|█|▒|▒|█|█|▒|▒|█|░|█|█|░|░|
##    |░|░|░|░|░|█|▒|▒|▒|▒|▒|▒|█|░|░|░|░|░|
##    |░|░|░|░|░|█|▒|▒|█|█|▒|▒|█|░|░|░|░|░|
##    |░|░|░|░|░|░|█|█|░|░|█|█|░|░|░|░|░|░|
##    |░|░|░|░|░| N  E  L  I  A  T  C  H  I |░|░|░|░|░|
##    
##        """
##Soyofuwatchi = u"""
##    |░|░|░|░|░|█|█|█|█|█|█|█|█|░|░|░|░|░|
##    |░|░|░|█|█|▒|▒|█|▒|█|▒|█|▒|█|█|░|░|░|
##    |░|░|█|▒|▒|▒|▒|▒|▒|▒|▒|▒|▒|▒|▒|█|░|░|
##    |░|█|▒|▒|▒|█|█|▒|▒|▒|▒|█|█|▒|▒|▒|█|░|
##    |░|█|▒|▒|▒|█|█|▒|▒|▒|▒|█|█|▒|▒|▒|█|░|
##    |░|█|▒|▒|█|▒|▒|▒|▒|▒|▒|▒|▒|█|▒|▒|█|░|
##    |░|█|▒|▒|▒|▒|▒|█|▒|▒|█|▒|▒|▒|▒|▒|█|░|
##    |░|░|█|▒|▒|▒|▒|▒|█|█|▒|▒|▒|▒|▒|█|░|░|
##    |░|░|░|█|█|▒|▒|▒|▒|▒|▒|▒|▒|█|█|░|░|░|
##    |░|░|░|░|░|█||█|█|█|█|█|█||█|░|░|░|░|░|
##    |░|░|░|░|█|▒|▒|▒|▒|▒|▒|▒|▒|█|░|░|░|░|
##    |░|░|░|█|▒|█|▒|█|▒|█|▒|█|▒|█|░|░|░|░|
##    |░|░|░|█|▒|█|▒|█|▒|█|▒|█|▒|█|░|░|░|░|
##    |░|░|░|█|▒|▒|█|▒|▒|▒|█|▒|▒|▒|█|░|░|░|
##    |░|░|░|░|█|▒|▒|▒|▒|▒|▒|▒|▒|▒|█|░|░|░|
##    |░|░|░|░|█|▒|▒|▒|█|▒|▒|▒|█|▒|▒|█|░|░|
##    |░|░|░|░|░|█|▒|█|░|█|▒|█|░|█|▒|█|░|░|
##    |░|░|░|░|░|░|█|█|░|░|█|█|░|░|█|█|░|░|
##    |░|░|░| S  O  Y  O  F  U  W  A  T  C  H  I |░|░|░|
##
##        """
##Mametchi_og = u"""
##⠀⠀⠀⠀⠀⠀⠀⠀╔══════════════════╗
##⠀⠀⠀⠀⠀⠀⠀⠀║⠀⠀⠀⠀▄▄▄⠀⠀⠀⠀▄▄▄⠀⠀⠀⠀║
##⠀⠀⠀⠀⠀⠀⠀⠀║⠀⠀⠀██⠀⠀█⠀⠀█⠀⠀██⠀⠀⠀║
##⠀⠀⠀⠀⠀⠀⠀⠀║⠀⠀⠀████████████⠀⠀⠀║
##⠀⠀⠀⠀⠀⠀⠀⠀║⠀⠀▄▀▄▄▄⠀⠀⠀▄▄▄⠀▀▄⠀⠀║
##⠀⠀⠀⠀⠀⠀⠀⠀║⠀⠀█⠀██⠀█⠀⠀██⠀█⠀█⠀⠀║
##⠀⠀⠀⠀⠀⠀⠀⠀║⠀⠀▀▄▀▀▀⠀▄▄▀▀▀⠀▄▀⠀⠀║
##⠀⠀⠀⠀⠀⠀⠀⠀║⠀⠀⠀⠀▀█▀▀▀▀▀▀█▀⠀⠀⠀⠀║
##⠀⠀⠀⠀⠀⠀⠀⠀║⠀⠀⠀⠀█▄█⠀⠀⠀⠀█▄█⠀⠀⠀⠀║
##⠀⠀⠀⠀⠀⠀⠀⠀║⠀⠀⠀⠀⠀⠀█▄▀▀▄█⠀⠀⠀⠀⠀⠀║
##⠀⠀⠀⠀⠀⠀⠀⠀║⠀⠀⠀⠀⠀Mametchi⠀⠀⠀⠀⠀║
##⠀⠀⠀⠀⠀⠀⠀⠀╚══════════════════╝
##⠀⠀⠀⠀⠀⠀⠀⠀"""
##
##Neliatchi_og = u"""
##        ╔══════════════════╗
##        ║  ▀▄▀▄▄▄▄▄▄▄▄▀▄▀  ║
##        ║ ▄▀▄▀  ▀▄▄▀  ▀▄▀▄ ║
##        ║ █ █ █▀    ▀█ █ █ ║
##        ║ █ █ ▀▀ ▄▄ ▀▀ █ █ ║
##        ║ █ ▀▄        ▄▀ █ ║
##        ║ █ █ █▀▀▄▄▀▀█ █ █ ║
##        ║ █  ▄▀▄▄▄▄▄▄▀▄  █ ║
##        ║  ▀▀ █  ▀▀  █ ▀▀  ║
##        ║     ▀▄▄▀▀▄▄▀     ║
##        ║     Neliatchi    ║
##        ╚══════════════════╝
##        """
##
##Soyofuwatchi_og = u"""
##        ╔══════════════════╗
##        ║   ▄▄▀▀█▀█▀█▀▄▄   ║
##        ║ ▄▀  ▄▄    ▄▄  ▀▄ ║
##        ║ █  ▄▀▀    ▀▀▄  █ ║
##        ║ ▀▄    ▀▄▄▀    ▄▀ ║
##        ║   ▀▀▄▄▄▄▄▄▄▄▀▀   ║
##        ║   ▄▀▄ ▄ ▄ ▄ █    ║
##        ║   █ ▀▄▀ ▀▄▀ ▀▄   ║
##        ║    █   ▄   ▄ ▀▄  ║
##        ║     ▀▄█ ▀▄█ ▀▄█  ║
##        ║   Soyofuwatchi   ║
##        ╚══════════════════╝
##        """
##
##testchar = u"""
##     ▁
##     ▂
##     ▃
##     ▄
##     ▅
##     ▆
##     ▇
##     █
##     ▉
##     ▊
##     ▋
##     ▌
##     ▍
##     ▎
##     ▏
##     
##     ░
##     ▒
##     ▓
##
##     |⠀|█|
##     
##     |▖|▗|▘|▝|
##
##     |▌|▐|▄|▀|
##     
##     |▙|▟|▛|▜|
##     
##     |▚|▞|_|
##     """
##
##Mametchi2 = u"""
##⠀⠀⠀⠀⠀⠀⠀⠀╔═════════════╗
##⠀⠀⠀⠀⠀⠀⠀⠀║ ▗▛▚   ▞▜▖ ║
##⠀⠀⠀⠀⠀⠀⠀⠀║ ▐▙▟▄▙▟▌   ║
##⠀⠀⠀⠀⠀⠀⠀⠀║ ▐▀▀▀▀▀▌   ║
##⠀⠀⠀⠀⠀⠀⠀⠀║ ▌   █▚  █▚▐ ║
##⠀⠀⠀⠀⠀⠀⠀⠀║ ▌   █▞  █▞▐ ║
##⠀⠀⠀⠀⠀⠀⠀⠀║ ▝▄▄█▄▄▘ ║
##⠀⠀⠀⠀⠀⠀⠀⠀║     ▞▖   ▗▚    ║
##⠀⠀⠀⠀⠀⠀⠀⠀║     ▀▌  ▄▐▀   ║
##⠀⠀⠀⠀⠀⠀⠀⠀║        ▀  ⠀▀      ║
##⠀⠀⠀⠀⠀⠀⠀⠀╚═════════════╝
##⠀⠀⠀⠀⠀⠀⠀⠀"""
##
##Mametchi3 = u"""
##⠀⠀⠀⠀⠀⠀⠀⠀╔═════════════════════════════════╗
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|⠀|█|█|█|⠀|⠀|⠀|⠀|█|█|█|⠀|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|█|█|⠀|⠀|█|⠀|⠀|█|⠀|⠀|█|█|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|█|█|⠀|⠀|█|⠀|⠀|█|⠀|⠀|█|█|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|█|█|█|█|█|█|█|█|█|█|█|█|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|█|█|█|█|█|█|█|█|█|█|█|█|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|█|⠀|⠀|⠀|⠀|⠀|⠀|⠀|⠀|⠀|⠀|█|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|█|⠀|█|█|█|⠀|⠀|⠀|█|█|█|⠀|⠀|█|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|█|⠀|█|█|⠀|█|⠀|⠀|█|█|⠀|█|⠀|█|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|█|⠀|█|█|⠀|█|⠀|⠀|█|█|⠀|█|⠀|█|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|█|⠀|█|█|█|⠀|⠀|⠀|█|█|█|⠀|⠀|█|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|█|⠀|⠀|⠀|⠀|█|█|⠀|⠀|⠀|⠀|█|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|⠀|█|█|█|█|█|█|█|█|█|█|⠀|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|⠀|⠀|█|⠀|⠀|⠀|⠀|⠀|⠀|█|⠀|⠀|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|⠀|█|⠀|█|⠀|⠀|⠀|⠀|█|⠀|█|⠀|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|⠀|█|█|█|⠀|⠀|⠀|⠀|█|█|█|⠀|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|⠀|⠀|⠀|█|⠀|█|█|⠀|█|⠀|⠀|⠀|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|⠀|⠀|⠀|█|█|⠀|⠀|█|█|⠀|⠀|⠀|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀║|⠀|⠀|⠀|⠀|M|a|m|e|t|c|h|i|⠀|⠀|⠀|⠀|║
##⠀⠀⠀⠀⠀⠀⠀⠀╚═════════════════════════════════╝
##        """
##
##from threading import Event, Thread
##def call_repeatedly(interval, func, *args):
##    stopped = Event()
##    def loop():
##        while not stopped.wait(interval): # the first call is in `interval` secs
##            func(*args)
##    Thread(target=loop).start()    
##    return stopped.set
##
##          ON
##        ╔════╗
##        ║ /```/
##        ║/___/
##        ║    ║
##        ║    ║
##        ╚════╝
##          OFF
##        ╔════╗
##        ║    ║
##        ║____║
##        ║\   \
##        ║ \,,,\
##        ╚════╝
##
##        
##             :
##         '.  _  .'
##        -=  (~)  =-   
##         .'  ≡  '.
##
##          __
##        ."  ".
##       (  ~~  )
##        \    /
##         "≡≡"
        
