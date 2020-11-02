import pyttsx3
import psutil

battery = psutil.sensors_battery()  # Power initialization
startplugged = battery.power_plugged
percent = str(battery.percent)

if startplugged:
    status = "Connected"
else:
    status = "Disconnected"


engine = pyttsx3.init()  # object creation

""" RATE"""
engine.setProperty('rate', 180)     # setting up new voice rate


"""VOLUME"""
engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Welcome")  # greetings


while True:
    battery = psutil.sensors_battery()
    percent = str(battery.percent)
    plugged = battery.power_plugged

    if status == "Connected":
        if not plugged:
            status = "Disconnected"
            engine.say('Charger disconnected at ' + percent + 'percent')

    if status == "Disconnected":
        if plugged:
            status = "Connected"
            engine.say("Charger connected")

    if plugged:
        if battery.percent == 100:
            engine.say("Battery full, Please remove your charger")
    engine.runAndWait()
