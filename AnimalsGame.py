import random
from tkinter import*

def loadQuestions():    #returns a list of questions and corresponding answers
    
    qs = []

    s = '\n'
    q = ''
    ans = ''
    options = []
    
    with open('animals.txt', encoding='utf-8') as file:
        for s in file:
            ls = s.split()
            if len(ls) == 0:
                if q != '':
                    if len(options) == 2:
                        if ans == 'Yes' or ans == 'True':
                            qs.append([q, True])
                        if ans == 'No' or ans == 'False':
                            qs.append([q, False])
                    q = ''
                    ans = ''
                    options = []
            else:
                t = ' '.join(ls[1:])
                if ls[0] == '#Q':
                    q = t
                elif ls[0] == '^':
                    ans = t
                else:
                    options.append(t)
    return qs           

questions = loadQuestions()           #assigns list to variable

def shuffledQuestions():      #function returns randomized list of q and a's
    randomQs = []
    for item in questions:
        randomQs.append(item)
    random.shuffle(randomQs)
    return randomQs

total = 0
correct = 0

def goodAnswer():
    global total
    global correct
    status['text'] = 'Your answer was correct'
    status['bg'] = 'light green'
    correct += 1
    total += 1
    showScore()
  ## Update Status and Score labels accordingly
    getNewQuestion()

def badAnswer():
    global total
    global correct
    status['text'] = 'Your answer was incorrect'
    status['bg'] = 'pink'
    correct += 0
    total += 1
    showScore()
    getNewQuestion()
    
root = Tk()         #window

topFrame = Frame(root)        #sets top frame
topFrame.pack(expand=YES, fill=BOTH)

header = Label(topFrame)  #makes label
header['text'] = 'Question:'
header.pack(anchor=N)

allQuestions = shuffledQuestions()  #list of all questions randomized
item = allQuestions[0]      #list of length two with question and answer
q = item[0]             #variable for only the question
ans = item[1]           #variable for only the answer


question = Message(topFrame, width=200)        #makes message instead of label
question['text'] = q        #can test outcome by switching this variable
question.pack()                     #switch item to 'q' for final submission

def getNewQuestion():      #Gets random question and corresponding answer
    questionAndAnswer = shuffledQuestions()[0]
    q = questionAndAnswer[0]
    a = questionAndAnswer[1]
    question['text'] = q      #add or delete ', a' to test correct output
    if a == False:                          #delete ', a' for final submission
        no['command'] = goodAnswer                  
        yes['command'] = badAnswer
    else:
        no['command'] = badAnswer
        yes['command'] = goodAnswer
    
def firstQuestion():
    if ans == False:
        no['command'] = goodAnswer
        yes['command'] = goodAnswer
    else:
        no['command'] = badAnswer
        yes['command'] = goodAnswer

no = Button(topFrame)       #makes no button
no['text'] = 'No'
no['command'] =  ''  #should take in a function that takes in no parameters
no.pack(side=RIGHT, expand=YES, fill=BOTH)
yes = Button(topFrame)        #makes yes button
yes['text'] = 'Yes'
yes['command'] = '' #should take in a function that takes in no parameters
yes.pack(side=LEFT, expand=YES, fill=BOTH)

firstQuestion()         #sets the command for the buttons on the first loop

botFrame = Frame(root)        #sets bottom frame
botFrame.pack(expand=YES, fill=X)

status = Label(botFrame)            #Makes label for question status
status['text'] = 'Status'
status['bg'] = 'light yellow'     
status.pack(side = LEFT)

scoreLabel = Label(botFrame)        #Makes label for user's score
scoreLabel['text'] = 'Score 0/0'
scoreLabel.pack(side = RIGHT)
def showScore():
    scoreLabel['text'] = 'Score {0}/{1}'.format(correct,total)
showScore()

mainloop()









