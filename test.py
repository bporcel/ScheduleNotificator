import subprocess
import time
import json
from datetime import datetime


def getSchedule():
    try:
        with open('/home/hacko/dev/repositories/day2day/schedule.json') as readContent:
            return json.load(readContent)
    except:
        return False


def sendNotification(hour, schedule):
    currentTime = datetime.now().strftime('%H:%M')
    if hour in schedule.keys():
        if not schedule[hour]['notified']:
            title = schedule[hour]['title'] + ' ' + currentTime
            body = schedule[hour]['body']
            subprocess.Popen(['notify-send', title, body])
            schedule[hour]['notified'] = True


def checkTime():
    seconds = str(datetime.now().second)
    print(seconds)
    sendNotification(seconds, schedule)


def scheduleNotificator(schedule):
    checkTime()
    time.sleep(1)
    return scheduleNotificator(schedule)


weekDay = datetime.today().weekday()
if weekDay != 5 and weekDay != 6:
    # try:
    schedule = getSchedule()
    if schedule:
        print('Scheduler started succesfully')
        scheduleNotificator(schedule)
    else:
        print('No he podido encontrar el horario para el día de hoy')
# except:
#     print('Error during program execution')
