import time
from pygame import mixer
from datetime import datetime
mixer.init()
def drinkwater():
    print("Time To Drink Water")
    while True:
        mixer.music.load("Please-Go-And-Drink-Water.ogg")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        n = str(input("Have You Drink Water?\nY(Yes)/N(No)\n"))
        n1 = n.upper()
        if n1 == 'N':
            time.sleep(1)
            continue
        elif n1 == 'Y':
            mixer.music.load("Thank-You-For-Drinking-Water.ogg")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            break
        else:
            print("Invalid Input")
            time.sleep(1)
            continue
###########Drinkwater Function End#####################
###########Relax Eyes Function Start###################
def relaxeyes():
    print("Time To Relax Eyes")
    while True:
        mixer.music.load("Please-Go-And-Give-Rest-To-Your-Eyes.ogg")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        n = str(input("Have You Take Rest For Your Eyes?\nY(Yes)/N(No)\n"))
        n1 = n.upper()
        if n1 == 'N':
            time.sleep(1)
            continue
        elif n1 == 'Y':
            mixer.music.load("Thank-You-For-Resting-Your-Eyes.ogg")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            break
        else:
            print("Invalid Input")
            time.sleep(1)
            continue
###########Relax Eyes Function End#####################
###########Physical Exercise Function Start############
def physical():
    print("Time To Do Exercise")
    while True:
        mixer.music.load("Time-to-Do-Some-Physical-Exercise.ogg")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        n = str(input("Have You Done Physical Exercise?\nY(Yes)/N(No)\n"))
        n1 = n.upper()
        if n1 == 'N':
            time.sleep(1)
            continue
        elif n1 == 'Y':
            mixer.music.load("Thank-You-For-Doing-Physical-Exercise.ogg")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            break
        else:
            print("Invalid Input")
            time.sleep(1)
            continue
###########Physical Exercise Function End##############
###########Check Function Start########################
def check():
    if datetime.now().strftime("%H:%M") == '00:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '00:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '01:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '01:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '01:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '02:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '02:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '02:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '03:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '03:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '03:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '04:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '04:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '04:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '05:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '05:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '05:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '06:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '06:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '06:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '07:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '07:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '07:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '08:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '08:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '08:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '09:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '09:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '09:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '10:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '10:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '10:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '11:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '11:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '11:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '12:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '12:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '12:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '13:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '13:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '13:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '14:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '14:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '14:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '15:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '15:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '15:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '16:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '16:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '16:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '17:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '17:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '17:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '18:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '18:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '18:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '19:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '19:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '19:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '20:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '20:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '20:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '21:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '21:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '21:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '22:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '22:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '22:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '23:00':
        physical()
    elif datetime.now().strftime("%H:%M") == '23:30':
        drinkwater()
    elif datetime.now().strftime("%H:%M") == '23:45':
        relaxeyes()
    elif datetime.now().strftime("%H:%M") == '00:00':
        physical()
###########Check Function End##########################
while True:
    check()
    time.sleep(60)
