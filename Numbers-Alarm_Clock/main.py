# Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
import winsound
import time
from datetime import datetime



timeInput = input("What time do you want to set your alarm? in HH:MM:SS format: ")
dateInput = input("Please enter the date in YYYY/MM/DD format: ")

alarm_time = datetime.strptime('%s %s'%(dateInput, timeInput),"%Y/%m/%d  %H:%M:%S")
print("Alarm clock set for " + str(alarm_time))

while alarm_time >= datetime.now():
    time.sleep(1)

print("Alarm clock activated! It's " + str(alarm_time))
# winsound.PlaySound('sound.wav', winsound.SND_LOOP)
for i in range(0,10):
    winsound.Beep(440, 500)
