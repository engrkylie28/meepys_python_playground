import inquirer
from random import randint
from time import sleep
from os import system
import pygame


pygame.mixer.init()
pygame.mixer.music.load('youlikejazz.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.play(-1, fade_ms=0)

player_hp = 190
spot_hp = 1500

bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_white = "\033[0;97m"
bright_cyan = "\033[0;96m"
bright_red = "\033[0;91m"
yellow = "\033[0;33m"

def miguel():
    print(bright_blue)
    print(r"""  ____________
 / __________ \
<_/   ⩌  ⩌   \_>
 <\__________/> 
 /|___// \\__|\
૮_|    \_/   |_ა 
   \___/ \___/
""")
    print(bright_white)
    
def miguelangry():
    print(bright_blue)
    print(r"""  ____________
 / __________ \
<_/ ꐦ⩌  ⩌   \_>
 <\__________/> 
 /|___// \\__|\
૮_|    \_/   |_ა 
   \___/ \___/
""")
    print(bright_white)

def gwen():
    print(bright_magenta)
    print(r"""
   __________
 / _________  \  
<\/  •́    •̀ \   >
  \_________/  /
 /|/_  \/  _\/\        
૮_|___\ _ /__|_ა        
   \___/ \___/
""")
    print(bright_white)
    
def miggy1():
    for i in range(2):
        miguel()
        sleep(.3)
        system("clear")
        miguelangry()
        sleep(.3)
        system("clear")
        miguel()
        sleep(.3)
        system("clear")

def spot():
    print(r"""
   __________
 /    ⢸⡇⢸⡇    \
 |   ⢸⡇⢸⡇⢸⡇   |
 \____________/
 /|⢸⡇⢸⡇     |\
૮_|    _ ⢸⡇⢸|_ა 
  \___/ \___/
""")


def spotangry():
    print(r"""
   __________
 /  ꐦ⢸⡇⢸⡇   \
 |   ⢸⡇⢸⡇⢸⡇   |
 \____________/
 /|⢸⡇⢸⡇     |\
૮_|    _ ⢸⡇⢸|_ა 
  \___/ \___/
""")

def spotangry1():
    print(r"""
   __________
 /  ꐦ⢸⡇⢸⡇   \ 
 |   ⢸⡇⢸⡇⢸⡇   |
 \____________/
 /|⢸⡇⢸⡇     |\    ꧂
૮_|    _ ⢸⡇⢸|_ა ꧂
  \___/ \___/
""")
    
def spotangry2():
    print(r"""
   __________
 /  ꐦ⢸⡇⢸⡇   \ 
 |   ⢸⡇⢸⡇⢸⡇   |
 \____________/
 /|⢸⡇⢸⡇     |\        ꧂
૮_|    _ ⢸⡇⢸|_ა   ꧂
  \___/ \___/
""")
    
def spotangry3():
    print(r"""
  __________
 /  ꐦ⢸⡇⢸⡇   \ 
 |   ⢸⡇⢸⡇⢸⡇   |
 \____________/
 /|⢸⡇⢸⡇     |\             ꧂
૮_|    _ ⢸⡇⢸|_ა꧂    ꧂
  \___/ \___/
""")

def spotangry4():
    print(r"""
   __________
 /  ꐦ⢸⡇⢸⡇  \ 
 |   ⢸⡇⢸⡇⢸⡇   |
 \____________/
 /|⢸⡇⢸⡇     |\          ꧂       ꧂
૮_|    _ ⢸⡇⢸|_ა   ꧂    
  \___/ \___/
""")
    
def spotty1():
    for i in range(2):
        spotangry()
        sleep(.3)
        system("clear")
        spotangry1()
        sleep(.3)
        system("clear")
        spotangry2()
        sleep(.3)
        spotangry3()
        system("clear")
        spotangry4()
        system("clear")

def spotblob():
    print(r"""
    /-----\
   /   ⢸⢸  \
  /  ⢸⡇⢸⡇⢸  \       
 |___________|         
""")
    
def spotblob2():
    print(r"""
      __________
    /    ⢸⢸     \
   /    ⢸⡇⢸⡇⢸    \       
  |_______________|         
""")

def spotty2():
    for i in range(2):
        spotblob()
        sleep(.3)
        system("clear")
        spotblob2()
        sleep(.3)
        system("clear")
        spotblob()
        sleep(.3)
        spotblob2()
        system("clear")
        spotblob()
        system("clear")


print(bright_cyan)
player_id = input("Please type in your name.") 
player_gender = input("And a gender (Man/Woman/person).").lower() 
sleep(.5)

print(f"""Player Stats
Name : {player_id}
Gender : {player_gender}
Health : {player_hp}
""")
print(bright_white)

sleep(2)
print("ugh...")
sleep(1.5)
print("What's...")
sleep(1)
print("You wake up in a red cage.")
sleep(1)
print("Everyone watches you")
sleep(1)
print("One")
sleep(.5)
print("By")
sleep(.5)
print("One.")
sleep(.5)
print("Every spider person is watching you from afar.")
sleep(1)
print("tap")
sleep(1)
print("tap") 
sleep(1)
print("tap")
sleep(.5)
print(bright_red)
print("Miguel is now in front of you.")
print(bright_white)

pygame.mixer.music.pause()
pygame.mixer.music.load('spider-man 2099.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.play(-1, fade_ms=0)
pygame.mixer.music.fadeout(5000)

sleep(1)
miguel()
sleep(1)
print(bright_blue)
print(f"You don't belong here {player_id}.")
print(bright_white)

pygame.mixer.music.load('youlikejazz.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.play(-1, fade_ms=0)

questions = [inquirer.List(
    'answer',
    choices = ['Yes I do', 'What?', 'You are right I do not'])]
answers = inquirer.prompt(questions)

if answers["answer"] == "Yes I do":
    sleep(1)
    print("BANG!")
    miggy1()
    print("Miguel hits the cage.. scaring you.")
    miguel()
    sleep(.9)
    print(bright_blue)
    print(f"You do not belong here {player_id}.")
    print(bright_white)
    questions = [inquirer.List(
        'answer',
        choices = ['Shut it!...', 'Stop I do belong here!'])]
    answers = inquirer.prompt(questions)

    if answers["answer"] == "Shut it!...":
        miguel()
        print(bright_blue)
        print(f"You were not supposed to be bitten {player_id}.")
        print(bright_white)
        sleep(1.5)
        miggy1()
        miguelangry()
        print("Miguel rubs his temples.")
        sleep(.9)
        miguelangry()
        print(bright_blue)
        print(f"What is so hard to understand from that {player_id}?!")
        print(bright_white)

        questions = [inquirer.List(
            'answer',
            choices = ['Try breaking out', 'Keep silent'])]
        answers = inquirer.prompt(questions)

        if answers["answer"] == "Try breaking out":
            print("You start to bang on the red cage")
            sleep(1)
            miguel()
            print(bright_blue)
            print("Quiet down... Cállate")
            print(bright_white)
            questions = [inquirer.List(
                'answer',
                choices = ['...'])]
            answers = inquirer.prompt(questions)

            if answers["answer"] == "...":
                sleep(1)
                print("Gwen goes to Miguel")
                gwen()
                sleep(1.5)
                gwen()
                print(bright_magenta)
                print(f"We cant just leave {player_id} here!")
                sleep(1.5)
                miguel()
                print(bright_blue)
                print("Yes we can, we need them to stay here until the canon event ends.")
                sleep(1.5)
                gwen()
                print(bright_white)
                print("Gwen looks at you in guilt.")
                sleep(1.5)
                gwen()
                print(bright_magenta)
                print("I'm sorry Miguel")
                print(bright_white)
                print("BANGG")
                gwen()
                print("Gwen breaks the red cage!")
                gwen()
                print(bright_magenta)
                print(f"Go! {player_id} go!")
                print(bright_white)
                questions = [inquirer.List(
                    'answer',
                    choices = ['Run'])]
                answers = inquirer.prompt(questions)

                if answers["answer"] == "Run":
                    print("You start to run")
                    sleep(1)
                    miguelangry()
                    print(bright_blue)
                    print("CHASE THEM!")
                    print(bright_white)
                    sleep(.5)
                    print("You keep running.")
                    sleep(1)
                    print("Everyone is right behind you.")
                    sleep(1)
                    print("You see a closed room.")
                    questions = [inquirer.List(
                        'action',
                        choices = ['Keep running', 'Hide'])]
                    answers = inquirer.prompt(questions)
        
                    if answers["action"] == "Keep running":
                        print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                        sleep(.5)
                        print("Everyone is right behind you..")
                        print("You see a closed room.")
                        questions = [inquirer.List(
                            'action',
                            choices = ['Hide'])]
                        answers = inquirer.prompt(questions)
        
                        if answers["action"] == "Hide":
                            print("You hid from the crowd.. Seeing each spider person going to another route")
                            sleep(.5)
                            print("You sighed, went into the room.. it looks like a lab")
                            questions = [inquirer.List(
                                'action',
                                choices = ['Search around',])]
                            answers = inquirer.prompt(questions)

                            if answers["action"] == "Search around":
                                print("You start to search the boxes")
                                sleep(.5)
                                print("You see 3 unknown liquids in test tubes, you should drink one.")
                                questions = [inquirer.List(
                                    'drink',
                                    choices = ['Unknown pink liquid', 'Unknown green liquid', 'Unknown purple liquid'])]
                                answers = inquirer.prompt(questions)
                            
                                if answers["drink"] == "Unknown pink liquid":
                                    player_hp = player_hp + 25
                                    sleep(.5)
                                    print(f"{player_id} drinks the pink liquid.. It has cotton candy in it. You gained 25 HP!")

                                elif answers["drink"] == "Unknown green liquid":
                                    player_hp = player_hp + 8
                                    sleep(.5)
                                    print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 8 HP!")

                                elif answers["drink"] == "Unknown purple liquid":
                                    player_hp = player_hp + 19
                                    sleep(.5)
                                    print(f"{player_id} drinks the purple liquid.. Tastes like grape. You gained 19 HP!")
                                    sleep(.8)
                                
                            print("Now.. maybe start searching around more..")
                            questions = [inquirer.List(
                                'action',
                                choices = ['Search around',])]
                            answers = inquirer.prompt(questions)

                            if answers["action"] == "Search around":
                                print("You start to search in one of the boxes")
                                sleep(.5)
                                print("You see a multiverse watch!")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Wear it', 'Throw it on the ground'])]
                                answers = inquirer.prompt(questions)
                
                                if answers["action"] == "Wear it":
                                    print("You wore the watch")
                                    sleep(.5)
                                    print("Boom! A portal opens")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Go inside'])]
                                    answers = inquirer.prompt(questions)
                        
                                    if answers["action"] == "Go inside":
                                        print(yellow)
                                        print("You went in the portal... Going to your own earth now... (Earth-43)")

                                elif answers["action"] == "Throw it on the ground":
                                    print("It breaks.")
                                    print("WWWWWWwwwwwwaaaaaaaaiiiiIIIIIILLLLLl!!")
                                    sleep(.5)
                                    print("The watch starts to alarm!! Uh oh!!")
                                    sleep(.5)
                                    print("Everyone barges in. You run out.")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Keep running', 'Hide'])]
                                    answers = inquirer.prompt(questions)
        
                                    if answers["action"] == "Keep running":
                                        print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                                        sleep(.5)
                                        print("Everyone is right behind you..")
                                        print("You see a closed room.")
                                        questions = [inquirer.List(
                                            'action',
                                            choices = ['Hide'])]
                                        answers = inquirer.prompt(questions)
        
                                        if answers["action"] == "Hide":
                                            print("You hid from the crowd.. Seeing each spider person going to another route")
                                            sleep(.5)
                                            print("In another lab..")
                                            questions = [inquirer.List(
                                                'action',
                                                choices = ['Search around',])]
                                            answers = inquirer.prompt(questions)

                                            if answers["action"] == "Search around":
                                                print("You start to search in one of the boxes")
                                                sleep(.5)
                                                print("You see a multiverse watch!")
                                                questions = [inquirer.List(
                                                    'action',
                                                    choices = ['Wear it'])]
                                                answers = inquirer.prompt(questions)

                                                if answers["action"] == "Wear it":
                                                    print("You wore the watch")
                                                    sleep(.5)
                                                    print("Boom! A portal opens")
                                                    questions = [inquirer.List(
                                                        'action',
                                                        choices = ['Go inside'])]
                                                    answers = inquirer.prompt(questions)

                                                    if answers["action"] == "Go inside":
                                                        print(yellow)
                                                        print("You went in the portal... Going to your own earth now... (Earth-43)")


                    elif answers["action"] == "Hide":
                        print("You hid from the crowd.. Seeing each spider person going to another route")
                        sleep(.5)
                        print("You sighed, went into the room.. it looks like a lab")
                        questions = [inquirer.List(
                                'action',
                                choices = ['Search around',])]
                        answers = inquirer.prompt(questions)

                        if answers["action"] == "Search around":
                                print("You start to search the boxes")
                                sleep(.5)
                                print("You see 3 unknown liquids in test tubes, you should drink one.")
                                questions = [inquirer.List(
                                    'drink',
                                    choices = ['Unknown pink liquid', 'Unknown green liquid', 'Unknown purple liquid'])]
                                answers = inquirer.prompt(questions)

                                if answers["drink"] == "Unknown pink liquid":
                                    player_hp = player_hp + 25
                                    sleep(.5)
                                    print(f"{player_id} drinks the pink liquid.. It has cotton candy in it. You gained 25 HP!")
                                    sleep(.8)
                                    print("Now.. maybe start searching around more..")

                                elif answers["drink"] == "Unknown green liquid":
                                    player_hp = player_hp + 8
                                    sleep(.5)
                                    print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 8 HP!")
                                    sleep(.8)
                                    print("Now.. maybe start searching around more..")

                                elif answers["drink"] == "Unknown purple liquid":
                                    player_hp = player_hp + 19
                                    sleep(.5)
                                    print(f"{player_id} drinks the purple liquid.. Tastes like grape. You gained 19 HP!")
                                    sleep(.8)
                                    print("Now.. maybe start searching around more..")
                            
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Search around',])]
                                answers = inquirer.prompt(questions)

                                if answers["action"] == "Search around":
                                    print("You start to search in one of the boxes")
                                    sleep(.5)
                                    print("You see a multiverse watch!")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Wear it', 'Throw it on the ground'])]
                                    answers = inquirer.prompt(questions)
                
                                    if answers["action"] == "Wear it":
                                        print("You wore the watch")
                                        sleep(.5)
                                        print("Boom! A portal opens")
                                        questions = [inquirer.List(
                                            'action',
                                            choices = ['Go inside'])]
                                        answers = inquirer.prompt(questions)
                        
                                        if answers["action"] == "Go inside":
                                            print(yellow)
                                            print("You went in the portal... Going to your own earth now... (Earth-43)")

                                    elif answers["action"] == "Throw it on the ground":
                                        print("It breaks.")
                                        print("WWWWWWwwwwwwaaaaaaaaiiiiIIIIIILLLLLl!!")
                                        sleep(.5)
                                        print("The watch starts to alarm!! Uh oh!!")
                                        sleep(.5)
                                        print("Everyone barges in. You run out.")
                                        questions = [inquirer.List(
                                            'action',
                                            choices = ['Keep running', 'Hide'])]
                                        answers = inquirer.prompt(questions)
        
                                        if answers["action"] == "Keep running":
                                            print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                                            sleep(.5)
                                            print("Everyone is right behind you..")
                                            print("You see a closed room.")
                                            questions = [inquirer.List(
                                                'action',
                                                choices = ['Hide'])]
                                            answers = inquirer.prompt(questions)
        
                                            if answers["action"] == "Hide":
                                                print("You hid from the crowd.. Seeing each spider person going to another route")
                                                sleep(.5)
                                                print("In another lab..")
                                                questions = [inquirer.List(
                                                    'action',
                                                    choices = ['Search around',])]
                                                answers = inquirer.prompt(questions)

                                                if answers["action"] == "Search around":
                                                    print("You start to search in one of the boxes")
                                                    sleep(.5)
                                                print("You see a multiverse watch!")
                                                questions = [inquirer.List(
                                                    'action',
                                                    choices = ['Wear it'])]
                                                answers = inquirer.prompt(questions)

                                                if answers["action"] == "Wear it":
                                                    print("You wore the watch")
                                                    sleep(.5)
                                                    print("Boom! A portal opens")
                                                    questions = [inquirer.List(
                                                        'action',
                                                        choices = ['Go inside'])]
                                                    answers = inquirer.prompt(questions)

                                                    if answers["action"] == "Go inside":
                                                        print(yellow)
                                                        print("You went in the portal... Going to your own earth now... (Earth-43)")

        elif answers["answer"] == "Keep silent":
            sleep(1)
            print("Gwen goes to Miguel.")
            gwen()
            sleep(1.5)
            gwen()
            print(bright_magenta)
            print(f"We cant just leave {player_id} here!")
            sleep(1.5)
            miguel()
            print(bright_blue)
            print("Yes we can, we need them to stay here until the canon event ends.")
            print(bright_white)
            sleep(1.5)
            gwen()
            print("Gwen looks at you in guilt.")
            sleep(1.5)
            gwen()
            print(bright_magenta)
            print("I'm sorry Miguel")
            print(bright_white)
            print("BANGG")
            print("Gwen breaks the red cage!")
            gwen()
            print(bright_magenta)
            print(f"Go! {player_id} go!")
            print(bright_white)
            questions = [inquirer.List(
                'answer',
                choices = ['Run'])]
            answers = inquirer.prompt(questions)

            if answers["answer"] == "Run":
                print("You start to run")
                sleep(1)
                miguelangry()
                print(bright_blue)
                print("CHASE THEM!")
                print(bright_white)
                sleep(.5)
                print("You keep running.")
                sleep(1)
                print("Everyone is right behind you.")
                sleep(1)
                print("You see a closed room.")
                questions = [inquirer.List(
                    'action',
                    choices = ['Keep running', 'Hide'])]
                answers = inquirer.prompt(questions)
        
                if answers["action"] == "Keep running":
                    print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                    sleep(.5)
                    print("Everyone is right behind you..")
                    print("You see a closed room.")
                    questions = [inquirer.List(
                        'action',
                        choices = ['Hide'])]
                    answers = inquirer.prompt(questions)
        
                    if answers["action"] == "Hide":
                        print("You hid from the crowd.. Seeing each spider person going to another route")
                        sleep(.5)
                        print("You sighed, went into the room.. it looks like a lab")
                        questions = [inquirer.List(
                            'action',
                            choices = ['Search around',])]
                        answers = inquirer.prompt(questions)

                        if answers["action"] == "Search around":
                            print("You start to search the boxes")
                            sleep(.5)
                            print("You see 3 unknown liquids in test tubes, you should drink one.")
                            questions = [inquirer.List(
                                'drink',
                                choices = ['Unknown pink liquid', 'Unknown green liquid', 'Unknown purple liquid'])]
                            answers = inquirer.prompt(questions)
                        
                            if answers["drink"] == "Unknown pink liquid":
                                player_hp = player_hp + 25
                                sleep(.5)
                                print(f"{player_id} drinks the pink liquid.. It has cotton candy in it. You gained 25 HP!")

                            elif answers["drink"] == "Unknown green liquid":
                                player_hp = player_hp + 8
                                sleep(.5)
                                print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 8 HP!")

                            elif answers["drink"] == "Unknown purple liquid":
                                player_hp = player_hp + 19
                                sleep(.5)
                                print(f"{player_id} drinks the purple liquid.. Tastes like grape. You gained 19 HP!")
                                sleep(.8)
                                
                            print("Now.. maybe start searching around more..")
                            questions = [inquirer.List(
                                'action',
                                choices = ['Search around',])]
                            answers = inquirer.prompt(questions)

                            if answers["action"] == "Search around":
                                print("You start to search in one of the boxes")
                                sleep(.5)
                                print("You see a multiverse watch!")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Wear it', 'Throw it on the ground'])]
                                answers = inquirer.prompt(questions)
                
                                if answers["action"] == "Wear it":
                                    print("You wore the watch")
                                    sleep(.5)
                                    print("Boom! A portal opens")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Go inside'])]
                                    answers = inquirer.prompt(questions)
                        
                                    if answers["action"] == "Go inside":
                                        print(yellow)
                                        print("You went in the portal... Going to your own earth now... (Earth-43)")

                                elif answers["action"] == "Throw it on the ground":
                                    print("It breaks.")
                                    print("WWWWWWwwwwwwaaaaaaaaiiiiIIIIIILLLLLl!!")
                                    sleep(.5)
                                    print("The watch starts to alarm!! Uh oh!!")
                                    sleep(.5)
                                    print("Everyone barges in. You run out.")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Keep running', 'Hide'])]
                                    answers = inquirer.prompt(questions)
        
                                    if answers["action"] == "Keep running":
                                        print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                                        sleep(.5)
                                        print("Everyone is right behind you..")
                                        print("You see a closed room.")
                                        questions = [inquirer.List(
                                            'action',
                                            choices = ['Hide'])]
                                        answers = inquirer.prompt(questions)
        
                                        if answers["action"] == "Hide":
                                            print("You hid from the crowd.. Seeing each spider person going to another route")
                                            sleep(.5)
                                            print("In another lab..")
                                            questions = [inquirer.List(
                                                'action',
                                                choices = ['Search around',])]
                                            answers = inquirer.prompt(questions)

                                            if answers["action"] == "Search around":
                                                print("You start to search in one of the boxes")
                                                sleep(.5)
                                                print("You see a multiverse watch!")
                                            questions = [inquirer.List(
                                                'action',
                                                choices = ['Wear it'])]
                                            answers = inquirer.prompt(questions)

                                            if answers["action"] == "Wear it":
                                                print("You wore the watch")
                                                sleep(.5)
                                                print("Boom! A portal opens")
                                                questions = [inquirer.List(
                                                    'action',
                                                    choices = ['Go inside'])]
                                                answers = inquirer.prompt(questions)

                                                if answers["action"] == "Go inside":
                                                    print(yellow)
                                                    print("You went in the portal... Going to your own earth now... (Earth-43)")


                elif answers["action"] == "Hide":
                    print("You hid from the crowd.. Seeing each spider person going to another route")
                    sleep(.5)
                    print("You sighed, went into the room.. it looks like a lab")
                    questions = [inquirer.List(
                        'action',
                        choices = ['Search around',])]
                    answers = inquirer.prompt(questions)

                    if answers["action"] == "Search around":
                        print("You start to search the boxes")
                        sleep(.5)
                        print("You see 3 unknown liquids in test tubes, you should drink one.")
                        questions = [inquirer.List(
                            'drink',
                            choices = ['Unknown pink liquid', 'Unknown green liquid', 'Unknown purple liquid'])]
                        answers = inquirer.prompt(questions)

                        if answers["drink"] == "Unknown pink liquid":
                            player_hp = player_hp + 25
                            sleep(.5)
                            print(f"{player_id} drinks the pink liquid.. It has cotton candy in it. You gained 25 HP!")
                            sleep(.8)

                        elif answers["drink"] == "Unknown green liquid":
                            player_hp = player_hp + 8
                            sleep(.5)
                            print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 8 HP!")
                            sleep(.8)

                        elif answers["drink"] == "Unknown purple liquid":
                            player_hp = player_hp + 19
                            sleep(.5)
                            print(f"{player_id} drinks the purple liquid.. Tastes like grape. You gained 19 HP!")
                            sleep(.8)
                            
                        print("Now.. maybe start searching around more..")
                        questions = [inquirer.List(
                            'action',
                            choices = ['Search around',])]
                        answers = inquirer.prompt(questions)

                        if answers["action"] == "Search around":
                            print("You start to search in one of the boxes")
                            sleep(.5)
                            print("You see a multiverse watch!")
                            questions = [inquirer.List(
                                'action',
                                choices = ['Wear it', 'Throw it on the ground'])]
                            answers = inquirer.prompt(questions)
                
                            if answers["action"] == "Wear it":
                                print("You wore the watch")
                                sleep(.5)
                                print("Boom! A portal opens")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Go inside'])]
                                answers = inquirer.prompt(questions)
                        
                                if answers["action"] == "Go inside":
                                    print(yellow)
                                    print("You went in the portal... Going to your own earth now... (Earth-43)")

                            elif answers["action"] == "Throw it on the ground":
                                print("It breaks.")
                                print("WWWWWWwwwwwwaaaaaaaaiiiiIIIIIILLLLLl!!")
                                sleep(.5)
                                print("The watch starts to alarm!! Uh oh!!")
                                sleep(.5)
                                print("Everyone barges in. You run out.")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Keep running', 'Hide'])]
                                answers = inquirer.prompt(questions)
        
                                if answers["action"] == "Keep running":
                                    print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                                    sleep(.5)
                                    print("Everyone is right behind you..")
                                    print("You see a closed room.")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Hide'])]
                                    answers = inquirer.prompt(questions)
        
                                    if answers["action"] == "Hide":
                                        print("You hid from the crowd.. Seeing each spider person going to another route")
                                        sleep(.5)
                                        print("In another lab..")
                                        questions = [inquirer.List(
                                            'action',
                                            choices = ['Search around',])]
                                        answers = inquirer.prompt(questions)

                                        if answers["action"] == "Search around":
                                            print("You start to search in one of the boxes")
                                            sleep(.5)
                                            print("You see a multiverse watch!")
                                            questions = [inquirer.List(
                                                'action',
                                                choices = ['Wear it'])]
                                            answers = inquirer.prompt(questions)

                                            if answers["action"] == "Wear it":
                                                print("You wore the watch")
                                                sleep(.5)
                                                print("Boom! A portal opens")
                                                questions = [inquirer.List(
                                                    'action',
                                                    choices = ['Go inside'])]
                                                answers = inquirer.prompt(questions)

                                                if answers["action"] == "Go inside":
                                                    print(yellow)
                                                    print("You went in the portal... Going to your own earth now... (Earth-43)")


    elif answers["answer"] == "Stop I do belong here!":
        miguel()
        print(bright_blue)
        print(f"You were not supposed to be bitten {player_id}.")
        print(bright_white)
        print("Miguel rubs his nose bridge.")
        sleep(.9)
        miguelangry()
        print(bright_blue)
        print(f"What is so hard to understand from that {player_id}?!")
        print(bright_white)
        questions = [inquirer.List(
            'answer',
            choices = ['Try breaking out', 'Keep silent'])]
        answers = inquirer.prompt(questions)

        if answers["answer"] == "Try breaking out":
            print("You start to bang on the red cage")
            sleep(1)
            miguel()
            print(bright_blue)
            print("Quiet down... Cállate")
            print(bright_white)
            questions = [inquirer.List(
                'answer',
                choices = ['...'])]
            answers = inquirer.prompt(questions)

            if answers["answer"] == "...":
                sleep(1)
                print("Gwen goes to Miguel")
                gwen()
                sleep(1.5)
                print(bright_magenta)
                print(f"We cant just leave {player_id} here!")
                sleep(1.5)
                miguel()
                print(bright_blue)
                print("Yes we can, we need them to stay here until the canon event ends.")
                print(bright_white)
                sleep(1)
                gwen()
                print("Gwen looks at you in guilt.")
                sleep(1.5)
                gwen()
                print(bright_magenta)
                print("I'm sorry Miguel")
                print(bright_white)
                print("BANGG")
                print("Gwen breaks the red cage!")
                gwen()
                print(bright_magenta)
                print(f"Go! {player_id} go!")
                print(bright_white)
                questions = [inquirer.List(
                   'answer',
                    choices = ['Run'])]
                answers = inquirer.prompt(questions)

                if answers["answer"] == "Run":
                    print("You start to run")
                    sleep(1)
                    miguelangry()
                    print(bright_blue)
                    print("CHASE THEM!")
                    print(bright_white)
                    sleep(.5)
                    print("You keep running.")
                    sleep(1)
                    print("Everyone is right behind you.")
                    sleep(1)
                    print("You see a closed room.")

                questions = [inquirer.List(
                        'action',
                        choices = ['Keep running', 'Hide'])]
                answers = inquirer.prompt(questions)
        
                if answers["action"] == "Keep running":
                    print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                    sleep(.5)
                    print("Everyone is right behind you..")
                    print("You see a closed room.")
                    questions = [inquirer.List(
                        'action',
                        choices = ['Hide'])]
                    answers = inquirer.prompt(questions)
        
                    if answers["action"] == "Hide":
                        print("You hid from the crowd.. Seeing each spider person going to another route")
                        sleep(.5)
                        print("You sighed, went into the room.. it looks like a lab")
                        questions = [inquirer.List(
                            'action',
                            choices = ['Search around',])]
                        answers = inquirer.prompt(questions)

                        if answers["action"] == "Search around":
                            print("You start to search the boxes")
                            sleep(.5)
                            print("You see 3 unknown liquids in test tubes, you should drink one.")
                            questions = [inquirer.List(
                                'drink',
                                choices = ['Unknown pink liquid', 'Unknown green liquid', 'Unknown purple liquid'])]
                            answers = inquirer.prompt(questions)
                        
                            if answers["drink"] == "Unknown pink liquid":
                                player_hp = player_hp + 25
                                sleep(.5)
                                print(f"{player_id} drinks the pink liquid.. It has cotton candy in it. You gained 25 HP!")

                            elif answers["drink"] == "Unknown green liquid":
                                player_hp = player_hp + 8
                                sleep(.5)
                                print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 8 HP!")

                            elif answers["drink"] == "Unknown purple liquid":
                                player_hp = player_hp + 19
                                sleep(.5)
                                print(f"{player_id} drinks the purple liquid.. Tastes like grape. You gained 19 HP!")
                                sleep(.8)
                                
                            print("Now.. maybe start searching around more..")
                            questions = [inquirer.List(
                                'action',
                                choices = ['Search around',])]
                            answers = inquirer.prompt(questions)

                            if answers["action"] == "Search around":
                                print("You start to search in one of the boxes")
                                sleep(.5)
                                print("You see a multiverse watch!")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Wear it', 'Throw it on the ground'])]
                                answers = inquirer.prompt(questions)
                
                                if answers["action"] == "Wear it":
                                    print("You wore the watch")
                                    sleep(.5)
                                    print("Boom! A portal opens")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Go inside'])]
                                    answers = inquirer.prompt(questions)
                        
                                    if answers["action"] == "Go inside":
                                        print(yellow)
                                        print("You went in the portal... Going to your own earth now... (Earth-43)")

                                elif answers["action"] == "Throw it on the ground":
                                    print("It breaks.")
                                    print("WWWWWWwwwwwwaaaaaaaaiiiiIIIIIILLLLLl!!")
                                    sleep(.5)
                                    print("The watch starts to alarm!! Uh oh!!")
                                    sleep(.5)
                                    print("Everyone barges in. You run out.")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Keep running', 'Hide'])]
                                    answers = inquirer.prompt(questions)

                                    if answers["action"] == "Keep running":
                                        print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                                        sleep(.5)
                                        print("Everyone is right behind you..")
                                        print("You see a closed room.")
                                        questions = [inquirer.List(
                                            'action',
                                            choices = ['Hide'])]
                                        answers = inquirer.prompt(questions)
        
                                        if answers["action"] == "Hide":
                                            print("You hid from the crowd.. Seeing each spider person going to another route")
                                            sleep(.5)
                                            print("In another lab..")
                                            questions = [inquirer.List(
                                                'action',
                                                choices = ['Search around',])]
                                            answers = inquirer.prompt(questions)

                                            if answers["action"] == "Search around":
                                                print("You start to search in one of the boxes")
                                                sleep(.5)
                                                print("You see a multiverse watch!")
                                                questions = [inquirer.List(
                                                    'action',
                                                    choices = ['Wear it'])]
                                                answers = inquirer.prompt(questions)

                                                if answers["action"] == "Wear it":
                                                    print("You wore the watch")
                                                    sleep(.5)
                                                    print("Boom! A portal opens")
                                                    questions = [inquirer.List(
                                                        'action',
                                                        choices = ['Go inside'])]
                                                    answers = inquirer.prompt(questions)

                                                    if answers["action"] == "Go inside":
                                                        print(yellow)
                                                        print("You went in the portal... Going to your own earth now... (Earth-43)")


                elif answers["action"] == "Hide":
                    print("You hid from the crowd.. Seeing each spider person going to another route")
                    sleep(.5)
                    print("You sighed, went into the room.. it looks like a lab")
                    questions = [inquirer.List(
                        'action',
                        choices = ['Search around',])]
                answers = inquirer.prompt(questions)

                if answers["action"] == "Search around":
                    print("You start to search the boxes")
                    sleep(.5)
                    print("You see 3 unknown liquids in test tubes, you should drink one.")
                    questions = [inquirer.List(
                        'drink',
                        choices = ['Unknown pink liquid', 'Unknown green liquid', 'Unknown purple liquid'])]
                    answers = inquirer.prompt(questions)

                    if answers["drink"] == "Unknown pink liquid":
                        player_hp = player_hp + 25
                        sleep(.5)
                        print(f"{player_id} drinks the pink liquid.. It has cotton candy in it. You gained 25 HP!")
                        sleep(.8)

                    elif answers["drink"] == "Unknown green liquid":
                        player_hp = player_hp + 8
                        sleep(.5)
                        print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 8 HP!")
                        sleep(.8)

                    elif answers["drink"] == "Unknown purple liquid":
                        player_hp = player_hp + 19
                        sleep(.5)
                        print(f"{player_id} drinks the purple liquid.. Tastes like grape. You gained 19 HP!")
                        sleep(.8)
                            
                    print("Now.. maybe start searching around more..")
                    questions = [inquirer.List(
                        'action',
                        choices = ['Search around',])]
                    answers = inquirer.prompt(questions)

                    if answers["action"] == "Search around":
                        print("You start to search in one of the boxes")
                        sleep(.5)
                        print("You see a multiverse watch!")
                        questions = [inquirer.List(
                            'action',
                            choices = ['Wear it', 'Throw it on the ground'])]
                        answers = inquirer.prompt(questions)
                
                        if answers["action"] == "Wear it":
                            print("You wore the watch")
                            sleep(.5)
                            print("Boom! A portal opens")
                            questions = [inquirer.List(
                                'action',
                                choices = ['Go inside'])]
                            answers = inquirer.prompt(questions)
                        
                            if answers["action"] == "Go inside":
                                print(yellow)
                                print("You went in the portal... Going to your own earth now... (Earth-43)")

                        elif answers["action"] == "Throw it on the ground":
                            print("It breaks.")
                            print("WWWWWWwwwwwwaaaaaaaaiiiiIIIIIILLLLLl!!")
                            sleep(.5)
                            print("The watch starts to alarm!! Uh oh!!")
                            sleep(.5)
                            print("Everyone barges in. You run out.")
                            questions = [inquirer.List(
                                'action',
                                choices = ['Keep running', 'Hide'])]
                            answers = inquirer.prompt(questions)

                            if answers["action"] == "Keep running":
                                print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                                sleep(.5)
                                print("Everyone is right behind you..")
                                print("You see a closed room.")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Hide'])]
                                answers = inquirer.prompt(questions)
    
                                if answers["action"] == "Hide":
                                    print("You hid from the crowd.. Seeing each spider person going to another route")
                                    sleep(.5)
                                    print("In another lab..")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Search around',])]
                                    answers = inquirer.prompt(questions)

                                    if answers["action"] == "Search around":
                                        print("You start to search in one of the boxes")
                                        sleep(.5)
                                        print("You see a multiverse watch!")
                                        questions = [inquirer.List(
                                            'action',
                                            choices = ['Wear it'])]
                                        answers = inquirer.prompt(questions)

                                        if answers["action"] == "Wear it":
                                            print("You wore the watch")
                                            sleep(.5)
                                            print("Boom! A portal opens")
                                            questions = [inquirer.List(
                                                'action',
                                                choices = ['Go inside'])]
                                            answers = inquirer.prompt(questions)

                                            if answers["action"] == "Go inside":
                                                print(yellow)
                                                print("You went in the portal... Going to your own earth now... (Earth-43)")

        elif answers["answer"] == "Keep silent":
            sleep(1)
            gwen()
            print("Gwen goes to Miguel.")
            sleep(1.5)
            gwen()
            print(bright_magenta)
            print(f"We cant just leave {player_id} here!")
            sleep(1.5)
            miguel()
            print(bright_blue)
            print("Yes we can, we need them to stay here until the canon event ends.")
            print(bright_white)
            sleep(1.5)
            gwen()
            print("Gwen looks at you in guilt.")
            sleep(1.5)
            gwen()
            print(bright_magenta)
            print("I'm sorry Miguel")
            print(bright_white)
            print("BANGG")
            print("Gwen breaks the red cage!")
            gwen()
            print(bright_magenta)
            print(f"Go! {player_id} go!")
            print(bright_white)
            questions = [inquirer.List(
                'answer',
                choices = ['Run'])]
            answers = inquirer.prompt(questions)

            if answers["answer"] == "Run":
                print("You start to run")
                sleep(1)
                miguelangry()
                print(bright_blue)
                print("CHASE THEM!")
                print(bright_white)
                sleep(.5)
                print("You keep running.")
                sleep(1)
                print("Everyone is right behind you.")
                sleep(1)
                print("You see a closed room.")
                questions = [inquirer.List(
                    'action',
                    choices = ['Keep running', 'Hide'])]
                answers = inquirer.prompt(questions)
        
                if answers["action"] == "Keep running":
                    print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                    sleep(.5)
                    print("Everyone is right behind you..")
                    print("You see a closed room.")
                    questions = [inquirer.List(
                        'action',
                        choices = ['Hide'])]
                    answers = inquirer.prompt(questions)
        
                    if answers["action"] == "Hide":
                        print("You hid from the crowd.. Seeing each spider person going to another route")
                        sleep(.5)
                        print("You sighed, went into the room.. it looks like a lab")
                        questions = [inquirer.List(
                            'action',
                            choices = ['Search around',])]
                        answers = inquirer.prompt(questions)

                        if answers["action"] == "Search around":
                            print("You start to search the boxes")
                            sleep(.5)
                            print("You see 3 unknown liquids in test tubes, you should drink one.")
                            questions = [inquirer.List(
                                'drink',
                                choices = ['Unknown pink liquid', 'Unknown green liquid', 'Unknown purple liquid'])]
                            answers = inquirer.prompt(questions)
                        
                            if answers["drink"] == "Unknown pink liquid":
                                player_hp = player_hp + 25
                                sleep(.5)
                                print(f"{player_id} drinks the pink liquid.. It has cotton candy in it. You gained 25 HP!")

                            elif answers["weapon"] == "Unknown green liquid":
                                player_hp = player_hp + 8
                                sleep(.5)
                                print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 8 HP!")

                            elif answers["weapon"] == "Unknown purple liquid":
                                player_hp = player_hp + 19
                                sleep(.5)
                                print(f"{player_id} drinks the purple liquid.. Tastes like grape. You gained 19 HP!")
                                sleep(.8)
                                
                            print("Now.. maybe start searching around more..")
                            questions = [inquirer.List(
                                'action',
                                choices = ['Search around',])]
                            answers = inquirer.prompt(questions)

                            if answers["action"] == "Search around":
                                print("You start to search in one of the boxes")
                                sleep(.5)
                                print("You see a multiverse watch!")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Wear it', 'Throw it on the ground'])]
                                answers = inquirer.prompt(questions)
                
                                if answers["action"] == "Wear it":
                                    print("You wore the watch")
                                    sleep(.5)
                                    print("Boom! A portal opens")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Go inside'])]
                                    answers = inquirer.prompt(questions)
                        
                                    if answers["action"] == "Go inside":
                                        print(yellow)
                                        print("You went in the portal... Going to your own earth now... (Earth-43)")

                                elif answers["action"] == "Throw it on the ground":
                                    print("It breaks.")
                                    print("WWWWWWwwwwwwaaaaaaaaiiiiIIIIIILLLLLl!!")
                                    sleep(.5)
                                    print("The watch starts to alarm!! Uh oh!!")
                                    sleep(.5)
                                    print("Everyone barges in. You run out.")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Keep running', 'Hide'])]
                                    answers = inquirer.prompt(questions)
        
                                    if answers["action"] == "Keep running":
                                        print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                                        sleep(.5)
                                        print("Everyone is right behind you..")
                                        print("You see a closed room.")
                                        questions = [inquirer.List(
                                            'action',
                                            choices = ['Hide'])]
                                        answers = inquirer.prompt(questions)
        
                                        if answers["action"] == "Hide":
                                            print("You hid from the crowd.. Seeing each spider person going to another route")
                                            sleep(.5)
                                            print("In another lab..")
                                            questions = [inquirer.List(
                                                'action',
                                                choices = ['Search around',])]
                                            answers = inquirer.prompt(questions)

                                            if answers["action"] == "Search around":
                                                print("You start to search in one of the boxes")
                                                sleep(.5)
                                                print("You see a multiverse watch!")
                                                questions = [inquirer.List(
                                                    'action',
                                                    choices = ['Wear it'])]
                                                answers = inquirer.prompt(questions)

                                                if answers["action"] == "Wear it":
                                                    print("You wore the watch")
                                                    sleep(.5)
                                                    print("Boom! A portal opens")
                                                    questions = [inquirer.List(
                                                        'action',
                                                        choices = ['Go inside'])]
                                                    answers = inquirer.prompt(questions)

                                                    if answers["action"] == "Go inside":
                                                        print(yellow)
                                                        print("You went in the portal... Going to your own earth now... (Earth-43)")


                elif answers["action"] == "Hide":
                    print("You hid from the crowd.. Seeing each spider person going to another route")
                    sleep(.5)
                    print("You sighed, went into the room.. it looks like a lab")
                    questions = [inquirer.List(
                        'action',
                        choices = ['Search around',])]
                    answers = inquirer.prompt(questions)

                    if answers["action"] == "Search around":
                        print("You start to search the boxes")
                        sleep(.5)
                        print("You see 3 unknown liquids in test tubes, you should drink one.")
                        questions = [inquirer.List(
                            'drink',
                            choices = ['Unknown pink liquid', 'Unknown green liquid', 'Unknown purple liquid'])]
                        answers = inquirer.prompt(questions)

                        if answers["drink"] == "Unknown pink liquid":
                            player_hp = player_hp + 25
                            sleep(.5)
                            print(f"{player_id} drinks the pink liquid.. It has cotton candy in it. You gained 25 HP!")
                            sleep(.8)

                        elif answers["drink"] == "Unknown green liquid":
                            player_hp = player_hp + 8
                            sleep(.5)
                            print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 8 HP!")
                            sleep(.8)

                        elif answers["drink"] == "Unknown purple liquid":
                            player_hp = player_hp + 19
                            sleep(.5)
                            print(f"{player_id} drinks the purple liquid.. Tastes like grape. You gained 19 HP!")
                            sleep(.8)
                        
                        print("Now.. maybe start searching around more..")
                        questions = [inquirer.List(
                            'action',
                            choices = ['Search around',])]
                        answers = inquirer.prompt(questions)

                        if answers["action"] == "Search around":
                            print("You start to search in one of the boxes")
                            sleep(.5)
                            print("You see a multiverse watch!")
                            questions = [inquirer.List(
                                'action',
                                choices = ['Wear it', 'Throw it on the ground'])]
                            answers = inquirer.prompt(questions)
            
                            if answers["action"] == "Wear it":
                                print("You wore the watch")
                                sleep(.5)
                                print("Boom! A portal opens")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Go inside'])]
                                answers = inquirer.prompt(questions)
                    
                                if answers["action"] == "Go inside":
                                    print(yellow)
                                    print("You went in the portal... Going to your own earth now... (Earth-43)")

                            elif answers["action"] == "Throw it on the ground":
                                print("It breaks.")
                                print("WWWWWWwwwwwwaaaaaaaaiiiiIIIIIILLLLLl!!")
                                sleep(.5)
                                print("The watch starts to alarm!! Uh oh!!")
                                sleep(.5)
                                print("Everyone barges in. You run out.")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Keep running', 'Hide'])]
                                answers = inquirer.prompt(questions)

                                if answers["action"] == "Keep running": 
                                    print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                                    sleep(.5)
                                    print("Everyone is right behind you..")
                                    print("You see a closed room.")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Hide'])]
                                    answers = inquirer.prompt(questions)
        
                                    if answers["action"] == "Hide":
                                        print("You hid from the crowd.. Seeing each spider person going to another route")
                                        sleep(.5)
                                        print("In another lab..")
                                        questions = [inquirer.List(
                                            'action',
                                            choices = ['Search around',])]
                                        answers = inquirer.prompt(questions)

                                        if answers["action"] == "Search around":
                                            print("You start to search in one of the boxes")
                                            sleep(.5)
                                            print("You see a multiverse watch!")
                                            questions = [inquirer.List(
                                                'action',
                                                choices = ['Wear it'])]
                                            answers = inquirer.prompt(questions)

                                            if answers["action"] == "Wear it":
                                                print("You wore the watch")
                                                sleep(.5)
                                                print("Boom! A portal opens")
                                                questions = [inquirer.List(
                                                    'action',
                                                    choices = ['Go inside'])]
                                                answers = inquirer.prompt(questions)

                                                if answers["action"] == "Go inside":
                                                    print(yellow)
                                                    print("You went in the portal... Going to your own earth now... (Earth-43)")



elif answers["answer"] == "What?":
    miguel()
    print(bright_blue)
    print(f"You never were supposed to be a spider{player_gender}")
    sleep(.9)
    print("You're an anomaly.")
    print(bright_white)
    questions = [inquirer.List(
        'answer',
        choices = ['What is an anomaly?'])]
    answers = inquirer.prompt(questions)

    if answers["answer"] == "What is an anomaly?":
        miguelangry()
        print(bright_blue)
        print("It means, you are not some normal spiderman, YOU were not supposed to get bitten!.")
        print(bright_white)
        print("Miguel rubs his temples.")
        sleep(.9)
        miguel()
        print(bright_blue)
        print(f"What is so hard to understand from that {player_id}?!")
        print(bright_white)
        questions = [inquirer.List(
            'answer',
            choices = ['...'])]
        answers = inquirer.prompt(questions)

        if answers["answer"] == "...":
            sleep(1)
            gwen()
            print("Gwen goes to Miguel")
            sleep(1.5)
            gwen()
            print(bright_magenta)
            print(f"We cant just leave {player_id} here!")
            sleep(1.5)
            miguel()
            print(bright_blue)
            print("Yes we can, we need them to stay here until the canon event ends.")
            print(bright_white)
            sleep(1.5)
            gwen()
            print("Gwen looks at you in guilt.")
            sleep(1.5)
            gwen()
            print(bright_magenta)
            print("I'm sorry Miguel")
            print(bright_white)
            print("BANGG")
            print("Gwen breaks the red cage!")
            gwen()
            print(bright_magenta)
            print(f"Go! {player_id} go!")
            questions = [inquirer.List(
                'answer',
                choices = ['Run'])]
            answers = inquirer.prompt(questions)

            if answers["answer"] == "Run":
                print("You start to run")
                sleep(1)
                miguelangry()
                print(bright_blue)
                print("CHASE THEM!")
                print(bright_white)
                sleep(.5)
                print("You keep running.")
                sleep(1)
                print("Everyone is right behind you.")
                sleep(1)
                print("You see a closed room.")
                questions = [inquirer.List(
                    'action',
                    choices = ['Keep running', 'Hide'])]
                answers = inquirer.prompt(questions)
        
                if answers["action"] == "Keep running":
                    print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                    sleep(.5)
                    print("Everyone is right behind you..")
                    print("You see a closed room.")
                    questions = [inquirer.List(
                        'action',
                        choices = ['Hide'])]
                    answers = inquirer.prompt(questions)
        
                    if answers["action"] == "Hide":
                        print("You hid from the crowd.. Seeing each spider person going to another route")
                        sleep(.5)
                        print("You sighed, went into the room.. it looks like a lab")
                        questions = [inquirer.List(
                            'action',
                            choices = ['Search around',])]
                        answers = inquirer.prompt(questions)

                        if answers["action"] == "Search around":
                            print("You start to search the boxes")
                            sleep(.5)
                            print("You see 3 unknown liquids in test tubes, you should drink one.")
                            questions = [inquirer.List(
                                'drink',
                                choices = ['Unknown pink liquid', 'Unknown green liquid', 'Unknown purple liquid'])]
                            answers = inquirer.prompt(questions)
                        
                            if answers["drink"] == "Unknown pink liquid":
                                player_hp = player_hp + 25
                                sleep(.5)
                                print(f"{player_id} drinks the pink liquid.. It has cotton candy in it. You gained 25 HP!")

                            elif answers["drink"] == "Unknown green liquid":
                                player_hp = player_hp + 8
                                sleep(.5)
                                print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 8 HP!")

                            elif answers["drink"] == "Unknown purple liquid":
                                player_hp = player_hp + 19
                                sleep(.5)
                                print(f"{player_id} drinks the purple liquid.. Tastes like grape. You gained 19 HP!")
                                sleep(.8)
                                
                            print("Now.. maybe start searching around more..")
                            questions = [inquirer.List(
                                'action',
                                choices = ['Search around',])]
                            answers = inquirer.prompt(questions)

                            if answers["action"] == "Search around":
                                print("You start to search in one of the boxes")
                                sleep(.5)
                                print("You see a multiverse watch!")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Wear it', 'Throw it on the ground'])]
                                answers = inquirer.prompt(questions)
                
                                if answers["action"] == "Wear it":
                                    print("You wore the watch")
                                    sleep(.5)
                                    print("Boom! A portal opens")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Go inside'])]
                                    answers = inquirer.prompt(questions)

                                    if answers["action"] == "Go inside":
                                        print(yellow)
                                        print("You went in the portal... Going to your own earth now... (Earth-43)")

                                elif answers["action"] == "Throw it on the ground":
                                    print("It breaks.")
                                    print("WWWWWWwwwwwwaaaaaaaaiiiiIIIIIILLLLLl!!")
                                    sleep(.5)
                                    print("The watch starts to alarm!! Uh oh!!")
                                    sleep(.5)
                                    print("Everyone barges in. You run out.")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Keep running'])]
                                    answers = inquirer.prompt(questions)
        
                                    if answers["action"] == "Keep running":
                                        print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                                        sleep(.5)
                                        print("Everyone is right behind you..")
                                        print("You see a closed room.")
                                        questions = [inquirer.List(
                                            'action',
                                            choices = ['Hide'])]
                                        answers = inquirer.prompt(questions)
        
                                        if answers["action"] == "Hide":
                                            print("You hid from the crowd.. Seeing each spider person going to another route")
                                            sleep(.5)
                                            print("In another lab..")
                                            questions = [inquirer.List(
                                                'action',
                                                choices = ['Search around',])]
                                            answers = inquirer.prompt(questions)

                                            if answers["action"] == "Search around":
                                                print("You start to search in one of the boxes")
                                                sleep(.5)
                                                print("You see a multiverse watch!")
                                                questions = [inquirer.List(
                                                    'action',
                                                    choices = ['Wear it'])]
                                                answers = inquirer.prompt(questions)

                                                if answers["action"] == "Wear it":
                                                    print("You wore the watch")
                                                    sleep(.5)
                                                    print("Boom! A portal opens")
                                                    questions = [inquirer.List(
                                                        'action',
                                                        choices = ['Go inside'])]
                                                    answers = inquirer.prompt(questions)

                                                    if answers["action"] == "Go inside":
                                                        print(yellow)
                                                        print("You went in the portal... Going to your own earth now... (Earth-43)")


                elif answers["action"] == "Hide":
                    print("You hid from the crowd.. Seeing each spider person going to another route")
                    sleep(.5)
                    print("You sighed, went into the room.. it looks like a lab")
                    questions = [inquirer.List(
                        'action',
                        choices = ['Search around',])]
                    answers = inquirer.prompt(questions)

                    if answers["action"] == "Search around":
                        print("You start to search the boxes")
                        sleep(.5)
                        print("You see 3 unknown liquids in test tubes, you should drink one.")
                        questions = [inquirer.List(
                            'drink',
                            choices = ['Unknown pink liquid', 'Unknown green liquid', 'Unknown purple liquid'])]
                        answers = inquirer.prompt(questions)

                        if answers["drink"] == "Unknown pink liquid":
                            player_hp = player_hp + 25
                            sleep(.5)
                            print(f"{player_id} drinks the pink liquid.. It has cotton candy in it. You gained 25 HP!")
                            sleep(.8)

                        elif answers["drink"] == "Unknown green liquid":
                            player_hp = player_hp + 8
                            sleep(.5)
                            print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 8 HP!")
                            sleep(.8)

                        elif answers["drink"] == "Unknown purple liquid":
                            player_hp = player_hp + 19
                            sleep(.5)
                            print(f"{player_id} drinks the purple liquid.. Tastes like grape. You gained 19 HP!")
                            sleep(.8)
                            
                        print("Now.. maybe start searching around more..")
                        questions = [inquirer.List(
                            'action',
                            choices = ['Search around',])]
                        answers = inquirer.prompt(questions)

                        if answers["action"] == "Search around":
                            print("You start to search in one of the boxes")
                            sleep(.5)
                            print("You see a multiverse watch!")
                            questions = [inquirer.List(
                                'action',
                                choices = ['Wear it', 'Throw it on the ground'])]
                            answers = inquirer.prompt(questions)
                
                            if answers["action"] == "Wear it":
                                print("You wore the watch")
                                sleep(.5)
                                print("Boom! A portal opens")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Go inside'])]
                                answers = inquirer.prompt(questions)
                        
                                if answers["action"] == "Go inside":
                                    print(yellow)
                                    print("You went in the portal... Going to your own earth now... (Earth-43)")

                            elif answers["action"] == "Throw it on the ground":
                                print("It breaks.")
                                print("WWWWWWwwwwwwaaaaaaaaiiiiIIIIIILLLLLl!!")
                                sleep(.5)
                                print("The watch starts to alarm!! Uh oh!!")
                                sleep(.5)
                                print("Everyone barges in. You run out.")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Keep running', 'Hide'])]
                                answers = inquirer.prompt(questions)
    
                                if answers["action"] == "Keep running":
                                    print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                                    sleep(.5)
                                    print("Everyone is right behind you..")
                                    print("You see a closed room.")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Hide'])]
                                    answers = inquirer.prompt(questions)
        
                                    if answers["action"] == "Hide":
                                        print("You hid from the crowd.. Seeing each spider person going to another route")
                                        sleep(.5)
                                        print("In another lab..")
                                        questions = [inquirer.List(
                                            'action',
                                            choices = ['Search around',])]
                                        answers = inquirer.prompt(questions)

                                        if answers["action"] == "Search around":
                                            print("You start to search in one of the boxes")
                                            sleep(.5)
                                            print("You see a multiverse watch!")
                                            questions = [inquirer.List(
                                                'action',
                                                choices = ['Wear it'])]
                                            answers = inquirer.prompt(questions)

                                            if answers["action"] == "Wear it":
                                                print("You wore the watch")
                                                sleep(.5)
                                                print("Boom! A portal opens")
                                                questions = [inquirer.List(
                                                    'action',
                                                    choices = ['Go inside'])]
                                                answers = inquirer.prompt(questions)

                                                if answers["action"] == "Go inside":
                                                    print(yellow)
                                                    print("You went in the portal... Going to your own earth now... (Earth-43)")




elif answers["answer"] == "You are right I do not":
    miguel()
    print(bright_blue)
    print("Thank you! You actually agree on something I said!")
    sleep(1)
    miguel()
    print(f"{player_id}, you still have to stay here for 2 days until your dad dies.")
    print(bright_white)
    questions = [inquirer.List(
            'answer',
            choices = ['You are crazy!', 'I am NOT staying here!'])]
    answers = inquirer.prompt(questions)

    if answers["answer"] == "You are crazy!":
        miguel()
        print(bright_blue)
        print("It's for your own good.")
        print(bright_white)
        print("Miguel rubs his temples.")
        sleep(.9)
        miguel()
        print(bright_blue)
        print(f"This is your canon event, {player_id}.")
        print(bright_white)
        questions = [inquirer.List(
            'answer',
            choices = ['...'])]
        answers = inquirer.prompt(questions)

        if answers["answer"] == "...":
            sleep(1)
            print("Gwen goes to Miguel")
            gwen()
            sleep(1.5)
            gwen()
            print(bright_magenta)
            print(f"We cant just leave {player_id} here!")
            sleep(1.5)
            miguel()
            print(bright_blue)
            print("Yes we can, we need them to stay here until the canon event ends.")
            print(bright_white)
            sleep(1.5)
            gwen()
            print("Gwen looks at you in guilt.")
            sleep(1.5)
            gwen()
            print(bright_magenta)
            print("I'm sorry Miguel")
            print(bright_white)
            print("BANGG")
            gwen()
            print("Gwen breaks the red cage!")
            gwen()
            print(bright_magenta)
            print(f"Go! {player_id} go!")
            questions = [inquirer.List(
                'answer',
                choices = ['Run'])]
            answers = inquirer.prompt(questions)

            if answers["answer"] == "Run":
                print("You start to run")
                sleep(1)
                miguelangry()
                print(bright_blue)
                print("CHASE THEM!")
                print(bright_white)
                sleep(.5)
                print("You keep running.")
                sleep(1)
                print("Everyone is right behind you.")
                sleep(1)
                print("You see a closed room.")
                questions = [inquirer.List(
                    'action',
                    choices = ['Keep running', 'Hide'])]
                answers = inquirer.prompt(questions)
        
                if answers["action"] == "Keep running":
                    print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                    sleep(.5)
                    print("Everyone is right behind you..")
                    print("You see a closed room.")
                    questions = [inquirer.List(
                        'action',
                        choices = ['Hide'])]
                    answers = inquirer.prompt(questions)
        
                    if answers["action"] == "Hide":
                        print("You hid from the crowd.. Seeing each spider person going to another route")
                        sleep(.5)
                        print("You sighed, went into the room.. it looks like a lab")
                        questions = [inquirer.List(
                            'action',
                            choices = ['Search around',])]
                        answers = inquirer.prompt(questions)

                        if answers["action"] == "Search around":
                            print("You start to search the boxes")
                            sleep(.5)
                            print("You see 3 unknown liquids in test tubes, you should drink one.")
                            questions = [inquirer.List(
                                'drink',
                                choices = ['Unknown pink liquid', 'Unknown green liquid', 'Unknown purple liquid'])]
                            answers = inquirer.prompt(questions)
                        
                            if answers["drink"] == "Unknown pink liquid":
                                player_hp = player_hp + 25
                                sleep(.5)
                                print(f"{player_id} drinks the pink liquid.. It has cotton candy in it. You gained 25 HP!")

                            elif answers["weapon"] == "Unknown green liquid":
                                player_hp = player_hp + 8
                                sleep(.5)
                                print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 8 HP!")

                            elif answers["weapon"] == "Unknown purple liquid": 
                                player_hp = player_hp + 19
                                sleep(.5)
                                print(f"{player_id} drinks the purple liquid.. Tastes like grape. You gained 19 HP!")
                                sleep(.8)
                                
                        print("Now.. maybe start searching around more..")
                        questions = [inquirer.List(
                            'action',
                            choices = ['Search around',])]
                        answers = inquirer.prompt(questions)

                        if answers["action"] == "Search around":
                            print("You start to search in one of the boxes")
                            sleep(.5)
                            print("You see a multiverse watch!")
                            questions = [inquirer.List(
                                'action',
                                choices = ['Wear it', 'Throw it on the ground'])]
                            answers = inquirer.prompt(questions)
                
                            if answers["action"] == "Wear it":
                                print("You wore the watch")
                                sleep(.5)
                                print("Boom! A portal opens")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Go inside'])]
                                answers = inquirer.prompt(questions)
                        
                                if answers["action"] == "Go inside":
                                    print(yellow)
                                    print("You went in the portal... Going to your own earth now... (Earth-43)")

                            elif answers["action"] == "Throw it on the ground":
                                print("It breaks.")
                                print("WWWWWWwwwwwwaaaaaaaaiiiiIIIIIILLLLLl!!")
                                sleep(.5)
                                print("The watch starts to alarm!! Uh oh!!")
                                sleep(.5)
                                print("Everyone barges in. You run out.")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Keep running', 'Hide'])]
                                answers = inquirer.prompt(questions)
    
                                if answers["action"] == "Keep running":
                                    print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                                    sleep(.5)
                                    print("Everyone is right behind you..")
                                    print("You see a closed room.")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Hide'])]
                                    answers = inquirer.prompt(questions)

                                    if answers["action"] == "Hide":
                                        print("You hid from the crowd.. Seeing each spider person going to another route")
                                        sleep(.5)
                                        print("In another lab..")
                                        questions = [inquirer.List(
                                            'action',
                                            choices = ['Search around',])]
                                        answers = inquirer.prompt(questions)

                                        if answers["action"] == "Search around":
                                            print("You start to search in one of the boxes")
                                            sleep(.5)
                                            print("You see a multiverse watch!")
                                            questions = [inquirer.List(
                                                'action',
                                                choices = ['Wear it'])]
                                            answers = inquirer.prompt(questions)

                                            if answers["action"] == "Wear it":
                                                print("You wore the watch")
                                                sleep(.5)
                                                print("Boom! A portal opens")
                                                questions = [inquirer.List(
                                                    'action',
                                                    choices = ['Go inside'])]
                                                answers = inquirer.prompt(questions)

                                                if answers["action"] == "Go inside":
                                                    print(yellow)
                                                    print("You went in the portal... Going to your own earth now... (Earth-43)")


            elif answers["action"] == "Hide":
                print("You hid from the crowd.. Seeing each spider person going to another route")
                sleep(.5)
                print("You sighed, went into the room.. it looks like a lab")
                questions = [inquirer.List(
                        'action',
                        choices = ['Search around',])]
                answers = inquirer.prompt(questions)

                if answers["action"] == "Search around":
                    print("You start to search the boxes")
                    sleep(.5)
                    print("You see 3 unknown liquids in test tubes, you should drink one.")
                    questions = [inquirer.List(
                        'drink',
                        choices = ['Unknown pink liquid', 'Unknown green liquid', 'Unknown purple liquid'])]
                    answers = inquirer.prompt(questions)

                    if answers["drink"] == "Unknown pink liquid":
                        player_hp = player_hp + 25
                        sleep(.5)
                        print(f"{player_id} drinks the pink liquid.. It has cotton candy in it. You gained 25 HP!")
                        sleep(.8)

                    elif answers["drink"] == "Unknown green liquid":
                        player_hp = player_hp + 8
                        sleep(.5)
                        print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 8 HP!")
                        sleep(.8)

                    elif answers["drink"] == "Unknown purple liquid":
                        player_hp = player_hp + 19
                        sleep(.5)
                        print(f"{player_id} drinks the purple liquid.. Tastes like grape. You gained 19 HP!")
                        sleep(.8)
                            
                    print("Now.. maybe start searching around more..")
                    questions = [inquirer.List(
                        'action',
                        choices = ['Search around',])]
                    answers = inquirer.prompt(questions)
                
                    if answers["action"] == "Search around":
                        print("You start to search in one of the boxes")
                        sleep(.5)
                        print("You see a multiverse watch!")
                        questions = [inquirer.List(
                            'action',
                            choices = ['Wear it', 'Throw it on the ground'])]
                        answers = inquirer.prompt(questions)
                
                        if answers["action"] == "Wear it":
                            print("You wore the watch")
                            sleep(.5)
                            print("Boom! A portal opens")
                            questions = [inquirer.List(
                                'action',
                                choices = ['Go inside'])]
                            answers = inquirer.prompt(questions)
                        
                            if answers["action"] == "Go inside":
                                print(yellow)
                                print("You went in the portal... Going to your own earth now... (Earth-43)")

                        elif answers["action"] == "Throw it on the ground":
                            print("It breaks.")
                            print("WWWWWWwwwwwwaaaaaaaaiiiiIIIIIILLLLLl!!")
                            sleep(.5)
                            print("The watch starts to alarm!! Uh oh!!")
                            sleep(.5)
                            print("Everyone barges in. You run out.")
                            questions = [inquirer.List(
                                'action',
                                choices = ['Keep running', 'Hide'])]
                            answers = inquirer.prompt(questions)

                            if answers["action"] == "Keep running":
                                print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                                sleep(.5)
                                print("Everyone is right behind you..")
                                print("You see a closed room.")
                                questions = [inquirer.List(
                                    'action',                                        
                                    choices = ['Hide'])]
                                answers = inquirer.prompt(questions)
        
                                if answers["action"] == "Hide":
                                    print("You hid from the crowd.. Seeing each spider person going to another route")
                                    sleep(.5)
                                    print("In another lab..")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Search around',])]
                                    answers = inquirer.prompt(questions)

                                    if answers["action"] == "Search around":
                                        print("You start to search in one of the boxes")
                                        sleep(.5)
                                        print("You see a multiverse watch!")
                                        questions = [inquirer.List(
                                            'action',
                                            choices = ['Wear it'])]
                                        answers = inquirer.prompt(questions)

                                        if answers["action"] == "Wear it":
                                            print("You wore the watch")
                                            sleep(.5)
                                            print("Boom! A portal opens")
                                            questions = [inquirer.List(
                                                'action',
                                                choices = ['Go inside'])]
                                            answers = inquirer.prompt(questions)

                                            if answers["action"] == "Go inside":
                                                print(yellow)
                                                print("You went in the portal... Going to your own earth now... (Earth-43)")

    elif answers["answer"] == "I am NOT staying here!":
        miguelangry()
        print(bright_blue)
        print(f"Yes you WILL.")
        sleep(.9)
        miguelangry()
        print("This is your CANON event.")
        print(bright_white)
        sleep(1)
        questions = [inquirer.List(
            'answer',
            choices = ['...'])]
        answers = inquirer.prompt(questions)

        if answers["answer"] == "...":
            sleep(1)
            print("Gwen goes to Miguel")
            sleep(1.5)
            gwen()
            print(bright_magenta)
            print(f"We cant just leave {player_id} here!")
            sleep(1.5)
            miguel()
            print(bright_blue)
            print("Yes we can, we need them to stay here until the canon event ends.")
            print(bright_white)
            sleep(1.5)
            gwen()
            print("Gwen looks at you in guilt.")
            sleep(1.5)
            gwen()
            print(bright_magenta)
            print("I'm sorry Miguel")
            print(bright_white)
            print("BANGG")
            print("Gwen breaks the red cage!")
            gwen()
            print(bright_magenta)
            print(f"Go! {player_id} go!")
            questions = [inquirer.List(
                'answer',
                choices = ['Run'])]
            answers = inquirer.prompt(questions)

            if answers["answer"] == "Run":
                print("You start to run")
                sleep(1)
                miguelangry()
                print(bright_blue)
                print("CHASE THEM!")
                print(bright_white)
                sleep(.5)
                print("You keep running.")
                sleep(1)
                print("Everyone is right behind you.")
                sleep(1)
                print("You see a closed room.")
                questions = [inquirer.List(
                    'action',
                    choices = ['Keep running', 'Hide'])]
                answers = inquirer.prompt(questions)

                if answers["action"] == "Keep running":
                    print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                    sleep(.5)
                    print("Everyone is right behind you..")
                    print("You see a closed room.")
                    questions = [inquirer.List(
                        'action',
                        choices = ['Hide'])]
                    answers = inquirer.prompt(questions)
        
                    if answers["action"] == "Hide":
                        print("You hid from the crowd.. Seeing each spider person going to another route")
                        sleep(.5)
                        print("You sighed, went into the room.. it looks like a lab")
                        questions = [inquirer.List(
                            'action',
                            choices = ['Search around',])]
                        answers = inquirer.prompt(questions)

                        if answers["action"] == "Search around":
                            print("You start to search the boxes")
                            sleep(.5)
                            print("You see 3 unknown liquids in test tubes, you should drink one.")
                            questions = [inquirer.List(
                                'drink',
                                choices = ['Unknown pink liquid', 'Unknown green liquid', 'Unknown purple liquid'])]
                            answers = inquirer.prompt(questions)
                        
                            if answers["drink"] == "Unknown pink liquid":
                                player_hp = player_hp + 25
                                sleep(.5)
                                print(f"{player_id} drinks the pink liquid.. It has cotton candy in it. You gained 25 HP!")

                            elif answers["weapon"] == "Unknown green liquid":
                                player_hp = player_hp + 8
                                sleep(.5)
                                print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 8 HP!")

                            elif answers["weapon"] == "Unknown purple liquid":
                                player_hp = player_hp + 19
                                sleep(.5)
                                print(f"{player_id} drinks the purple liquid.. Tastes like grape. You gained 19 HP!")
                                sleep(.8)
                                
                        print("Now.. maybe start searching around more..")
                        questions = [inquirer.List(
                            'action',
                            choices = ['Search around',])]
                        answers = inquirer.prompt(questions)

                        if answers["action"] == "Search around":
                            print("You start to search in one of the boxes")
                            sleep(.5)
                            print("You see a multiverse watch!")
                            questions = [inquirer.List(
                                'action',
                                choices = ['Wear it', 'Throw it on the ground'])]
                            answers = inquirer.prompt(questions)
                
                            if answers["action"] == "Wear it":
                                print("You wore the watch")
                                sleep(.5)
                                print("Boom! A portal opens")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Go inside'])]
                                answers = inquirer.prompt(questions)
                        
                                if answers["action"] == "Go inside":
                                    print(yellow)
                                    print("You went in the portal... Going to your own earth now... (Earth-43)")

                            elif answers["action"] == "Throw it on the ground":
                                print("It breaks.")
                                print("WWWWWWwwwwwwaaaaaaaaiiiiIIIIIILLLLLl!!")
                                sleep(.5)
                                print("The watch starts to alarm!! Uh oh!!")
                                sleep(.5)
                                print("Everyone barges in. You run out.")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Keep running', 'Hide'])]
                                answers = inquirer.prompt(questions)
        
                                if answers["action"] == "Keep running":
                                    print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                                    sleep(.5)
                                    print("Everyone is right behind you..")
                                    print("You see a closed room.")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Hide'])]
                                    answers = inquirer.prompt(questions)
        
                                    if answers["action"] == "Hide":
                                        print("You hid from the crowd.. Seeing each spider person going to another route")
                                        sleep(.5)
                                        print("In another lab..")
                                        questions = [inquirer.List(
                                            'action',
                                            choices = ['Search around',])]
                                        answers = inquirer.prompt(questions)

                                        if answers["action"] == "Search around":
                                            print("You start to search in one of the boxes")
                                            sleep(.5)
                                            print("You see a multiverse watch!")
                                            questions = [inquirer.List(
                                                'action',
                                                choices = ['Wear it'])]
                                            answers = inquirer.prompt(questions)

                                            if answers["action"] == "Wear it":
                                                print("You wore the watch")
                                                sleep(.5)
                                                print("Boom! A portal opens")
                                                questions = [inquirer.List(
                                                    'action',
                                                    choices = ['Go inside'])]
                                                answers = inquirer.prompt(questions)

                                                if answers["action"] == "Go inside":
                                                    print(yellow)
                                                    print("You went in the portal... Going to your own earth now... (Earth-43)")


            elif answers["action"] == "Hide":
                print("You hid from the crowd.. Seeing each spider person going to another route")
                sleep(.5)
                print("You sighed, went into the room.. it looks like a lab")
                questions = [inquirer.List(
                    'action',
                    choices = ['Search around',])]
                answers = inquirer.prompt(questions)

                if answers["action"] == "Search around":
                    print("You start to search the boxes")
                    sleep(.5)
                    print("You see 3 unknown liquids in test tubes, you should drink one.")
                    questions = [inquirer.List(
                        'drink',
                        choices = ['Unknown pink liquid', 'Unknown green liquid', 'Unknown purple liquid'])]
                    answers = inquirer.prompt(questions)

                    if answers["drink"] == "Unknown pink liquid":
                        player_hp = player_hp + 25
                        sleep(.5)
                        print(f"{player_id} drinks the pink liquid.. It has cotton candy in it. You gained 25 HP!")
                        sleep(.8)

                    elif answers["drink"] == "Unknown green liquid":
                        player_hp = player_hp + 8
                        sleep(.5)
                        print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 8 HP!")
                        sleep(.8)

                    elif answers["drink"] == "Unknown purple liquid":
                        player_hp = player_hp + 19
                        sleep(.5)
                        print(f"{player_id} drinks the purple liquid.. Tastes like grape. You gained 19 HP!")
                        sleep(.8)
                            
                    print("Now.. maybe start searching around more..")
                    questions = [inquirer.List(
                        'action',
                        choices = ['Search around',])]
                    answers = inquirer.prompt(questions)

                    if answers["action"] == "Search around":
                        print("You start to search in one of the boxes")
                        sleep(.5)
                        print("You see a multiverse watch!")
                        questions = [inquirer.List(
                            'action',
                            choices = ['Wear it', 'Throw it on the ground'])]
                        answers = inquirer.prompt(questions)
                
                        if answers["action"] == "Wear it":
                            print("You wore the watch")
                            sleep(.5)
                            print("Boom! A portal opens")
                        questions = [inquirer.List(
                                'action',
                                choices = ['Go inside'])]
                        answers = inquirer.prompt(questions)
                        
                        if answers["action"] == "Go inside":
                            print(yellow)
                            print("You went in the portal... Going to your own earth now... (Earth-43)")

                        elif answers["action"] == "Throw it on the ground":
                            print("It breaks.")
                            print("WWWWWWwwwwwwaaaaaaaaiiiiIIIIIILLLLLl!!")
                            sleep(.5)
                            print("The watch starts to alarm!! Uh oh!!")
                            sleep(.5)
                            print("Everyone barges in. You run out.")
                            questions = [inquirer.List(
                                'action',
                                choices = ['Keep running', 'Hide'])]
                            answers = inquirer.prompt(questions)
        
                            if answers["action"] == "Keep running":
                                print("You run a fast as you can. Webbing the ceiling and swinging through the air.")
                                sleep(.5)
                                print("Everyone is right behind you..")
                                print("You see a closed room.")
                                questions = [inquirer.List(
                                    'action',
                                    choices = ['Hide'])]
                                answers = inquirer.prompt(questions)
        
                                if answers["action"] == "Hide":
                                    print("You hid from the crowd.. Seeing each spider person going to another route")
                                    sleep(.5)
                                    print("In another lab..")
                                    questions = [inquirer.List(
                                        'action',
                                        choices = ['Search around',])]
                                    answers = inquirer.prompt(questions)

                                    if answers["action"] == "Search around":
                                        print("You start to search in one of the boxes")
                                        sleep(.5)
                                        print("You see a multiverse watch!")
                                        questions = [inquirer.List(
                                            'action',
                                            choices = ['Wear it'])]
                                        answers = inquirer.prompt(questions)

                                        if answers["action"] == "Wear it":
                                            print("You wore the watch")
                                            sleep(.5)
                                            print("Boom! A portal opens")
                                            questions = [inquirer.List(
                                                'action',
                                                choices = ['Go inside'])]
                                            answers = inquirer.prompt(questions)

                                            if answers["action"] == "Go inside":
                                                print(yellow)
                                                print("You went in the portal... Going to your own earth now... (Earth-43)")

sleep(2.5)
system("clear")
print(bright_white)

pygame.mixer.music.stop()
pygame.mixer.music.load('bossbatterahhhhhh.mp3')
pygame.mixer.music.play(0)
pygame.mixer.music.play(0, fade_ms=0)

print(yellow)
print("You've been teleported into your own world.. (Earth-43)")
print(bright_white)
sleep(.5)
print("It's a mess! Everything is messed up! Spot is destroying everything!")
questions = [inquirer.List(
    'action',
    choices = ['Run to the scene where Spot is destoying everything.'])]
answers = inquirer.prompt(questions)

if answers["action"] == "Run to the scene where Spot is destoying everything.":
    print("You start to web towards Spot ")
    sleep(.5)
    spot()
    print(f"Oh! Hello {player_id}!~")
    sleep(1)
    print("Spot sees you webbiing towards him.")
    spot()
    sleep(1.5)
    print("Spot is right there!")

pygame.mixer.music.stop()
pygame.mixer.init()
pygame.mixer.music.load('intro.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.play(-1, fade_ms=1)

while True:
    print("")
    sleep(.8)
    spot()
    sleep(1)
    
    print("\n")
    print("--------------------------------------------")
    print("\n")
    
    print(f"Spot: {spot_hp} HP")
    print(f"{player_id}: {player_hp} HP")

    questions = [inquirer.List(
        'action',
        choices = ['Web towards him and kick his face', 'Attack in a different way', 'Ask for help'])]
    answers = inquirer.prompt(questions)

    if answers["action"] == "Web towards him and kick his face":
        sleep(.8)
        print(f"{player_id} kicks Spot's face!")
        sleep(1)
        spotangry()
        player_dmg = randint(0,100)
        if player_dmg >= 100:
            spot_hp -= player_dmg
            sleep(.8)
            print(f"You did a critical hit! {player_dmg} DMG to Spot!")
            sleep(1)
            spotty1()
        elif player_dmg <=0:
            sleep(.8)
            print(f"{player_id} did not do any damage")
            sleep(1)
            spot()
        else:
            spot_hp -= player_dmg
            sleep(.8)
            print(f"You did {player_dmg} damage to Spot!")
            sleep(1)
            spotty1()

    elif answers ["action"] == "Attack in a different way":
        sleep(.8)
        print(f"{player_id} rushes towards Spot, starting to fight hand on hand combat")
        player_dmg = randint(0,100)
        if player_dmg >= 100:
            spot_hp -= player_dmg
            sleep(.8)
            print(f"You did a critical hit! {player_dmg} DMG to Spot!")
            sleep(1)
            spotty1()
        elif player_dmg <=0:
            print(f"{player_id} did not do any damage")
            sleep(1)
            spot()
        else:
            spot_hp -= player_dmg
            sleep(.8)
            print(f"You did {player_dmg} damage to Spot!")
            sleep(1)
            spotangry()

    elif answers ["action"] == "Ask for help":
        print("You try to run away from Spot.")

        run_chance = randint(0,500)

        if run_chance <= 500:
            sleep(.8)
            print("You couldn't run away.")
            sleep(.4)
            print("You have to keep fighting Spot.")
            sleep(2)
            spotty1()

        elif run_chance <= 0:
            sleep(.8)
            print("You ran away. Spot killed everyone and your dad.")
            spot()
            break

    spot_dmg = randint(0,100)
    
    if spot_dmg >= 100:
        spot_hp -= player_dmg
        sleep(.8)
        print(f"Spot did a critical hit! {spot_dmg} DMG to {player_id}!")
        sleep(1)
        spotty1()
    
    elif spot_dmg <=0:
        print("Spot did not do any damage")
    
    else:
        player_hp -= spot_dmg
        sleep(.8)
        print(f"Spot did {spot_dmg} DMG to {player_id}!")

    if player_hp < 10:
        player_hp = player_hp + 500
        player_hp -= spot_dmg
        sleep(.8)
        print(f"{player_id} is about to die!!")
        sleep(1)
        print("...")
        sleep(1.2)
        print(bright_red)
        print("Miguel has entered Earth-43.")
        print(bright_white)
        
        pygame.mixer.music.stop()
        pygame.mixer.music.load('spider-man 2099.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.play(-1, fade_ms=5000)
        pygame.mixer.music.load('intro.mp3')
        
        miguel()
        sleep(1)
        print("Miguel sighs")
        sleep(1)
        print(bright_blue)
        print("You've got to be kidding me.")
        print(bright_white)
        sleep(.5)
        print("Gwen also has enetered Earth-43")
        sleep(1)
        gwen()
        sleep(1)
        print(bright_magenta)
        print(f"Hii {player_id}!! Lets fight them!")
        print(bright_white)
            
        while True:
            sleep(1)
            print("Miguel is going close to Spot! Starting to do hand in hand combat")
            miguel_dmg = randint(0,600)

            if miguel_dmg > 600:
                spot_hp -= miguel_dmg
                sleep(.8)
                print(f"Miguel did a critical hit! {miguel_dmg} DMG to Spot!")
                sleep(1)
                miguel()

            elif miguel_dmg < 0:
                print(f"Miguel did not do any damage")
                sleep(1)
                miguel()

            else:
                spot_hp - miguel_dmg
                sleep(.8)
                print(f"Miguel did {miguel_dmg} damage to Spot!")
                sleep(1)
                miguel()

            sleep(1)
            print("Gwen webs Spot and ties him up! She punches Spot")
            gwen_dmg = randint(0,120)

            if gwen_dmg > 120:
                spot_hp -= miguel_dmg
                sleep(.8)
                print(f"Gwen did a critical hit! {gwen_dmg} DMG to Spot!")
                sleep(1)
                gwen()

            elif gwen_dmg < 0:
                print(f"Gwen did not do any damage")
                sleep(1)
                gwen()

            else:
                spot_hp - gwen_dmg
                sleep(.8)
                print(f"Gwen did {gwen_dmg} damage to Spot!")
                sleep(1)
                gwen()

            print("")
            sleep(.8)
            spot()
            sleep(2)
    
            print("\n")
            print("--------------------------------------------")
            print("\n")
    
            print(f"Spot: {spot_hp} HP")
            print(f"{player_id}: {player_hp} HP")
            
            questions = [inquirer.List(
                'action',
                choices = ['Web towards him and kick his face', 'Attack in a different way', 'Ask for help'])]
            answers = inquirer.prompt(questions)

            if answers["action"] == "Web towards him and kick his face":
                sleep(.8)
                print(f"{player_id} kicks Spot's face!")
                sleep(1)
                spotangry()
                player_dmg = randint(0,100)
                
                if player_dmg >= 100:
                    spot_hp -= player_dmg
                    sleep(.8)
                    print(f"You did a critical hit! {player_dmg} DMG to Spot!")
                    sleep(1)
                    spotty1()
                
                elif player_dmg <=0:
                    sleep(.8)
                    print(f"{player_id} did not do any damage")
                    sleep(1)
                    spot()
                
                else:
                    spot_hp -= player_dmg
                    sleep(.8)
                    print(f"You did {player_dmg} damage to Spot!")
                    sleep(1)
                    spotty1()

            elif answers ["action"] == "Attack in a different way":
                sleep(.8)
                print(f"{player_id} rushes towards Spot, starting to fight hand on hand combat")
                player_dmg = randint(0,100)
                
                if player_dmg >= 100:
                    spot_hp -= player_dmg
                    sleep(.8)
                    print(f"You did a critical hit! {player_dmg} DMG to Spot!")
                    sleep(1)
                    spotty1()
                
                elif player_dmg <=0:
                    print(f"{player_id} did not do any damage")
                    sleep(1)
                    spot()
        
                else:
                    spot_hp -= player_dmg
                    sleep(.8)
                    print(f"You did {player_dmg} damage to Spot!")
                    sleep(1)
                    spotangry()

            elif answers ["action"] == "Ask for help":
                print("You try to run away from Spot.")

                run_chance = randint(0,500)

                if run_chance <= 500:
                    sleep(.8)
                    print("You couldn't run away.")
                    sleep(.4)
                    print("You have to keep fighting Spot.")
                    sleep(2)
                    spotty1()

                elif run_chance <= 0:
                    sleep(.8)
                    print("You ran away. Spot killed everyone and your dad.")
                    spot()
                    break

                spot_dmg = randint(0,40)
    
                if spot_dmg >= 40:
                    spot_hp -= player_dmg
                    sleep(.8)
                    print(f"Spot did a critical hit! {spot_dmg} DMG to {player_id}!")
                    sleep(1)
                    spotty1()
    
                elif spot_dmg <=0:
                    print("Spot did not do any damage")
    
                else:
                    player_hp -= spot_dmg
                    sleep(.8)
                    print(f"Spot did {spot_dmg} DMG to {player_id}!")
        
            if spot_hp < 0:
                system("clear")
            
                pygame.mixer.music.stop()
                pygame.mixer.music.load('youlikejazz.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.play(-1, fade_ms=0)
            
                print("You succeded on fighting Spot! He starts to corrupt.")
                sleep(2)
                print(f"AhHHHHHh {player_id} YOU. WILL. PAY. FOR THIS!!")
                spotangry()
                sleep(1)
                print("plop")
                sleep(1)
                spotblob()
                sleep(1)
                print("Spot turned into a weird blob.")
                spotty2()
                sleep(5)
                break
    

print("\n")
print("--------------------------------------------")
print("\n")


sleep(5)
print(bright_cyan)
print(f"Thanks for playing Across the Spiderverse 1, {player_id}! This game was made by Meepy! (Kylie)")
sleep(5)
input("press enter to clear up the screen !!")
system("clear")
print(bright_red)
print("play again")
