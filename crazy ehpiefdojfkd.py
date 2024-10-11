import inquirer
from random import randint
from time import sleep
from os import system
import pygame

player_hp = 100
spot_hp = 200

def miguel():
    print(r"""  ____________
 / __________ \
<_/   ⩌  ⩌   \_>
 <\__________/> 
 /|___// \\__|\
૮_|    \_/   |_ა 
   \___/ \___/
""")
    
def miguelangry():
    print(r"""  ____________
 / __________ \
<_/ ꐦ⩌  ⩌   \_>
 <\__________/> 
 /|___// \\__|\
૮_|    \_/   |_ა 
   \___/ \___/
""")
     
def gwen():
    print(r"""
   __________
 / _________  \  
<\/  •́    •̀ \   >
  \_________/  /
 /|/_  \/  _\/\        
૮_|___\ _ /__|_ა        
   \___/ \___/
""")
    
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


player_id = input("Please type in your spidername.")
player_gender = input("And a gender (Man/Woman/person).").lower()
sleep(.5)

print(f"""Player Stats
Name : {player_id}
Gender : {player_gender}
Health : {player_hp}
""")

pygame.mixer.init()
pygame.mixer.music.load('intro.mp3')
pygame.mixer.music.play(-1)

pygame.mixer.music.play(-1, fade_ms=1)
pygame.mixer.music.fadeout(9500)
0
sleep(2)
print("ugh...")
sleep(1.5)
print("What's...")
sleep(1)
print("You wake up in a red cage.")
sleep(1.5)
print("Everyone watches you")
sleep(1)
print("One")
sleep(.5)
print("By")
sleep(.5)
print("One.")
sleep(.5)
print("Every spider person is watching you from afar.")
sleep(3)
print("tap")
sleep(.5)
print("tap") 


