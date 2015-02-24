import time
import math

#Init of variables
startTime = []  #List of the start times for my events
startTimeSeconds = []
eventList = []  #List of my events

#Defining mah functions
def addEvent():
    nowStart = time.asctime(time.localtime(time.time()))
    nowStartTime = time.time()
    startTime.append(nowStart)
    startTimeSeconds.append(nowStartTime)
    s = raw_input('Event Name --> ')
    eventList.append(s)

def finishEvent():
    f = open('Day Tracker.txt', 'a+')   #Creates the Day Tracker.txt if it doesn't exist, or adds on to it
    nowFinish = time.asctime(time.localtime(time.time()))
    nowFinishTime = time.time()
    timeSpentMins = round(((nowFinishTime - startTimeSeconds[-1])/60), 0)
    timeSpentSeconds = round((nowFinishTime - startTimeSeconds[-1]), 0)
    if timeSpentMins > 1.0:
        f.write('From ' + startTime[-1] + ' to ' + nowFinish + ' I did: ' + eventList[-1] + ' for ' + str(timeSpentMins) + ' minutes' + '\n')
    else:
        f.write('From ' + startTime[-1] + ' to ' + nowFinish + ' I did: ' + eventList[-1] + ' for ' + str(timeSpentSeconds) + ' seconds' + '\n')
    f.close()         #Done using the .txt file so I close it. This way the file is opened only when it is needed and can be accessed at other times
#Runs all the functions in the necessary order and stuff
def startProg():
    print 'Welcome to Day Tracker!'
    print 'Starting Day Tracker...'
    whileVar = ''
    while whileVar != 'q':
        addEvent()
        whileVar = raw_input('Press enter when finished with event or press q to quit...')
        finishEvent()
    print 'Thank you for using Day Tracker! Have a nice day!~'

#Starting program
startProg()

#TO-DO: #Add a way to see how much time has been spent on current event
