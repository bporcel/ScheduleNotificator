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
    weekDay = datetime.today().weekday()
    hour = datetime.now().hour
    minutes = datetime.now().minute
    strHour = str(hour)
    if hour == 7 or hour == 14 or hour == 15:
        if minutes >= 30:
            sendNotification(strHour, schedule)
    elif hour == 8:
        if minutes >= 15:
            sendNotification(strHour, schedule)
    elif hour == 18:
        if weekDay % 2 != 0:
            climbing = "Deberias estar escalando... no?"
            schedule[strHour]['body'] = climbing
        sendNotification(strHour, schedule)
    elif hour == 20:
        tvShow = "Se acabó por hoy, toca ir a cenar. Y no te olvides, HOY SE MIRA SERIE"
        book = "Se acabó por hoy, toca ir a cenar. Y no te olvides, HOY SE LEE"
        if weekDay % 2 == 0:
            schedule[strHour]['body'] = book
        else:
            schedule[strHour]['body'] = tvShow

        sendNotification(strHour, schedule)
    else:
        sendNotification(strHour, schedule)


def scheduleNotificator(schedule):
    checkTime()
    time.sleep(60)
    scheduleNotificator(schedule)


# Start of the Script ------------------------------------------------------------------
weekDay = datetime.today().weekday()
if weekDay != 5 and weekDay != 6:
    try:
        schedule = getSchedule()
        if schedule:
            subprocess.Popen(['notify-send', 'Scheduler',
                              'Scheduler started succesfully'])
            scheduleNotificator(schedule)
        else:
            subprocess.Popen(['notify-send', 'Scheduler',
                              'No he podido encontrar el horario para el día de hoy'])
    except:
        subprocess.Popen(['notify-send', 'Scheduler',
                          'Error during program execution'])
else:
    subprocess.Popen(['notify-send', 'Scheduler',
                      'Enjoy your weekend!'])