pygame.mixer.init()
pygame.mixer.music.load('spider-man 2099.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.play(-1, fade_ms=1)
pygame.mixer.music.fadeout(65000)

print("tap")
sleep(.5)
print("Miguel is now in front of you.")
sleep(.5)
miguel()
print(f"You don't belong here {player_id}.")
questions = [inquirer.List(
             'answer',
            choices = ['Yes I do', 'What?', 'You are right I do not'])]
answers = inquirer.prompt(questions)

if answers["answer"] == "Yes I do":
    print("BANG!")
    miggy1()
    print("Miguel hits the cage.. scaring you.")
    miguel()
    sleep(.9)
    print(f"You do not belong here {player_id}.")
    questions = [inquirer.List(
            'answer',
            choices = ['Shut it!...', 'Stop I do belong here!'])]
    answers = inquirer.prompt(questions)

    if answers["answer"] == "Shut it!...":
        miguel()
        print(f"You were not supposed to be bitten {player_id}.")
        print("Miguel rubs his temples.")
        miggy1()
        sleep(.9)
        miguelangry()
        print(f"What is so hard to understand from that {player_id}?!")

        questions = [inquirer.List(
            'answer',
            choices = ['Try breaking out', 'Keep silent'])]
        answers = inquirer.prompt(questions)

        if answers["answer"] == "Try breaking out":
            print("You start to bang on the red cage")
            sleep(1)
            miguel()
            print("Quiet down... Cállate")
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
                print(f"We cant just leave {player_id} here!")
                sleep(1.5)
                miguel()
                print("Yes we can, we need them to stay here until the canon event ends.")
                sleep(1.5)
                gwen()
                print("Gwen looks at you in guilt.")
                sleep(1.5)
                gwen
                print("I'm sorry Miguel")
                print("BANGG")
                gwen()
                print("Gwen breaks the red cage!")
                gwen()
                print(f"Go! {player_id} go!")
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
                                print(f"{player_id} drinks the green liquid.. Tastes like grape. You gained 19 HP!")
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
                                print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 1 HP!")
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
                                                    print("You went in the portal... Going to your own earth now... (Earth-43)")

        elif answers["answer"] == "Keep silent":
            sleep(1)
            print("Gwen goes to Miguel.")
            gwen()
            sleep(1.5)
            gwen()
            print(f"We cant just leave {player_id} here!")
            sleep(1.5)
            miguel()
            print("Yes we can, we need them to stay here until the canon event ends.")
            sleep(1.5)
            gwen()
            print("Gwen looks at you in guilt.")
            sleep(1.5)
            gwen()
            print("I'm sorry Miguel")
            print("BANGG")
            print("Gwen breaks the red cage!")
            gwen()
            print(f"Go! {player_id} go!")
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
                            print(f"{player_id} drinks the pink liquid.. It has cotton candy in it. You gained 15 HP!")
                            sleep(.8)

                        elif answers["drink"] == "Unknown green liquid":
                            player_hp = player_hp + 8
                            sleep(.5)
                            print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 1 HP!")
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
                                                    print("You went in the portal... Going to your own earth now... (Earth-43)")


    elif answers["answer"] == "Stop I do belong here!":
        miguel()
        print(f"You were not supposed to be bitten {player_id}.")
        print("Miguel rubs his nose bridge.")
        sleep(.9)
        miguelangry()
        print(f"What is so hard to understand from that {player_id}?!")
        questions = [inquirer.List(
            'answer',
            choices = ['Try breaking out', 'Keep silent'])]
        answers = inquirer.prompt(questions)

        if answers["answer"] == "Try breaking out":
            print("You start to bang on the red cage")
            sleep(1)
            miguel()
            print("Quiet down... Cállate")
            questions = [inquirer.List(
                'answer',
                choices = ['...'])]
            answers = inquirer.prompt(questions)

            if answers["answer"] == "...":
                sleep(1)
                print("Gwen goes to Miguel")
                gwen()
                sleep(1.5)
                print(f"We cant just leave {player_id} here!")
                sleep(1.5)
                miguel()
                print("Yes we can, we need them to stay here until the canon event ends.")
                sleep(1)
                gwen()
                print("Gwen looks at you in guilt.")
                sleep(1.5)
                gwen()
                print("I'm sorry Miguel")
                print("BANGG")
                print("Gwen breaks the red cage!")
                gwen()
                print(f"Go! {player_id} go!")
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
                                                    print("You went in the portal... Going to your own earth now... (Earth-43)")



        elif answers["answer"] == "Keep silent":
            sleep(1)
            gwen()
            print("Gwen goes to Miguel.")
            sleep(1.5)
            gwen()
            print(f"We cant just leave {player_id} here!")
            sleep(1.5)
            miguel()
            print("Yes we can, we need them to stay here until the canon event ends.")
            sleep(1.5)
            gwen()
            print("Gwen looks at you in guilt.")
            sleep(1.5)
            gwen()
            print("I'm sorry Miguel")
            print("BANGG")
            print("Gwen breaks the red cage!")
            gwen()
            print(f"Go! {player_id} go!")
            questions = [inquirer.List(
                'answer',
                choices = ['Run'])]
            answers = inquirer.prompt(questions)

            if answers["answer"] == "Run":
                print("You start to run")
                sleep(1)
                miguelangry()
                print("CHASE THEM!")
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
                                                    print("You went in the portal... Going to your own earth now... (Earth-43)")

elif answers["answer"] == "What?":
    miguel()
    print(f"You never were supposed to be a spider{player_gender}")
    sleep(.9)
    print("You're an anomaly.")
    questions = [inquirer.List(
        'answer',
        choices = ['What is an anomaly?'])]
    answers = inquirer.prompt(questions)

    if answers["answer"] == "What is an anomaly?":
        miguelangry()
        print("It means, you are not some normal spiderman, YOU were not supposed to get bitten!.")
        print("Miguel rubs his temples.")
        sleep(.9)
        miguel()
        print(f"What is so hard to understand from that {player_id}?!")
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
            print(f"We cant just leave {player_id} here!")
            sleep(1.5)
            miguel()
            print("Yes we can, we need them to stay here until the canon event ends.")
            sleep(1.5)
            gwen()
            print("Gwen looks at you in guilt.")
            sleep(1.5)
            gwen()
            print("I'm sorry Miguel")
            print("BANGG")
            print("Gwen breaks the red cage!")
            gwen()
            print(f"Go! {player_id} go!")
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
                        player_hp = player_hp + 1
                        sleep(.5)
                        print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 1 HP!")
                        sleep(.8)

                    elif answers["drink"] == "Unknown purple liquid":
                        player_hp = player_hp + 9
                        sleep(.5)
                        print(f"{player_id} drinks the purple liquid.. Tastes like grape. You gained 9 HP!")
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
                                                    print("You went in the portal... Going to your own earth now... (Earth-43)")

elif answers["answer"] == "You are right I do not":
    miguel()
    print("Thank you! You actually agree on something I said!")
    sleep(1)
    miguel()
    print(f"{player_id}, you still have to stay here for 2 days until your dad dies.")
    questions = [inquirer.List(
            'answer',
            choices = ['You are crazy!', 'I am NOT staying here!'])]
    answers = inquirer.prompt(questions)

    if answers["answer"] == "You are crazy":
        miguel()
        print("It's for your own good.")
        print("Miguel rubs his temples.")
        sleep(.9)
        miguel()
        print(f"This is your canon event, {player_id}.")
        questions = [inquirer.List(
            'answer',
            choices = ['...'])]
        answers = inquirer.prompt(questions)

        if answers["answer"] == "...":
            sleep(1)
            print("Gwen goes to Miguel")
            sleep(1.5)
            print(f"We cant just leave {player_id} here!")
            sleep(1.5)
            miguelangry()
            print("Yes we can, we need them to stay here until the canon event ends.")
            sleep(1.5)
            print("Gwen looks at you in guilt.")
            sleep(1.5)
            print("I'm sorry Miguel")
            print("BANGG")
            print("Gwen breaks the red cage!")
            print(f"Go! {player_id} go!")
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
                                                print("You went in the portal... Going to your own earth now... (Earth-43)")



    elif answers["answer"] == "I am NOT staying here!":
        miguelangry()
        print(f"Yes you WILL.")
        sleep(.9)
        miguelangry()
        print("This is your CANON event.")
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
            print(f"We cant just leave {player_id} here!")
            sleep(1.5)
            miguel()
            print("Yes we can, we need them to stay here until the canon event ends.")
            sleep(1.5)
            gwen()
            print("Gwen looks at you in guilt.")
            sleep(1.5)
            gwen()
            print("I'm sorry Miguel")
            print("BANGG")
            print("Gwen breaks the red cage!")
            gwen()
            print(f"Go! {player_id} go!")
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
                        player_hp = player_hp + 15
                        sleep(.5)
                        print(f"{player_id} drinks the pink liquid.. It has cotton candy in it. You gained 15 HP!")
                        sleep(.8)

                    elif answers["drink"] == "Unknown green liquid":
                        player_hp = player_hp + 1
                        sleep(.5)
                        print(f"{player_id} drinks the green liquid.. Taste like it has a bit of a minty side. You gained 1 HP!")
                        sleep(.8)

                    elif answers["drink"] == "Unknown purple liquid":
                        player_hp = player_hp + 9
                        sleep(.5)
                        print(f"{player_id} drinks the purple liquid.. Tastes like grape. You gained 9 HP!")
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
                                                print("You went in the portal... Going to your own earth now... (Earth-43)")

    sleep(2.5)
    system("clear")
    print("You've been teleported into your own world.. (Earth-43)")
    sleep(.5)
    print("It's a mess! Everything is messed up! Spot is destroying everything!")
    questions = [inquirer.List(
        'action',
        choices = ['Run to the scene where Spot is destoying everything.'])]
    answers = inquirer.prompt(questions)

if answers["action"] == "Run to the scene where Spot is destoying everything.":
    print("You start to web towards Spot ")
    sleep(.5)
    print(f"Oh! Hello {player_id}!~")
    print("Spot sees you webbiing towards him.")
    spot()
    sleep(1.5)
    print("Spot is right there!")
    
while True:
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
        player_dmg = randint(0,10)
        if player_dmg >= 10:
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
        player_dmg = randint(0,10)
        if player_dmg >= 10:
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

    spot_dmg = randint(0,10)
    if spot_dmg >= 10:
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

    if spot_hp <= 0:
        print("You succeded on fighting Spot! He starts to corrupt.")
        sleep(.5)
        print(f"AhHHHHHh {player_id} YOU. WILL. PAY. FOR THIS!!")
        spotangry()
        print("plop")
        spotblob()
        sleep(.4)
        print("Spot turned into a weird blob.")
        spotty2()
        sleep(5)
        break

    if player_hp <= 0:
        player_hp -= spot_dmg
        sleep(.8)
        print(f"{player_id} has died due to dying from Spot, Spot kills everyone.")
        spot()
        sleep(5)
        break

print("\n")
print("--------------------------------------------")
print("\n")


sleep(5)
print(f"Thanks for playing {player_id}! This game was made by Meepy! (Kylie)")
sleep(5)
system("clear")
print("play again")
