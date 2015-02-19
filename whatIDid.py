import time
import math

#Init of variables
f = open('My Day.txt', 'r+')
startTime = []  #List of the start times for my events
startTimeSeconds = []
eventList = []  #List of my events

#Defining my functions
#Empty the file
def clearNotepad():
    f.truncate()

def addEvent():
    nowStart = time.asctime(time.localtime(time.time()))
    nowStartTime = time.time()
    startTime.append(nowStart)
    startTimeSeconds.append(nowStartTime)
    s = raw_input('Event Name --> ')
    eventList.append(s)

def finishEvent():
    nowFinish = time.asctime(time.localtime(time.time()))
    nowFinishTime = time.time()
    timeSpent = round(((nowFinishTime - startTimeSeconds[-1])/60), 0)
    f.write('From ' + startTime[-1] + ' to ' + nowFinish + ' I did: ' + eventList[-1] + ' for ' + str(timeSpent) + ' minutes' + '\n')

#Runs all the functions in the necessary order and stuff
def startProg():
    print 'Welcome to Day Tracker!'
    print 'Starting Day Tracker...'
    clearNotepad()
    whileVar = ''
    while whileVar != 'q':
        addEvent()
        whileVar = raw_input('Press y when finished with event or press q to quit...')
        finishEvent()
    f.close()
    print 'Thank you for using Day Tracker! Have a nice day!~'

#Starting program
startProg()

#TO-DO: #Add a way to see how much time has been spent on current event
        #Add a way to access the .txt while program is running
        #Make the program not rewrite the file each time (add on to the last line so it's not a one day thing)
